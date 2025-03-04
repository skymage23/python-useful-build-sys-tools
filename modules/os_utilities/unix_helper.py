from . import os_helper

class UNIXHelper(os_helper.OSHelper):
    def __init__(self):
        self.initialize("sh")