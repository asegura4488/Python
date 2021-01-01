import sys


list = [2,3,4]

try:

	num = int(input('Introduce un numero: '))
	#num = input('Introduce un numero: ')
	print('El reciproco es:', 1/num)
	print(list[num])


except ZeroDivisionError:
	print('--- Division by zero ---')
	print('The error was: ', sys.exc_info()[0])

# We could have several exceptions

except (ValueError, TypeError, IndexError):
	print('--- Error ---')
	print('The error was: ', sys.exc_info()[0])