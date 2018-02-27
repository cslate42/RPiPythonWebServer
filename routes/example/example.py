import include.WebServer as WebServer


# @WebServer.addRoute('/example')
def example():
    """
    Two methods to define the custom route
    Either use the decorator: "@WebServer.addRoute('/example')" before the def
    Or call "WebServer.addRoute('/example', example)" directly
    """
    return 'example'


# WebServer.addRoute('/example', example)
