import development

SUCCESS_ERRCODE = 0
GENERIC_ERROR_ERRCODE = 1

next_available = 1
errcodes = {
    "success": SUCCESS_ERRCODE,
    "generic_error": GENERIC_ERROR_ERRCODE    
}
messages = {
    SUCCESS_ERRCODE: "Success",
    GENERIC_ERROR_ERRCODE: "Unknown error."
}

def gen_errcode():
    retval = next_available
    next_available += 1
    return retval

def register_errcode(name: str = None, message: str = None):
    if name is None:
        raise ValueError("\"name\" cannot be None.")

    if message is None:
        raise ValueError("\"message\" cannot be None.")

    errcode = gen_errcode()
    errcodes[name] = errcode
    messages[errcode] = message
    return errcode

def get_message(errcode):
    if isinstance(errcode,int):
        return messages[errcode]
    elif isinstance(errcode, str):
        return messages[errcodes[errcode]]

    raise development.errors.DevelopmentError(
        "error_handling.errcode_handling",
        "get_message",
         f"\"{errcode}\" is neither a valid errcode nor the name of one."
    )