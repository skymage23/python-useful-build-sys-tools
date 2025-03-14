from . import os_helper

class WindowsHelper(os_helper.OSHelper):
    def __init__(self):
        self.initialize("powershell.exe")