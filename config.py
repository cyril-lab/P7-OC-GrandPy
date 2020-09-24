import os

#Key for the Google Map API
KEY_API_GOOGLE = os.environ.get("KEY_API_GOOGLE")

if not KEY_API_GOOGLE:
    raise ValueError("No KEY_API_GOOGLE set for Flask application")