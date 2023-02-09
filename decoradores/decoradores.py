#INICIO. Los decoaradores son funciones que modifican el comportamienti de otras funciones
# Acortan nuestro código
def mi_decorador(function):
    def nueva_function(a,b):
        print("Se llama a la función")
        c=function(a,b)
        print("Se ha llamado a la función")
        return c
    return nueva_function

@mi_decorador
def suma(a,b):
    print("Entra función suma")
    return a+b

@mi_decorador
def resta(a,b):
    print("Entra función resta")
    return a-b


print(suma(3,5))
# print(resta(4,7))


#DEFINIENDO DECORADORES.

def di_hola(): 
    print("Hola")

f1=di_hola() #llama a la función
f2=di_hola #Asigna a f2 la función

# print(f1) #None, di_hola no devuelve nada
# print(f2) #<function di_hola at 0x00000295D8712680>

# f1() # TypeError: 'NoneType' object is not callable
f2() #llama a la función f2

# del f2() # SyntaxError: cannot delete function call
del f2 # Borra función f2
# f2 # NameError: name 'f2' is not defined. Did you mean: 'f1'?


def operaciones(op):
    def suma(a,b):
        return a+b
    def resta(a,b):
        return a-b
    
    if op=="suma":
        return suma
    elif op=="resta":
        return resta

function_suma=operaciones("suma")
# print(function_suma(5,7))

function_resta=operaciones("resta")
# print(function_resta(5,7))


# ESCRIBIR NUESTRO PROPIO DECORADOR SIN @
def decorador(func):
    def envoltotio_func(a,b):
        print("Decorador antes de llamar a la función")
        c=func(a,b)
        print("Decorador despues de llamar a la función")
        return c
    return envoltotio_func

def suma(a,b):
    print("Dentro de suma")
    return a+b

# Nueva funcion decorada
funcion_decorada=decorador(suma)

# funcion_decorada(5,8)


#DECORADORES CON PARAMETROS.

def mi_decorador(arg):
    def decorador_real(function):
        def nueva_function(a,b):
            print(arg)
            c=function(a,b)
            print(arg)
            return c
        return nueva_function
    return decorador_real


@mi_decorador("IMPRIMIR ESTO ANTES Y DESPUES")
def suma(a,b):
    print("entra suma")
    return a+b

# suma(5,8)


 # @staticmethod # No necesita self
    # @classmethod # No necesita self
    # @property # No necesita self
    # **kwargs # Argumentos variables lista
    # *args # Argumentos variables dupla    