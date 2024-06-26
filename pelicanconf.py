AUTHOR = 'Jesus Flores'
SITENAME = 'Humberto de Jesus Flores'
SITEURL = "https://hjesusflores.org"

PATH = "content"

TIMEZONE = 'America/Mexico_City'

RELATIVE_URLS = True

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 3

THEME = 'pelican-hyde'
PROFILE_IMAGE = 'avatar.png'
COLOR_THEME = '0c'
SOCIAL = [
    ('github', 'https://github.com/stokekld'),
    ('email', 'mailto:hdjesus.flores@gmail.com'),
    ('twitter', 'https://twitter.com/stokekld')
]
DISPLAY_PAGES_ON_MENU = True
MENUITEMS = [
    ('About Me', 'https://hjesusflores.org/about-me.html')
]
BIO = "Sysadmin / Developer"