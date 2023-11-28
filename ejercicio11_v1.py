#!/usr/bin/python3
#Algoritmo que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

es_primo = True
numero_es_primo = int(input("Introduce un numero para comprobar si es un numero primo"))
for num in range(2, numero_es_primo):
	if numero_es_primo % num == 0:
		es_primo = False
		break
if es_primo:
	print("Es primo")
else:
	print("No es Primo")
