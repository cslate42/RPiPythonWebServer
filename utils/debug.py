from pprint import pprint


def dump(var):
    print type(var)
    pprint(vars(var))
    # return (vars(var))
