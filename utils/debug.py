from pprint import pprint


def dump(var):
    """
    Emulate php's var_dump
    TODO do for any var type
    Args:
        var (any): the variable to dump
    """
    print type(var)
    pprint(vars(var))
    # return (vars(var))
