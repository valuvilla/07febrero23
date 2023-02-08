def positive_number(func):
    def wrapper(x):
        if x < 0:
            raise ValueError("El número debe ser positivo")
        return func(x)
    return wrapper

@positive_number
def square(x):
    return x * x

print(square(4))
print(square(-4))
