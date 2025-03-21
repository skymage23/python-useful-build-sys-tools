class ShellMissingError(Exception):
    def __init__(self, shell):
        #Hello
        super().__init__("\"{}\", the supported shell program is not on the system PATH.".format(shell))

class UnsupportedOSError(Exception):
    def __init__(self, os_in_question):
        super().__init__(f"""Unfortunately, \"{os_in_question}\" is not yet supported by this software.""")