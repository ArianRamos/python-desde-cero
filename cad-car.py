#!/usr/bin/python3
# Pide una cadena y un carácter por teclado
#(valida que se un carácter) y muestra cuantas veces 
#aparece el caracter en la cadena

cad = input("Introduce una cadena:")
while True:
	car = input("Introduce un caracter")
	if len(car) == 1: break

print("En la cadena",cad,"aparecen",cad.count(car),"veces el caracter",car)
