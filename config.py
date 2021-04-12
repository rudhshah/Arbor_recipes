"""ArborRecipe development configuration."""
import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b']?N\xc2\xb7~(\x8b\x17\x0c7 j\xb2\\\x0f,$\xf8\xab\xd8ug+'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
ARBORRECIPE_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = ARBORRECIPE_ROOT / 'var' / 'uploads'
IMAGES_FOLDER = ARBORRECIPE_ROOT / 'ArborRecipe' / 'static' / 'images'
CSS_FOLDER = ARBORRECIPE_ROOT / 'ArborRecipe' / 'static' / 'css'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = ARBORRECIPE_ROOT / 'var' / 'ArborRecipe.sqlite3'
