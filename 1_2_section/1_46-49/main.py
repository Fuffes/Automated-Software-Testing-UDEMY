import functools

user = {"name" : "Nata", "access_level": "admin"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_func(*args, **kwargs):
            if user["access_level"] == "admin":
                return func(*args, **kwargs)
            else:
                print("you dont have access")
            
        return secure_func
    return decorator


@make_secure("admin")
def get_password(role):
    if role == "admin":
        return "123"
    elif role == "user":
        return "user"

@make_secure("user")
def get_dashboard_password():
    return "user: User_password"


print(get_password("admin"))