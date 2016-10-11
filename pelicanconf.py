#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ryan'
SITENAME = 'cerris'
SITEURL = 'http://localhost:8000'
TAGLINE = "cloudy and tree-like thoughts"

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PATH = 'content'

TIMEZONE = 'America/Denver'
DATE_FORMAT = '%Y-%m-%d'

DEFAULT_LANG = u'en'
DEFAULT_METADATA = {'status':'draft'}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

MENUITEMS = [
    ('About', '/pages/about.html'),
    ('Portfolio', '#'),
    ('Tags', '/tags.html'),
    ('Contact', '#'),
]

SOCIAL = [
    '<script type="text/javascript" src="//www.redditstatic.com/button/button1.js"></script>',
    """
    <a href="https://twitter.com/share" class="twitter-share-button" data-via="funtime_bobby">Tweet</a>
    <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>
    """
]

DEFAULT_PAGINATION = False

RELATIVE_URLS = True
THEME = 'theme'
