#!/usr/bin/python3
#Realisa un programa que comprueba si una cadena eleida por teclado
#comienza por una subcadena introducida por teclado

cad = input("Introduce una cadena:")
subcad = input("Introduce una subcadena:")
if cad.startswith(subcad):
	print("La cadena comienza por la subcadena")
else:
	print("La cadena NO comienza por la subcadena")
