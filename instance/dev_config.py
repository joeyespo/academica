"""\
Development Config

This will be used when running Flask's local development server with app.run().
You can use this implicitly with app.run or by setting SETTINGS_MODULE to this.

See 'default_config.py' for a complete list of overridable settings.
"""


# Development settings
DEBUG = True
HOST = 'localhost'
PORT = 80

# Security settings
SECRET_KEY = 'development key'
