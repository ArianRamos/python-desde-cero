#!/usr/bin/python3
while True:
	try:
		x = int(input("Introduce un numero:"))
		break
	except ValueError:
		print("Deber introducir un numero")
