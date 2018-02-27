import include.WebServer as WebServer
# import utils.debug


def index():
    routes = WebServer.getRoutes()
    return WebServer.render('index.html', {
        'routes': routes
    })


WebServer.addRoute('/', index)
