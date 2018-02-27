from include.WebServer import WebServer
# import utils.debug


def index():
    routes = WebServer.getRoutes()
    return WebServer.render('index.html', {
        'routes': routes
    })


WebServer.addRoute('/', index)
