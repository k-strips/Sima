import secrets

# Secret key for signing cookies
SECRET_KEY = secrets.token_hex(15)

# Use a secure, unique and absolutely secret key for
# signing the data.
CSRF_SESSION_KEY = secrets.token_hex(15)

#rounds to has with bcrypt
BCRYPT_LOG = 12
