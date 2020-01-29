#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = os.environ.get('SITEURL', 'www.euroscipy.org')
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

TWITTER_USERNAME = "scipyconf"
DISQUS_SITENAME = "scipyconferences"
#GOOGLE_ANALYTICS = ""
