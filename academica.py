"""\
Academica

The academic site.
"""

from flask import Flask, render_template, abort
import seeds

__version__ = '0.1'


# Flask application
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('default_config')
# Configuration, using development when run locally, overridden by ENV
if __name__ == '__main__':
    app.config.from_pyfile('dev_config.py', silent=True)
app.config.from_envvar('SETTINGS_MODULE', silent=True)


#Views
@app.route('/')
def index():
    # TODO: signup, etc
    return render_template('index.html')


@app.route('/university/<username>')
def university(username):
    item = seeds.find(lambda x: x['username'] == username, seeds.universities)
    if not item:
        abort(404)
    return render_template('university.html', university=item)


@app.route('/<username>')
def profile(username):
    user = seeds.find(lambda x: x['username'] == username, seeds.users)
    if not user:
        abort(404)
    return render_template('profile.html', user=user)


# Run development server with the development settings
if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'], app.debug != False)
