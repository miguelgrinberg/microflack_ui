import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
env = os.path.join(basedir, '.env')
if os.path.exists(env):
    load_dotenv(env)
else:
    print('Warning: .env file not found')


class Config(object):
    DEBUG = False
    TESTING = False
    NO_SOCKETIO = True if os.environ.get('NO_SOCKETIO') else False


class DevConfig(Config):
    DEBUG = True


class TestConfig(Config):
    TESTING = True


class ProdConfig(Config):
    pass
