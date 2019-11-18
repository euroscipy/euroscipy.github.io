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
TEMPLATE_PAGES = {
    os.path.join(os.getcwd(), "content/pages/2020/index.html"): '2020/index.html'
}
DIRECT_TEMPLATES = []
TEMPLATE_EXTENSIONS = ['.html']
THEME = os.path.join(os.getcwd(), "theme", "beevibrant")

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 5

STATIC_PATHS = ['content/static']
ASSET_URL = 'theme'

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'assets',
    # 'sitemap',
    'jinja2content'
]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
