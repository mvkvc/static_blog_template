import datetime

THEME = 'themes/minimal-xy'

# Theme customizations
MINIMALXY_CUSTOM_CSS = 'content/custom.css'
# MINIMALXY_FAVICON = 'favicon.ico'
MINIMALXY_START_YEAR = 2023
MINIMALXY_CURRENT_YEAR = datetime.date.today().year

# Author
AUTHOR_INTRO = u'Hello world! I’m John Doe.'
AUTHOR_DESCRIPTION = u'Hello world! I’m John Doe. I like coffee, birds and Python.'
# AUTHOR_AVATAR = 'http://www.gravatar.com/avatar/abcdefghijkl?s=240'
AUTHOR_WEB = 'http://mypersonalsite.com'

# Services
# GOOGLE_ANALYTICS = 'UA-12345678-9'
# DISQUS_SITENAME = 'johndoe'

# Social
SOCIAL = (
    # ('facebook', 'http://www.facebook.com/johndoe'),
    ('twitter', 'http://twitter.com/johndoe'),
    ('github', 'https://github.com/johndoe'),
    # ('linkedin', 'http://www.linkedin.com/in/johndoe'),
)

# Menu
MENUITEMS = (
    ('Home', '/' + 'index.html'),
    ('Categories', '/' + 'categories.html'),
    ('Archive', '/' + 'archives.html')
    )

#     MENUITEMS = (('About', 'about-me/'),
#                         ('Reading', 'reading/'),
#                 ('Archive','archives.html'),)
# )

# Search plugin
# SEARCH_MODE = "source"
# SEARCH_HTML_SELECTOR = "main"

DISPLAY_CATEGORIES_ON_MENU = False

# Base settings
AUTHOR = 'John Doe'
SITENAME = 'Static Blog Template'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Not sure if used in minimal-xy theme
DEFAULT_PAGINATION = 10

# Not used in minimal-xy theme
# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

REVERSE_ARCHIVE_ORDER = True
