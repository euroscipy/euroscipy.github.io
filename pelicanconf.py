#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

import yaml


AUTHOR = u'The EuroSciPy team <info@euroscipy.org>'
SITENAME = u'EuroSciPy'
SITEURL = ''

TIMEZONE = 'Europe/Berlin'
DEFAULT_LANG = u'en'

# Set the article URL
ARTICLE_URL = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'news/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

# Title menu options
DISPLAY_PAGES_ON_MENU = False

DELETE_OUTPUT_DIRECTORY = True
DIRECT_TEMPLATES = []
THEME = os.path.join(os.getcwd(), "theme", "beevibrant")
EXTRA_TEMPLATES_PATH = os.path.join(THEME, "templates")
THEME_STATIC_DIR = 'theme_2020'
ASSET_URL = THEME_STATIC_DIR

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 5

PATH = 'content'
STATIC_URL = '../static'
STATIC_PATHS = ['static', 'extra']
ARTICLE_EXCLUDES = STATIC_PATHS
METADATA = os.path.join(PATH, 'metadata')
EXTRA_PATH_METADATA = {
    # 'extra/CNAME': {'path': 'CNAME'},
    'extra/index.html': {'path': 'index.html'},
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'assets',
   # 'md-metayaml',
    # 'sitemap',
]
TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TWITTER_FOLLOW_URL = 'https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fwww.euroscipy.org%2F2019%2F&ref_src=twsrc%5Etfw&region=follow_link&screen_name=euroscipy&tw_p=followbutton'
TELEGRAM_URL = 'https://t.me/euroscipy'
SPECTRUM_URL = 'https://spectrum.chat/euroscipy'

CURRENT_EDITION = '2022'

EVENT = {}
EVENT['euroscipy_2020'] = yaml.safe_load(open(os.path.join(METADATA, '2020', 'event.yml')))
EVENT['euroscipy_2022'] = yaml.safe_load(open(os.path.join(METADATA, '2022', 'event.yml')))

SUBMENU = {}
SUBMENU['euroscipy_2020'] = yaml.safe_load(open(os.path.join(METADATA, '2020', 'menu.yml')))
SUBMENU['euroscipy_2022'] = yaml.safe_load(open(os.path.join(METADATA, '2022', 'menu.yml')))

KEYNOTES = {}
KEYNOTES['euroscipy_2020'] = yaml.safe_load(open(os.path.join(METADATA, '2020', 'keynotes.yml'))) or []
KEYNOTES['euroscipy_2022'] = yaml.safe_load(open(os.path.join(METADATA, '2022', 'keynotes.yml'))) or []

SPONSORS = {}
SPONSORS['euroscipy_2020'] = yaml.safe_load(open(os.path.join(METADATA, '2020', 'sponsors.yml'))) or []
SPONSORS['euroscipy_2022'] = yaml.safe_load(open(os.path.join(METADATA, '2022', 'sponsors.yml'))) or []
