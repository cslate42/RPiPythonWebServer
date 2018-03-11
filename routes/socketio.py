import include.WebServer as WebServer


@WebServer.addRoute('/sio')
def socketio():
    return WebServer.render('sio-test.html')
