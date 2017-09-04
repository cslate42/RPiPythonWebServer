from threading import Thread
import time

# import app
import myGlobals

thread = None
count = 0

def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        time.sleep(1)
        count += 1
        myGlobals.sio.emit('my response', {'data': 'Server generated event'}, namespace='/test')
        break

def prepareThreads():
    """
    Setup threads for html routes
    """
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return
