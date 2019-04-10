# encoding: utf8
import os
from serverlessplus import create_environ, create_app, get_response, wrap_response

# add current dir to `LD_LIBRARY_PATH` so that we can use a newer version of sqlite3
os.environ['LD_LIBRARY_PATH'] = os.path.dirname(os.path.realpath(__file__)) + ':' + os.environ['LD_LIBRARY_PATH']

APP = 'django_example.wsgi:application'
app = create_app(APP)

def main_handler(event, context):
    environ = create_environ(event, context)
    response = get_response(app, environ)
    return wrap_response(response, {})
