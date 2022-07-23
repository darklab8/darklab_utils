import os

class ShellException(Exception):
    pass

def _shell_execute(cmd, show_cmd=True):

    if show_cmd:
        print(f"$ {cmd}")
    
    return_code = os.system(cmd)
    if return_code != 0:
        raise ShellException(f"return code is not zero for command: {cmd}")

class ShellMixin:
    @classmethod
    def shell(cls, cmd, show_cmd=True):
        _shell_execute(cmd, show_cmd=print)