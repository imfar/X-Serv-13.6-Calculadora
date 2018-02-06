#!/usr/bin/python3
import sys

if len(sys.argv)==4:
	try:
		funcion=sys.argv[1]
		op1=float(sys.argv[2])
		op2=float(sys.argv[3])
		#operadores tipo 'ints' o 'floats': no problem
		#otro tipo: excepcion
	except ValueError:
		print('Error: Los operadores deben ser NUMEROS')
		raise SystemExit	

	#overflow aritmetico:
	#'ans' infinitamente grande = 'inf'(infinito)
	if funcion=="sumar":
		ans=op1+op2
		print(ans)

	elif funcion=="restar":
		ans=op1-op2
		print(ans)

	elif funcion=='multiplicar':
		ans=op1*op2
		print(ans)
	
	elif funcion=='dividir':
		try:
			ans=op1/op2
			print(ans)
		except ZeroDivisionError:
			print('Error: Division por cero')
	
	else:
		print('Valid functions: <sumar, restar, multiplicar, dividir>')
	 
else:
	print('usage: <function> <operador1> <operador2>')


