"""\
Development Config

This will be used when running Flask's local development server with app.run().
You can use this implicitly with app.run or by setting SETTINGS_MODULE to this.

See 'default_config.py' for a complete list of overridable settings.
"""

import os
import imp
from flask.ext.pymongo import PyMongo, BSONObjectIdConverter


# Development settings
DEBUG = True
HOST = 'localhost'
PORT = 80

# Security settings
SECRET_KEY = 'development key'


# Override MongoDB driver
class FakePyMongo(PyMongo):
    def init_app(self, app, config_prefix='MONGO'):
        """Overrides PyMongo with mongofake."""
        if 'pymongo' not in app.extensions:
            app.extensions['pymongo'] = {}

        if config_prefix in app.extensions['pymongo']:
            raise Exception('duplicate config_prefix "%s"' % config_prefix)

        self.config_prefix = config_prefix
        
        def key(suffix):
            return '%s_%s' % (config_prefix, suffix)

        username = app.config.get(key('USERNAME'))
        password = app.config.get(key('PASSWORD'))
        auth = (username, password)

        if any(auth) and not all(auth):
            raise Exception('Must set both USERNAME and PASSWORD or neither')

        dbname = app.config.get(key('DBNAME'))
        cx = imp.load_source('mongofake', os.path.join(os.path.dirname(__file__), 'mongofake.py')).FakeMongoConnection()
        db = cx[dbname]

        if any(auth):
            db.authenticate(username, password)

        app.extensions['pymongo'][config_prefix] = (cx, db)
        app.url_map.converters['ObjectId'] = BSONObjectIdConverter


MONGO_OBJECT = FakePyMongo
#MONGO_SEEDS = {
#}
