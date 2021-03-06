__all__ = ('ScriptError', 'ImportScriptError', 'InstallDependencyError')


class ScriptError(Exception):
    """
    A general script exception all other exceptions are derived from.
    """
    pass


class ImportScriptError(ScriptError):
    """
    A script could not be imported.

    Arguments:
        - `name`: The name of the script.
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Could not import script: {}'.format(self.name)


class InstallDependencyError(ScriptError):
    """
    A script dependency could not be installed.

    Arguments:
        - `dependency`: The dependency.
    """
    def __init__(self, dependency):
        self.dependency = dependency

    def __str__(self):
        return 'Could not install dependency: {}'.format(self.dependency)
