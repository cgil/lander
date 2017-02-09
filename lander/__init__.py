import os

from flask import (
    Flask,
    render_template,
    request,
    send_from_directory,
)

os.environ['CONFIG_ENV'] = './config/%s.yaml' % os.environ['ENV_NAME']
from utils.configuration import config


def create_app():
    """Create and initialize the application."""
    app = Flask(__name__, static_folder='static')
    app.config['DEBUG'] = config.get('debug')

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(
            os.path.join(app.root_path, 'static'),
            'favicon.ico',
            mimetype='image/vnd.microsoft.icon'
        )

    @app.route('/')
    def home():
        return render_template('home.html', is_production=not config.get('debug'))

    return app
