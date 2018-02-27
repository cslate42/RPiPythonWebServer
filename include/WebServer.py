# see http://flask.pocoo.org/docs/0.12/patterns/appdispatch/
# from flask import Flask, render_template
import flask
import socketio
import eventlet
# ========== MY MODULES =============
import config

__app = None
__port = 8080
__flask = None  # web server inst
__sio = None
__secret = 'secret!'
__templateFolder = config.ROOT_DIR + 'templates/'


def setup():
    """
    Initialize the module
    """
    __setupEnvironment()
    __setupRoutes()


def __setupEnvironment():
    """
    Setup the webserver environment
        Create the web server application
        handle socket communication
        create the app instance
    """
    __setupFlask()
    __setupSocketIO()
    __setupApp()


def __setupFlask():
    """
    Create the flask web server
    """
    global __flask
    __flask = flask.Flask(
        __name__,
        # template_folder=cls.templateFolder,
        root_path=config.ROOT_DIR,
        static_folder='public',
        static_url_path='/public'
    )
    # set the secret
    # WTF is this again?!
    __flask.config['SECRET_KEY'] = __secret


def __setupSocketIO():
    """
    Setup the socket io server for low latency communications
    """
    global __sio
    __sio = socketio.Server()


def __setupApp():
    """
    Setup the flask application handler
    """
    global __app
    __app = socketio.Middleware(__sio, __flask)


def __setupRoutes():
    """
    Setup the initial routes by scanning the routes directory
    """
    # import all in the routes/ dir
    __import__('routes')


def getSocketIO():
    """
    Get the socket io object
    Returns:
        socketio.Server: the instance
    """
    return __sio


def getApp():
    """
    Get the web app
    Returns:
        socketio.Middleware: the instance
    """
    return __app


def run():
    """
    Run the web server on the port
    """
    eventlet.wsgi.server(
        eventlet.listen(('', __port)),
        __app
    )


def shutdown():
    """
    Handle the shutdown function
    see https://stackoverflow.com/a/17053522
    """
    print 'shutting down'
    shutdown = flask.request.environ.get('werkzeug.server.shutdown')
    if shutdown is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    shutdown()


def addRoute(path, callback):
    """
    Dynamically add a route to the web server
    Args:
        path (str): the path to use for the template
        callback (def): the template handler
    """
    if type(path) is not str:
        raise TypeError('path must be str')
    elif not callable(callback):
        raise ValueError('callback must be callable')
    __flask.add_url_rule(path, callback.__name__, callback)


def getRoutes():
    """
    Get a list of all the routes
    Returns:
        list: of routes sorted alphabetically
    """
    routes = []
    for rule in __flask.url_map.iter_rules():
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
    return sorted(routes)


def render(templatePath, args):
    """
    https://stackoverflow.com/questions/9195455/how-to-document-a-method-with-parameters
    Use jinja to render an html page
    Args:
        templatePath (str): the path to the template
        args (dict): key value pairs which are used in the template
    """
    # from pprint import pprint
    # pprint(args)
    return flask.render_template(templatePath, **args)
