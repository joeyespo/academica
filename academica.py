"""\
Academica

The academic site.
"""

from flask import Flask, render_template

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
    return render_template('index.html')


@app.route('/view')
def view():
    return render_template('view.html')


@app.route('/<username>')
def profile(username):
    return render_template('profile.html', username=username)


# Run development server with the development settings
if __name__ == '__main__':
    app.run(app.config['HOST'], app.config['PORT'], app.debug != False)
