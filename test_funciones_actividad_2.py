"""
Implementa un Script con un conjunto de funciones y crea un mínimo de 5 test para cada 
una de las librerías de test vistas en clase (unittest y pytest) 
"""

from funciones_actividad_2 import *
import unittest

# Se crean los test normales para las funciones suma, resta, multiplicación, división, 
# módulo, raíz y potencia.

def test_suma_pytest():
    assert suma(3,2) == 5
    
def test_resta_pytest():
    assert resta(5,2) == 3

def test_multiplicacion_pytest():
    assert multiplicacion(5,3) == 15
    
def test_division_pytest():
    assert division(23,1) == 23

def test_modulo_pytest():
    assert modulo(15,5) == 0

def test_raiz_pytest():
    assert raiz(4) == 2
    
def test_potencia_pytest():
    assert potencia(2,3) == 8

# Se realizan ahora test con unittest, donde algunos test se modifican ligeramente para 
# no repetir lo realizado previamente
 
class Test_Unittest_actividad_2(unittest.TestCase):
    # Se emplea sólo el siguiente test unitario que presenta el mismo carácter que 
    # en los test de pytest
    def test_multiplicacion_unittest(self):
        resultado = multiplicacion(2,4)
        self.assertEqual(resultado,8)
    
    # Se realizará la división sólo si el divisor es distinto de 0
    def test_division_unittest(self):
        divisor=5
        self.assertNotEqual(0,divisor, "Error, no se puede dividir por 0")
        resultado = division(10,divisor)
        self.assertEqual(resultado,2)
    
    # Se comprueba que el número introducido es un elemento flotante
    def test_raiz_unittest(self):
        num=4.0
        self.assertIsInstance(num,float,"El elemento introducido no es un número real")
        resultado=raiz(4)
        self.assertEqual(resultado,2)
    
    # Se realiza una multiplicación o una potencia según el valor de b
    def test_potencia_unittest(self):
        a=3
        # b=2
        b=3
        if b==2:
            resultado=multiplicacion(a,a)
            self.assertEqual(resultado,9)
        else:
            resultado=potencia(a,b)
            self.assertEqual(resultado,27)
    
    # Se mostrará un error siempre que b no sea divisor de a
    def test_modulo_unittest(self):
        a=6
        b=3
        resultado=modulo(a,b)
        self.assertTrue(resultado==0,f"El número {b} no es divisor de {a}")

            