# see http://flask.pocoo.org/docs/0.12/patterns/appdispatch/
# from flask import Flask, render_template
import flask
import socketio
import eventlet
import os
# import urllib
# ========== MY MODULES =============
import config
# import utils.files as files


class WebServer(object):
    # ============ public variables ============
    # asyncMode = 'eventlet'  # 'threading', 'eventlet', or 'gevent'
    app = None
    port = 8080
    flask = None  # web server inst
    sio = None
    secret = 'secret!'
    templateFolder = config.ROOT_DIR + 'templates/'
    # routesDir = config.ROOT_DIR + 'routes/'
    # ============ private variables ============

    @classmethod
    def setupEnvironment(cls):
        # eventlet.monkey_patch()  # asyncMode eventlet setup
        cls.__setupFlask()
        cls.__setupSocketIO()
        cls.__setupApp()

    @classmethod
    def __setupFlask(cls):
        cls.flask = flask.Flask(
            __name__,
            # template_folder=cls.templateFolder,
            root_path=config.ROOT_DIR,
            static_folder='public',
            static_url_path='/public'
        )
        # set the secret
        # WTF is this again?!
        cls.flask.config['SECRET_KEY'] = cls.secret

    @classmethod
    def __setupSocketIO(cls):
        cls.sio = socketio.Server()

    @classmethod
    def __setupApp(cls):
        cls.app = socketio.Middleware(cls.sio, cls.flask)

    @classmethod
    def run(cls):
        eventlet.wsgi.server(
            eventlet.listen(('', cls.port)),
            cls.app
        )

    @classmethod
    def shutdown(cls):
        """ see https://stackoverflow.com/a/17053522 """
        print 'shutting down'
        shutdown = flask.request.environ.get('werkzeug.server.shutdown')
        if shutdown is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        shutdown()

    @classmethod
    def addRoutes(cls):
        # import all in the routes/ dir
        __import__('routes')

    @classmethod
    def addRoute(cls, path, callback):
        if type(path) is not str:
            raise TypeError('path must be str')
        elif not callable(callback):
            raise ValueError('callback must be callable')
        cls.flask.add_url_rule(path, callback.__name__, callback)

    @classmethod
    def getRoutes(cls):
        routes = []
        for rule in WebServer.flask.url_map.iter_rules():
            if rule.endpoint == 'static':
                continue
            options = {}
            for arg in rule.arguments:
                options[arg] = "[{0}]".format(arg)
            # methods = ','.join(rule.methods)
            url = flask.url_for(rule.endpoint, **options)
            # line = urllib.unquote("{:50s} {:20s} {}".format(
            #     rule.endpoint,
            #     methods,
            #     url
            # ))
            routes.append(url)
        return routes

    @classmethod
    def render(cls, templatePath):
        """
        Use jinja to render an html page
        """
        return flask.render_template(templatePath)


"""
def list_routes():
    output = []
    for rule in WebServer.flask.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)
        methods = ','.join(rule.methods)
        url = flask.url_for(rule.endpoint, **options)
        # url = rule.endpoint
        line = urllib.unquote("{:50s} {:20s} {}".format(
            rule.endpoint,
            methods,
            url
        ))
        output.append(line)

    for line in sorted(output):
        print line
"""
