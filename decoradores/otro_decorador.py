def add_arguments(arg1, arg2, arg3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(arg1, arg2, arg3, *args, **kwargs)
        return wrapper
    return decorator

@add_arguments("Hello", "world", 234567)
def print_args(*args):
    for arg in args:
        print(arg)

print_args()