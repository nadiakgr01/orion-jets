import argparse

def main():
	parser = argparse.ArgumentParser(
		description='Realiza una operación aritmética simple entre dos números.'
	)
	
	# Argumentos obligatorios: x y y
	parser.add_argument(
		'x',
		help='Primer número.',
		type=float,
	)
	parser.add_argument(
		'y',
		help='Segundo número',
		type=float,
	)
	
	# Opción para elegir la operación
	parser.add_argument(
		'--operacion',
		choices=['sumar', 'restar', 'multiplicar', 'dividir'],
		default='sumar',
		help='Operación a realizar: "sumar" (por defecto), "restar", "multiplicar o dividir"',
	)
	
	# Opción booleana "verbose"
	parser.add_argument(
		'--verbose',
		action='store_false',
		help='Si se activa, muestra una salida más detallada.'
	)
	
	parser.add_argument(
	    '--precision',
	    type=int,
	    default=2,
	    help='Número de decimales'
	)
	
	args = parser.parse_args()
	
	# Lógica de la operación
	if args.operacion == 'sumar':
		resultado = args.x + args.y
		operador = '+'
	elif args.operacion == 'restar':
		resultado = args.x - args.y
		operador = '-'
	elif args.operacion == 'multiplicar':
	    resultado = args.x * args.y
	    operador = '*'
	elif args.operacion == 'dividir':
	    resultado = args.x / args.y
	    operador = '/'
	else: # Nunca deberíamos de llegar
	    raise ValueError('Operación no permitida')
	    
	# Opción para redondear
	resultado = round(resultado, ndigits=args.precision)
		
	# Impresión según verbose
	if args.verbose:
		print(f"{(resultado := round(resultado, ndigits=args.precision))}")

	else:
		print(f'{args.x} {operador} {args.y} = {resultado}')
		
if __name__ == '__main__':
	main()
