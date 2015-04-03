# -*- coding: utf-8 -*-

import sys
import os
from bottle import error, get, static_file, view, default_app, run

# Use UTF8
reload(sys)
sys.setdefaultencoding('utf8')

# setup initial config file from example
if not os.path.exists('config.py'):
    from shutil import copyfile
    copyfile('config.py.example', 'config.py')
from config import CONFIG

@error(404)
def error404(error):
    """Display the error 404 page"""
    return server_static('error/404.html')

@get('/')
@view('index')
def index():
    """Display the homepage"""
    return {
        'config': CONFIG,
        'body_title': CONFIG['title'],
        'head_title': CONFIG['author'] + ': ¡Hola!',
        'head_author': CONFIG['author'],
        'head_keywords': 'beautiful bottle,python bottle,bottle python',
        'head_description': 'Beautiful Python/Bottle example web page.'
    }

@get('/<filepath:path>')
def server_static(filepath):
    """Display static files in the web root folder"""
    return static_file(filepath, root = CONFIG['webroot'])

application=default_app()

if __name__ in ('__main__'):

    if CONFIG['debug'] is True:
        print "DEBUG is enabled!"

    run(host='localhost', port=8080)
