import include.WebServer as WebServer


@WebServer.addRoute('/latency')
def latency():
    return WebServer.render('latency.html')


@WebServer.sioHandler('ping')
def ping(sid, data=None):
    WebServer.sioEmit('pong', '', sid)
