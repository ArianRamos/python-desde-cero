#!/usr/bin/python3
#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.
for tabla in range(1, 6):
	for  num in range(1, 11):
		print("%d * %d = %d" %(num,tabla,num*tabla))
