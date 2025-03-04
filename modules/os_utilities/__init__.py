import sys

from . import errors
from . import windows_helper
from . import macos_helper
from . import linux_helper


def is_windows():
    return sys.platform.startswith('win32') or sys.platform.startswith('cygwin')

def is_linux():
    return sys.platform.startswith('linux')

def is_macos():
    return sys.platform.startswith('darwin')

def get_os_helper():
    if is_windows():
        return windows_helper.WindowsHelper()
    
    if is_macos():
        return macos_helper.MacosHelper()
    
    if is_linux():
        return linux_helper.LinuxHelper()
    
    raise errors.UnsupportedOSHelper()