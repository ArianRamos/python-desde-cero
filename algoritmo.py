#!/usr/bin/python3
#Algoritmo que pida un número y diga si es positivo, negativo o 0.
num = int(input("Dime el numero:"))
if num == 0:
	print("Es igual a 0")
else:
	if num > 0:
		print("Es positivo")
	else:
		print("Es negativo")
