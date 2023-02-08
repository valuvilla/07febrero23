import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Elapsed time: {end - start}")
        return result
    return wrapper

@timer
def long_running_function():
    for i in range(10000000):
        pass

long_running_function()
