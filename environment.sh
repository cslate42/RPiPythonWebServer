#!/bin/bash
# https://stackoverflow.com/a/19401753
# http://www.linuxjournal.com/content/return-values-bash-functions
# https://ryanstutorials.net/bash-scripting-tutorial/bash-functions.php

echo "========================================================================="
echo "              This doesn't work since this runs as a fork"
echo "========================================================================="

function isEnvironmentSetup() {
    isEnvironmentSetup=0
    # find the location of python
    py_path=$(which python)
    # check if the virtual environment is used
    if [[ $py_path =~ $(pwd) ]]; then # py_path contains current working directory
        isEnvironmentSetup=1
    fi
    return $isEnvironmentSetup
}

$(isEnvironmentSetup)
isSetup=$?
if [[ $isSetup != 1 ]]; then # py_path doesn't use virtual environment
    echo "Activating Python Dir $(pwd)/bin/activate"
    # setup python virtual environment
    $(source bin/activate)
else
    echo "Environment currently configured"
fi

# # exit virtual environment
# $(deactivate)
