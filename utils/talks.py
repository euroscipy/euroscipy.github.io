import json
import os
from collections import defaultdict
from string import Template

from pydantic import BaseModel
from pytanis import PretalxClient


def load_submissions():
    with open("databags/submissions.json") as file:
        return json.load(file)["results"]


def load_speakers():
    with open("databags/speakers.json") as file:
        return json.load(file)


def submission_to_talk(sub):
    t = defaultdict(lambda: "")
    t["title"] = sub["title"]
    t["code"] = sub["code"]
    t["abstract"] = sub["abstract"]
    t["full_description"] = sub["description"]
    return t


def merge_speakers_and_submissions(submissions, speakers):
    talks = [submission_to_talk(s) for s in submissions]
    return talks


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
    pass


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
    submissions = load_submissions()
    speakers = load_speakers()
    talks = merge_speakers_and_submissions(submissions, speakers)
    print(talks)
    for talk in talks:
        talk_to_lektor_file(talk)


if __name__ == "__main__":
    main()
