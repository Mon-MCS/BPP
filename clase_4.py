#import pdb
#pdb.set_trace()

"""1. Haciendo uso de comprensión de listas realice un programa que,
    dado una lista de números enteros, devuelva el máximo de cada lista."""

def max_lista(lista):
    """Función que recibe una lista de listas de números enteros y devuelve 
    el máximo de cada lista. 
    
    param lista: Lista de números enteros
    type lista: list
    param maximos_sublitas: Lista que contiene los máximos de cada sublista
    type maximos_sublitas: list
    """
    # Se utiliza compresión de listas para extraer el máximo de cada sublista
    maximos_sublistas=[max(sublista) for sublista in lista]
    return maximos_sublistas

# Prueba de que funciona la definición que se buscaba
if __name__ == '__main__':
    ejem_lista=[[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]
    mostrar=max_lista(ejem_lista)
    print(f"Los máximos de las sublistas de la lista de enteros {ejem_lista} es {mostrar}")
 
 
"""2. Haga uso de la función filter para construir un programa que, dado una lista de n
números devuelva aquellos que son primos. Por ejemplo, dada la lista [3,4,8,5,22,13],
el programa que implemente debe devolver como resultado [3,5,5,13]"""   
def es_primo(n):
    """Función que recibe una lista de n números y devuelve True si son primos, 
    en caso contrario devuelve False.
    
    param n: Lista de números enteros
    type n: list
    param primo: Variable para controlar si los números contenidos en n son primos.
    type primo: booleano
    param j: Contador del bucle
    type j: int
    """
    primo=True
    j=2
    while j<n and primo==True:
        if n%j==0:
            primo=False
        j+=1
    return primo

# Ejemplo para comprobar que funciona la función
posibles_primos=[3,4,8,5,5,22,13]
"""Se recurre a filter para aplicar la función a la lista de posibles_primos y devolver 
aquellos número cuyo valor sea True (por lo que son primos).
"""
primos=list(filter(es_primo,posibles_primos))
print(f"Los primos de la lista de enteros introducida {posibles_primos} son {primos}")
            