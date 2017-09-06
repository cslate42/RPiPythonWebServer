#! /usr/bin/python2.7

"""
The application to run the demo
@see https://github.com/miguelgrinberg/python-socketio
@see https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
"""
import my_pi_server
from lib import basic_io

def main():
    """Setup application"""
    try:
        basic_io.setup()
        my_pi_server.setup()
    except KeyboardInterrupt:
        basic_io.shutdown()

if __name__ == "__main__":
    main()
