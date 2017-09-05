"""
The server application to run the demo
"""
# ---------------------IMPORTS-------------------------------
import sys
import os
import time
from threading import Thread
from flask import Flask, render_template
# from flask_socketio import SocketIO
import socketio
import eventlet
import eventlet.wsgi
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
# ---------------------module functions-------------------------
"""Setup the server to run based on config variable"""
sioServer = socketio.Server(logger=True, ASYNC_MODE='eventlet')
app = Flask(__name__, static_folder='static', static_url_path='')
@app.route('/')
def index():
    """Serve the client-side application."""
    return render_template('index.html')
# wrap Flask application with engineio's middleware
app = socketio.Middleware(sioServer, app)
eventlet.wsgi.server(eventlet.listen(('', 80)), app)
