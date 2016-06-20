# set this to 'threading', 'eventlet', or 'gevent'
async_mode = 'threading'

if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey
    monkey.patch_all()

from flask import Flask, render_template

import socketio
import fnmatch
import os

import myGlobals
import myThreading

myGlobals.sio = socketio.Server(logger=True, async_mode=async_mode)
myGlobals.app = Flask(__name__, static_folder='static', static_url_path='')
myGlobals.app.wsgi_app = socketio.Middleware(myGlobals.sio, myGlobals.app.wsgi_app)
myGlobals.app.config['SECRET_KEY'] = 'secret!'

def importDirectory(baseDir, importName):
    """
    iterate through directory and import all files
    """
    path = os.path.dirname(__file__)
    basePath = path + '/' + baseDir
    # print(basePath, os.listdir(path + '/' + baseDir), baseDir)
    for name in os.listdir(basePath):
        if name.endswith(".py"):
            #strip the extension
            module = name[:-3]
            # set the module name in the current global name space:
            #  print("Importing:", os.path.join(basePath, module))
            globals()[module] = __import__(os.path.join(baseDir, module).replace('/', '.') )
    return

_tmp_routes = None
importDirectory('routes', _tmp_routes)
_tmp_sio = None
importDirectory('my_socketio', _tmp_sio)
