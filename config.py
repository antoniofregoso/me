import os
import configparser
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    path_current_directory = os.path.dirname(__file__)
    config = configparser.ConfigParser() 
    path_config_file = os.path.join(path_current_directory, 'me.ini')
    config.read(path_config_file)
    OPTIONS = config['options']
    ODOO = config['odoo']
    csrf = OPTIONS['csrf_secret'] 
    SECRET_KEY = os.environ.get('SECRET_KEY') or csrf 