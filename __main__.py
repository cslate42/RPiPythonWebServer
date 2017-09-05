#! /usr/bin/python2.7

"""
The application to run the demo
@see https://github.com/miguelgrinberg/python-socketio
@see https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
"""
import my_pi_server

def main():
    """Setup application"""
    my_pi_server.setup()

if __name__ == "__main__":
    main()
