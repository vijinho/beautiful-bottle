# -*- coding: utf-8 -*-

import os
from bottle import error, route, static_file, default_app, run

@error(404)
def error404(error):
    return server_static('error/404.html')

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='www')

@route('/')
def index():
    return static_file('index.html', root='www')

application=default_app()

if __name__ in ('__main__'):
    run(host='localhost', port=8080)
