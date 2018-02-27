import include.WebServer as WebServer


def example():
    return 'example'


WebServer.addRoute('/example', example)
