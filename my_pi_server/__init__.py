"""
The server application to run the demo
"""
# ---------------------IMPORTS-------------------------------
import sys
import os
import time
from threading import Thread
from flask import Flask, render_template
import logging
from logging.handlers import RotatingFileHandler
# from flask_socketio import SocketIO
import socketio
import eventlet
# from eventlet import wsgi
# import fnmatch

# ---------------------module variables------------------------
# socketio server
# sioServer = socketio.Server(logger=True, ASYNC_MODE='eventlet')
sioServer = socketio.Server()
# application server
app = Flask(__name__, static_folder='../static', static_url_path='', template_folder='../templates')

# config parameters
config = {
    'port': 80,
    'SECRET_KEY': 'secret!'
}
thread = None
threadCount = 0
# ---------------------module functions-------------------------

def setup():
    """Setup the server to run based on config variable"""
    global app, sioServer, config, thread, threadCount
    app.config['SECRET_KEY'] = config['SECRET_KEY']
    # IMPORTANT setup includes and all routes before setting up socketio/eventlet
    setupErrorHandling()
    setupIncludes()
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sioServer, app)
    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(
        eventlet.listen(('', config['port'])),
        app
        )
    return

def setupErrorHandling():
    """
    Basic error handling of web server
    http://flask.pocoo.org/docs/0.12/errorhandling/
    https://gist.github.com/ibeex/3257877
    """
    global app
    handler = RotatingFileHandler('app.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)


def setupIncludes():
    """Setup includes such as routes"""
    # import the rest of the files
    importDirectory("routes")
    # importDirectory('socketio_routes')
    return


def importDirectory(directory):
    """Iterate through directory and import all files."""
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    basePath = path + '/' + directory
    # print (baseDir, path, '/', basePath, os.path.abspath(__file__))
    for name in os.listdir(basePath):
        if name.endswith(".py"):
            # strip the extension
            module = name[:-3]
            # set the module name in the current global name space:
            fullPackageName = os.path.join(directory, module).replace('/', '.')
            if fullPackageName not in sys.modules:
                print "Module: {} Importing: {}".format(module, fullPackageName)
                globals()[module] = __import__(fullPackageName)
    return

def backgroundThread():
    """Example of how to send server generated events to clients."""
    global sioServer, threadCount
    threadCount = 0
    while True:
        time.sleep(1)
        count += 1
        sioServer.emit('my response', {'data': 'Server generated event'}, namespace='/test')
        break

def prepareThreads():
    """Example of how to prepare threads so that users communication works"""
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return


def render(fileToRender):
    """Render flask html file"""
    print "RENDERING: ", fileToRender
    return render_template(fileToRender)
