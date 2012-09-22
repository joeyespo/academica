"""\
Development Config

This will be used when running Flask's local development server with app.run().
You can use this implicitly with app.run or by setting SETTINGS_MODULE to this.

See 'default_config.py' for a complete list of overridable settings.
"""

import os


# Development settings
DEBUG = False
HOST = '0.0.0.0'
PORT = int(os.environ.get('PORT', 5000))

# Security settings
SECRET_KEY = 'development key'
