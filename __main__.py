#!/usr/bin/python
"""
Startup the app and switch to virtualenv
"""
import os
import sys


def isRunningVirtualenv():
    """
    Solution found from https://stackoverflow.com/a/1883251
    """
    return hasattr(sys, 'real_prefix')


def setupVirtualEnvironment():
    # TODO allow both $ ./__main__.py and $ python RPiPythonWebServer/
    # issue with os cwd or sys.path?
    if os.path.dirname(__file__) != '.':
        raise EnvironmentError("Must run from root of project ie: $ ./run.sh")

    if isRunningVirtualenv():
        activatePath = os.path.dirname(__file__) + '/bin/activate_this.py'
        execfile(activatePath, dict(__file__=activatePath))
        isVirtualEnv = isRunningVirtualenv()
    else:
        isVirtualEnv = True

    return isVirtualEnv


def main():
    from include.WebServer import WebServer
    WebServer.setupEnvironment()
    WebServer.addRoutes()

    try:
        WebServer.run()
    except KeyboardInterrupt:
        WebServer.shutdown()


if __name__ == '__main__':
    if setupVirtualEnvironment():
        main()
    else:
        raise RuntimeError("Unable to switch to virtualenv")
