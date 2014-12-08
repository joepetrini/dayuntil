import os

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

PERMANENT_SESSION_LIFETIME = 31536000
DEFAULT_TZ = 'America/Chicago'

# Database connection string
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'data.db')
#SQLALCHEMY_DATABASE_URI = 'mysql://user:pass@localhost/dbname'
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASE_DIR, 'migrations')
#DATABASE_CONNECT_OPTIONS = {}

# App threads, 2 per available cores
THREADS_PER_PAGE = 2

# Enable protection against *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Use a secure, unique and absolutely secret key for
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"

# Flask-Mail settings
MAIL_SERVER = 'your.mailserver.com'
MAIL_PORT = 25
#MAIL_USERNAME = None
#MAIL_PASSWORD = None

# administrator list
ADMINS = ['you@example.com']

ANALYTICS_ID = ''
FB_APP_ID = ''
FB_SECRET = ''

ADSENSE_TOP = """
                    FULL ADSENSE CODE HERE
              """

ADSENSE_MOB = """
                    FULL ADSENSE CODE HERE
              """

ADSENSE_BOTTOM = """
                    FULL ADSENSE CODE HERE
                 """