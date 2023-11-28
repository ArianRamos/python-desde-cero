#!/usr/bin/python3
#Realiza un programa que compruebe si una cadena contiene una 
#subcadena las dos cadenas se introducen por teclado

cad = input("Introduce una cadena:")
subcad = input("Introduc una subcadena")

if cad.find(subcad) > -1:
	print("La cadena contiene la subcadena.")
else:
	print("La cadena no contiene subcadena.")
#Otra forma

if subcad in cad:
	print("La cadena contiene la subcadena")
else:
	print("La cadena no contiene la subcadena")
