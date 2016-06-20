#!/bin/bash python

# set this to 'threading', 'eventlet', or 'gevent'
async_mode = 'threading'

if async_mode == 'eventlet':
    import eventlet
    eventlet.monkey_patch()
elif async_mode == 'gevent':
    from gevent import monkey
    monkey.patch_all()

import app
import myGlobals

if __name__ == "__main__":
    if async_mode == 'threading':
        # deploy with Werkzeug
        myGlobals.app.run(threaded=True)
    elif async_mode == 'eventlet':
        # deploy with eventlet
        import eventlet
        eventlet.wsgi.server(eventlet.listen(('', app.port)), myGlobals.app)
    elif async_mode == 'gevent':
        # deploy with gevent
        from gevent import pywsgi
        try:
            from geventwebsocket.handler import WebSocketHandler
            websocket = True
        except ImportError:
            websocket = False
        if websocket:
            pywsgi.WSGIServer(('', port), myGlobals.app, handler_class=WebSocketHandler).serve_forever()
        else:
            pywsgi.WSGIServer(('', port), myGlobals.app).serve_forever()
    else:
        print('Unknown async_mode: ' + async_mode)
