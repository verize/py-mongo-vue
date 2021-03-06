import os

from .config_dev import config_dev
from .config_prod import config_prod



def get_app_config():
    if os.environ['FLASK_ENV'] == 'production':
        return config_prod
    if os.environ['FLASK_ENV'] == 'development':
        # Load Development environment
        return config_dev
