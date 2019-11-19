#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os

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

SUBMENU = {}

DELETE_OUTPUT_DIRECTORY = True
DIRECT_TEMPLATES = []
THEME = os.path.join(os.getcwd(), "theme", "beevibrant")

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 5

PATH = 'content'
STATIC_URL = '../static'
STATIC_PATHS = ['static']
ASSET_URL = 'theme'

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'assets',
    # 'sitemap',
]
TYPOGRIFY = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

TWITTER_FOLLOW_URL = 'https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fwww.euroscipy.org%2F2019%2F&ref_src=twsrc%5Etfw&region=follow_link&screen_name=euroscipy&tw_p=followbutton'
TELEGRAM_URL = 'https://t.me/euroscipy'
