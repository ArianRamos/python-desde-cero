#!/usr/bin/python3
#Funcion CalcularAreaPerimetro:

import math
def CalcularAreaPerimetro(radio):
	area = math.pi * radio ** 2;
	perimetro = 2 * math.pi * radio;
	return area,perimetro
#Diseña una funcion que calcule el area y el perimetro

radio = float(input("Introduce el radio:"))
area,perimetro = CalcularAreaPerimetro(radio)
print("Area:",area)
print("Perimetro:",perimetro)
