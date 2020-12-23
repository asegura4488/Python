from decimal import getcontext, Decimal
getcontext().prec = 100

def fib(n):
     result = []
     a,b=0,1
     o=0.
     while b < n:
          #print(b)
          a,b = b,a+b
          o=Decimal(b)/Decimal(a)
          result.append(b)
          print("the golden number is: ", o)
     return result

f_lista = fib(1E100)

for i in range(len(f_lista)):
     print(i, f_lista[i])
