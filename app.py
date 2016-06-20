# set this to 'threading', 'eventlet', or 'gevent'
async_mode = 'threading'

if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey
    monkey.patch_all()

from flask import Flask, render_template
# from flask_socketio import SocketIO
import socketio
import eventlet

import fnmatch
import os

import myGlobals
import myThreading

port = 80
# myGlobals.sio = socketio.Server(logger=True, async_mode=async_mode)
myGlobals.app = Flask(__name__, static_folder='static', static_url_path='')
# myGlobals.app.wsgi_app = socketio.Middleware(myGlobals.sio, myGlobals.app.wsgi_app)
myGlobals.app.config['SECRET_KEY'] = 'secret!'
# myGlobals.sio = socketio(logger=True, async_mode=async_mode)
myGlobals.sio = socketio.Server()

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


# -----------------------__RUN__--------------------------

if __name__ == "__main__":
    # myGlobals.sio.run(myGlobals.app, host="0.0.0.0", port=80)


    # wrap Flask application with engineio's middleware
    app = socketio.Middleware(myGlobals.sio, myGlobals.app)

    # deploy as an eventlet WSGI server
    eventlet.wsgi.server(eventlet.listen(('', 80)), app)

    # if async_mode == 'threading':
    #     # deploy with Werkzeug
    #     myGlobals.app.run(threaded=True)
    # elif async_mode == 'eventlet':
    #     # deploy with eventlet
    #     import eventlet
    #     eventlet.wsgi.server(eventlet.listen(('', app.port)), myGlobals.app)
    # elif async_mode == 'gevent':
    #     # deploy with gevent
    #     from gevent import pywsgi
    #     try:
    #         from geventwebsocket.handler import WebSocketHandler
    #         websocket = True
    #     except ImportError:
    #         websocket = False
    #     if websocket:
    #         pywsgi.WSGIServer(('', port), myGlobals.app, handler_class=WebSocketHandler).serve_forever()
    #     else:
    #         pywsgi.WSGIServer(('', port), myGlobals.app).serve_forever()
    # else:
    #     print('Unknown async_mode: ' + async_mode)
