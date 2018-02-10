from include.WebServer import WebServer


def example():
    return 'example'


WebServer.addRoute('/example', example)
