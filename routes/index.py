import include.WebServer as WebServer
# import utils.debug


@WebServer.addRoute('/asdf')
def asdf():
    return WebServer.render('index.html', {
        'routes': ['asdf']
    })


def index():
    routes = WebServer.getRoutes()
    return WebServer.render('index.html', {
        'routes': routes
    })


WebServer.addRoute('/', index)
WebServer.addRoute('/dashboard', index)
