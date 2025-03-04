class ShellMissingError(Exception):
    def __init__(self, shell):
        #Hello
        super().__init__("\"{}\", the supported shell program is not on the system PATH.".format(shell))