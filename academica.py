"""\
Academica

The academic site.
"""

from flask import Flask, render_template, abort
from flask.ext.pymongo import PyMongo
import seeds

__version__ = '0.1'


# Flask application
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('default_config')
# Configuration, using development when run locally, overridden by ENV
if __name__ == '__main__':
    app.config.from_pyfile('dev_config.py', silent=True)
app.config.from_envvar('SETTINGS_MODULE', silent=True)

# Setup database
driver = app.config['MONGO_OBJECT'] if app.config.get('MONGO_OBJECT') else PyMongo
mongo = driver(app)


#Views
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/view')
def view():
    return render_template('view.html')


@app.route('/university/<name>')
def university(name):
    item = seeds.find(lambda x: x['username'] == name, seeds.universities)
    return render_template('university.html', university=item)


@app.route('/<username>')
def profile(username):
    #user = seeds.find(lambda x: x['username'] == username, seeds.users)
    user = mongo.db.users.find_one({'username': username})
    if not user:
        abort(404)
    return render_template('profile.html', user=user)


# Run development server with the development settings
if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'], app.debug != False)
