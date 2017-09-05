

from flask import Flask
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
    'port': 80,
    'SECRET_KEY': 'secret!'
}
thread = None
threadCount = 0
# sioServer = socketio.Server(logger=True, ASYNC_MODE=ASYNC_MODE)
server = Flask(__name__, static_folder='static', static_url_path='')
# app.wsgi_app = socketio.Middleware(myGlobals.sio, myGlobals.app.wsgi_app)
server.config['SECRET_KEY'] = config['SECRET_KEY']
# sioServer = socketio(logger=True, ASYNC_MODE=ASYNC_MODE)
sioServer = socketio.Server()
# sioServer.run(myGlobals.app, host="0.0.0.0", port=80)
# wrap Flask application with engineio's middleware
app = socketio.Middleware(sioServer, server)
# deploy as an eventlet WSGI server
eventlet.wsgi.server(eventlet.listen(('', config['port'])), app)
# asyncMode()

@server.route('/')
def test():
    print "HERE"
    return "HERE"
