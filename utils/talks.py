import calendar
import os
import shutil
from collections import defaultdict
from datetime import datetime
from string import Template

import requests
from pydantic import BaseModel
from pytanis import PretalxClient
from social_cards import generate_social_card

PRETALX_BASE_URL = "https://pretalx.com/api/events/"


def fetch_submissions(api_key, event_name):
    params = "state=confirmed&expand=speakers,track,slots"
    r = requests.get(
        f"{PRETALX_BASE_URL}{event_name}/submissions?{params}",
        headers={"Authorization": api_key},
    )
    return r.json()["results"]


def submission_to_talk(sub):
    slot = sub["slots"][0]
    start_time = datetime.fromisoformat(slot["start"])
    t = defaultdict(lambda: "")
    t["title"] = sub["title"]
    t["code"] = sub["code"]
    t["room"] = slot["room"]["name"]["en"].lower()
    t["abstract"] = sub["abstract"]
    t["full_description"] = sub["description"]
    t["duration_minutes"] = sub["duration"]
    t["start_time"] = start_time.strftime("%H:%M")
    t["day"] = calendar.day_name[start_time.weekday()]

    t["social_card_image"] = f"/static/talks/{sub['code']}.png"
    t["speaker_names"] = ", ".join([s["name"] for s in sub["speakers"]])
    for speaker in sub["speakers"]:
        t["speakers"] += speaker_to_markdown(speaker)
    return t


def speaker_to_markdown(speaker):
    s = {"name": speaker["name"]}
    s["biography"] = speaker["biography"] if speaker["biography"] is not None else ""
    tmpl = Template("""
### $name

$biography
""")
    return tmpl.substitute(s)


def talk_to_lektor(talk):
    tmpl = Template("""title: $title
---
created: $created
---
code: $code
---
speaker_names: $speaker_names
---
speakers:

$speakers
---
abstract:

$abstract
---
full_description:

$full_description
---
room: $room
---
day: $day
---
start_time: $start_time
---
duration_minutes: $duration_minutes
---
track: $track
---
python_skill: $python_skill
---
domain_expertise: $domain_expertise
---
social_card_image: $social_card_image

""")

    return tmpl.substitute(talk)


def talk_to_lektor_file(talk):
    content = talk_to_lektor(talk)
    new_dir = f"content/talks/{talk['code']}"
    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)

    with open(new_dir + "/contents.lr", "w") as f:
        f.write(content)


def remove_old_talks():
    """
    Removes old talks before regenerating them to avoid having previously on
    Pretalx removed talks still hanging around on the website. Crude but simple
    """
    talk_dirs = [f.path for f in os.scandir("content/talks") if f.is_dir()]
    for talk_dir in talk_dirs:
        shutil.rmtree(talk_dir)


def configure_pretalx_client():
    pretalx_api_key = os.environ.get("PRETALX_API_KEY")

    class PretalxBasicModel(BaseModel):
        api_token: str | None = None

    class PytanisBasicConfigModel(BaseModel):
        Pretalx: PretalxBasicModel

    cfg = PytanisBasicConfigModel.model_validate(
        {"Pretalx": {"api_token": pretalx_api_key}}
    )
    return PretalxClient(config=cfg)


def main():
    event_name = os.environ.get("PRETALX_EVENT_NAME")
    api_key = os.environ.get("PRETALX_API_KEY")
    assert event_name is not None and api_key is not None

    submissions = fetch_submissions(api_key, event_name)
    talks = [submission_to_talk(sub) for sub in submissions]

    remove_old_talks()
    for talk in talks:
        talk_to_lektor_file(talk)
        generate_social_card(talk)


if __name__ == "__main__":
    main()
