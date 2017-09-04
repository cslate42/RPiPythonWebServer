#!/usr/bin/python2.7
"""
The server application to run the demo
"""
# ---------------------IMPORTS-------------------------------
import sys
import os
from flask import Flask  # , render_template
# from flask_socketio import SocketIO
import socketio
import eventlet
# from eventlet import wsgi
# import fnmatch

# ---------------------module variables------------------------
# application server
app = None
# socketio server
sioServer = None
# config parameters
config = {
    'port': 80
}

# ---------------------module functions-------------------------

def setup():
    """Setup the server to run based on config variable"""
    # sioServer = socketio.Server(logger=True, ASYNC_MODE=ASYNC_MODE)
    app = Flask(__name__, static_folder='static', static_url_path='')
    # app.wsgi_app = socketio.Middleware(myGlobals.sio, myGlobals.app.wsgi_app)
    app.config['SECRET_KEY'] = 'secret!'
    # sioServer = socketio(logger=True, ASYNC_MODE=ASYNC_MODE)
    sioServer = socketio.Server()
    # sioServer.run(myGlobals.app, host="0.0.0.0", port=80)
    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(sioServer, app)
    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', config['port'])), app)
    # asyncMode()
    importDirectory('routes')
    importDirectory('my_socketio')
    return


def importDirectory(directory):
    """Iterate through directory and import all files."""
    path = os.path.dirname(os.path.abspath(__file__))
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
