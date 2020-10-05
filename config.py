# -*- coding: utf-8 -*-
import os
import configparser
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    config = configparser.ConfigParser() 
    path_config_file = os.path.join(basedir , 'me.ini')
    config.read(path_config_file)
    OPTIONS = config['options']
    ODOO = config['odoo']
    CRM = config['crm']
    csrf = OPTIONS['csrf_secret'] 
    SECRET_KEY = os.environ.get('SECRET_KEY') or csrf 