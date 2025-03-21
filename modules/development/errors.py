class DevelopmentError():
    def __init__(self, module_name: str, function_name:str, message:str):
        super().__init__(f"""This program has reached an irreconcilable state and has to exit.
This is NOT your fault.  The developer made a mistake. If you have anyway
to let them know about what happened, I am sure they would appreciate it.
                         
Module: {module_name}: Function: {function_name}: {message}
""")