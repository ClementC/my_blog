#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Clément Chastagnol'
SITENAME = 'Clément Chastagnol'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/clément-chastagnol-26b75611'),
          ('github', 'https://github.com/ClementC'),
          ('twitter', 'https://twitter.com/HerrDoktorFunk'),
         )

SIDEBAR_DIGEST = 'Computer Scientist and Musician'

SUMMARY_MAX_LENGTH = 150
DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# To use Jupyter notebooks
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

IGNORE_FILES = ['.ipynb_checkpoints']

IPYNB_USE_META_SUMMARY = True

STATIC_PATHS = ["figures", "images"]
USE_FOLDER_AS_CATEGORY = False

PAGE_DIRS = ['pages']
ARTICLE_DIRS = ['articles']

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

#ABOUT_PAGE = '/pages/about.html'
#TWITTER_USERNAME = 'herrdoktorfunk'
GITHUB_USERNAME = 'ClementC'
SHOW_ARCHIVES = True
SHOW_FEED = False  # Need to address large feeds

MENUITEMS = [("About", "/pages/about.html"), ("Posts", "/category/posts.html"), ("Archive", "/archives.html")]

THEME = '../pelican-blue'
DISPLAY_CATEGORIES_ON_MENU = False
