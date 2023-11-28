#!/usr/bin/python3
def factorial(n):
	"""Calcula el factorial de un numero"""
	resultado = 1
	for i in range(1,n+1):
		resultado*=i
	return resultado

num = int(input("Dame un numero:"))
print(factorial(num))
