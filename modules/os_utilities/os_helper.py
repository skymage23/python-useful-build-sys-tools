import os
import errors
#We only support a handful of shells. So, make sure they exist on the system PATH

def is_program_on_system_PATH(program_name):
    #Hello
    for path in os.environ["PATH"].split(os.pathsep):
        if os.path.exists(os.path.join(path, program_name)):
            return True 
    return False

class OSHelper:
    def initialize(self, shell):
        if not is_program_on_system_PATH(shell):
            raise errors.ShellMissingError(shell)
        self.shell = shell
    def get_shell(self):
        return self.shell