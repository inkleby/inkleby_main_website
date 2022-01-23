#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
from ssl import ALERT_DESCRIPTION_PROTOCOL_VERSION
import sys
sys.path.append(os.curdir)

AUTHOR = u'Alex Parsons'
SITENAME = u'inkleby.com'
SITEURL = 'http://www.inkleby.com'

#from plugins import neighbors

#PLUGINS = [neighbors]

PATH = 'content'

THEME = "theme"
TIMEZONE = 'Europe/London'
STATIC_PATHS = ['uploads','extra']
DEFAULT_LANG = u'en'

ASSET_SOURCE_PATHS = ["static/css"]

# Feed generation is usually not desired when developing
RELATIVE_URLS = True
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

#ARTICLE_PATHS = ["posts"]
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS  = "blog/{date:%Y}/{date:%m}/{slug}/index.html"
PAGE_URL  = "{slug}/"
PAGE_SAVE_AS   = "{slug}/index.html"


TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_URL = 'authors/'
AUTHORS_SAVE_AS = 'authors/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORYS_URL = 'categories/'
CATEGORYS_SAVE_AS = 'categories/index.html'


INDEX_SAVE_AS = "blog/index.html"
FRONT_SAVE_AS = "index.html"
STRINGPRINT_SAVE_AS = "stringprint/index.html"

EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DIRECT_TEMPLATES = ('stringprint','front','index')

PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)


DEFAULT_PAGINATION = 6
DEFAULT_ORPHANS = 2

GOOGLE_ANALYTICS = ""

SECTIONS = (
    ('StringPrint', 'fa-newspaper-o' ,'/stringprint'),
    ('Projects', 'fa-cog' ,'/projects'),
    ('Blog', 'fa-newspaper-o' ,'/blog'),
    ('About', 'fa-newspaper-o' ,'/about'),
)

PORTFOLIO= [
    ('Letting Fees UK', 'Crowdsourcing Websites' ,'lettingfees.png',"http://lettingfees.inkleby.com"),
    ('StringPrint', 'Better Longform Publishing' ,'stringprint.png',"http://www.stringprint.com"),
    ('We Name The Stars', 'Dataset Exploration' ,'pluto_t.png',"http://wenamethestars.inkleby.com"),
    ('Robots', 'Drip Distribution' ,'robots_t.png',"/robots/"),
    ('Postal Vote', 'User Assistance' ,'postalvote.png',"http://postalvote.inkleby.com"),
    ('Crisis Alert', 'Text Analysis' ,'crisis_t.png',"http://crisisalert.inkleby.com"),
]


ROW_PORTFOLIO = [[(y, PORTFOLIO[y + x*3]) for y in range(0,3)] for x in range(0,2)]


HAS_IMAGE= ["Robots"]


