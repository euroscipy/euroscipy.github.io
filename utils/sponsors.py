import json
from pathlib import Path
from string import Template


def dict_to_lektor(sponsor):
    tmpl = Template("""name: $name
---
id: $id
---
type: $type
---
name: $name
---
full_description: $full_description
---
logo: $logo
---
url: $url
""")
    return tmpl.substitute(sponsor)


def json_to_dict(sponsor, _type):
    s = {}
    s["type"] = _type.replace("Sponsors", "Sponsor")
    s["type"] = s["type"].replace("Partners", "Partner")
    s["id"] = sponsor.get("id")
    s["name"] = sponsor.get("name")
    s["logo"] = sponsor.get("logo")
    s["url"] = sponsor.get("url") or ""
    s["full_description"] = sponsor.get("full_description")
    return s


def load_sponsors():
    sponsor_types = []
    sponsors = []
    with (Path(__file__).parents[1] / "databags/sponsors.json").open() as f:
        j = json.load(f)
        sponsor_types = j["types"]
    for type in sponsor_types:
        sponsors += [
            json_to_dict(s, type["name"]) for s in type["sponsors"]
        ]

    return sponsors


def save_as_lektor(sponsor):
    new_dir = Path(__file__).parents[1] / f"content/sponsors/{sponsor['id']}"
    new_dir.mkdir(parents=True, exist_ok=True)

    lektor = dict_to_lektor(sponsor)
    with (new_dir / "contents.lr").open("w") as f:
        f.write(lektor)


def main():
    sponsors = load_sponsors()
    for sponsor in sponsors:
        save_as_lektor(sponsor)


if __name__ == "__main__":
    main()
