import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap

import config

app = Flask(__name__)
config_name = os.environ.get('FLASK_CONFIG', 'dev')
app.config.from_object(getattr(config, config_name.title() + 'Config'))

Bootstrap(app)


@app.route('/')
def index():
    """Serve client-side application."""
    return render_template('index.html',
                           use_socketio=not app.config['NO_SOCKETIO'])


if __name__ == '__main__':
    app.run()  # pragma: no cover
