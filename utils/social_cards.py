import textwrap

from PIL import Image, ImageDraw, ImageFont

BOLD_FONT = ImageFont.truetype("assets/static/fonts/IBMPlexSans-SemiBold.ttf", 34)
REGULAR_FONT = ImageFont.truetype("assets/static/fonts/IBMPlexSans-Regular.ttf", 34)
CODE_FONT = ImageFont.truetype("assets/static/fonts/IBMPlexSans-Regular.ttf", 14)


def generate_social_card(talk):
    template = Image.open("assets/static/sc-template.png")
    dst = f"assets/static/talks/{talk['code']}.png"
    d = ImageDraw.Draw(template)

    headlines = "\n".join(textwrap.wrap(talk["title"], 60))
    d.multiline_text((40, 470), headlines, font=BOLD_FONT)
    d.text((40, 550), talk["speaker_names"], font=REGULAR_FONT)
    d.text((40, 595), talk["code"], font=CODE_FONT)
    template.save(dst)
