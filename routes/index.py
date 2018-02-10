from include.WebServer import WebServer
# import utils.debug


def index():
    routes = WebServer.getRoutes()
    # print utils.debug.dump(routes)
    print routes
    return WebServer.render('index.html')


WebServer.addRoute('/', index)
