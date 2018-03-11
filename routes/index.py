import include.WebServer as WebServer


@WebServer.addRoute('/')
def index():
    routes = WebServer.getRoutes()
    return WebServer.render('index.html', {
        'routes': routes
    })
# WebServer.addRoute('/', index)
