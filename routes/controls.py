import include.WebServer as WebServer


def controls():
    return WebServer.render('controls.html')


WebServer.addRoute('/controls', controls)
