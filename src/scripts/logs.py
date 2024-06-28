""" Archivo par amanejo de los logs del servicio """

def before_app_request():
    """
    It's a function that runs before every request
    """
    print("before_app_request")

def after_app_request(resp):
    """
    The function `after_app_request` is called after the request is processed by the Flask app
    """
    print("after_app_request")
    return resp

def teardown_app_request(_error):
    """
    It's a function that is called after every request, and it prints "teardown_app_request" to the
    console
    """
    if _error:
        print("teardown_app_request")
