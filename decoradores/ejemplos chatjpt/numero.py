def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count +=1
        result=func(*args, **kwargs)
        print(f"{func.__name__} ha sido llamada {wrapper.count} veces")
        return result
    wrapper.count=0
    return wrapper

@counter
def foo():
    pass

foo()
foo()
foo()
foo()
foo()
foo()
foo()