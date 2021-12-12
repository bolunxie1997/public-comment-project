from functools import wraps
from flask import session,jsonify,request,make_response

def login_required(func):
    """Make sure user has been login
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        if (request.cookies.get('user_id')):
            return func(*args,**kwargs)
        else:
            response = make_response(jsonify({"result":-1,"msg":"You are Not Login"}))
            response.headers['Access-Control-Allow-Credentials']='true'
            return response
    return wrapper

def admin_required(func):
    """Make sure user has been login
    """
    @wraps(func)
    def wrapper(*args,**kwargs):
        if (request.cookies.get('user_id')):
            if(request.cookies.get("user_type")=='2'):
                return func(*args,**kwargs)
            else:
                response = make_response(jsonify({"result":-1,"msg":"You are Not Admin"}))
        else:
            response = make_response(jsonify({"result":-1,"msg":"You are Not Login"}))
        response.headers['Access-Control-Allow-Credentials']='true'
        return response
    return wrapper