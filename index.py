# encoding: utf8
from serverlessplus import create_environ, create_app, get_response, wrap_response

APP = 'app:app'
app = create_app(APP)

def main_handler(event, context):
    environ = create_environ(event, context)
    response = get_response(app, environ)
    return wrap_response(response, {})
