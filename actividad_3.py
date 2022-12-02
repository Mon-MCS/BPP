"""
Se recrea la documentación de la actividad_1 de esta asignatura
"""


# Se muestra la clase que se crea para mostrar la excepción
class Miexcepcion(Exception):
    '''Aparece cuando el número entero introducido es mayor de 10'''
    
    pass

print(Miexcepcion.__doc__)
def funcion_solicitar():
    """1. Crea una función que pida por pantalla un número al usuario y que controle 
    mediante excepciones lo siguiente. Sólo se podrá introducir números enteros.
    Si el número es mayor de 10 se lanza una excepción con raise la cual hayas 
    creado previamente mediante class Miexcepcion(Exception).

    :param numero: Número que se solicita al usuario
    :type numero: int, optional
    :raises Miexcepcion: Se introduce un número superior a 10
    :return None
    """
    try:
        numero = int(input("Introduzca un número entero y menor de 11: "))
        # Se establece la condición que controla si el número introducido es mayor de 10, 
        # para que se muestre el error creado (apartado b.)
        if (numero>10):
            raise Miexcepcion({"num":"El número entero introducido es mayor de 10"})
    # Se controla que el usuario sólo introduzca números enteros (apartado a.)   
    except ValueError:
        print("El valor introducido no es un número entero")
    # Se controla la excepción de que el número introducido sea mayor que 10
    except Miexcepcion as e:
        aux = e.args[0]
        print(aux["num"])
    # Se controla si se produce otra excepción
    except Exception as e:
        print("Ha ocurrido un error: ", e)
print(funcion_solicitar.__doc__)
funcion_solicitar()
def funcion_archivo():
    """ 2. Abre un fichero .txt y controla mediante excepciones las diferentes casuísticas para
    que el progama no termine de forma inesperada. Utiliza el finally para cerrar el fichero.
    Para que no salte un error en el if del finally, si no se encuentra el archivo,
    se iguala f a False.
    
    :param f: Variable para evitar error en la ejecución, que también sirve para realizar operaciones sobre un fichero
    :type f: booleano o fichero
    :return None
    """
    f = False
    from io import UnsupportedOperation
    try:
        f = open("leccion_1.txt", 'r', encoding='utf-8')
        f.write("Hola\n")
        print(f.readlines())
    # Se controla si no se localiza el archivo
    except FileNotFoundError:
        print("Error archivo no encontrado")
    # Se controla si se produce un fallo en la descodificación
    except UnicodeDecodeError:
        print("Error al descodificar el documento")
    except UnsupportedOperation:
        print("Error al intentar realizar una operación no permitida")
    # Se controla si se produce otra excepción
    except Exception as e:
        print("Ha ocurrido un error: ", e)
    finally:
        if f:
            f.close()
print(funcion_archivo.__doc__)
funcion_archivo()