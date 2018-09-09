#!/usr/bin/python
"""
Startup the app and switch to virtualenv
Using google python documentation
@see http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html
"""
import os
import sys

def execfile(filepath, execGlobals=None, execLocals=None):
    if execGlobals is None:
        execGlobals = {}
    execGlobals.update({
        "__file__": filepath,
        "__name__": "__main__",
    })
    with open(filepath, 'rb') as file:
        exec(compile(file.read(), filepath, 'exec'), execGlobals, execLocals)


def isRunningVirtualenv():
    """
    Test if the virtual environment is running
    Solution found from https://stackoverflow.com/a/1883251
    Rreturn:
        bool: is using virtualenv
    """
    return hasattr(sys, 'real_prefix')


def setupVirtualEnvironment():
    """
    Switch to the virtual environment if not active
    Returns:
        bool: Is currently running virtual environment
    Raises:
        EnvironmentError: Must be running app from app root dir
    """

    if isRunningVirtualenv():
        activatePath = os.path.dirname(__file__) + '/bin/activate_this.py'
        execfile(activatePath, dict(__file__=activatePath))
        isVirtualEnv = isRunningVirtualenv()
    else:
        isVirtualEnv = True

    return isVirtualEnv


def main():
    """
    The main dispatcher
    """
    import include.WebServer as WebServer
    WebServer.setup()

    try:
        WebServer.run()
    except KeyboardInterrupt:
        WebServer.shutdown()


if __name__ == '__main__':
    """
    If executed call switch to virtualenv and call the dispatcher
    """
    if setupVirtualEnvironment():
        main()
    else:
        raise RuntimeError("Unable to switch to virtualenv")
