

def success(message=None, data=None):
    return {
        'status' : 'success',
        'message' : message,
        'data' : data
    }


def error(message=None, errors=None):
    return {
        'status' : 'error',
        'message' : message,
        'errors' : errors
    }
