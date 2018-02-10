import pkgutil


def addAllSiblings(path):
    """
    Used by __init__.py
    Loads all modules in current directory and adds them to import
        Example usage:
            import utils.modules
            __all__ = utils.modules.addAllSiblings(__path__)
    """
    modules = []
    for loader, module_name, is_pkg in pkgutil.walk_packages(path):
        modules.append(module_name)
        # must have 'module = '
        module = loader.find_module(module_name).load_module(module_name)
        exec('%s = module' % module_name)
    return modules
