#!/usr/bin/env python

import numpy as np
from timeit import default_timer as timer

x = np.arange(100000.).reshape(1000,100)
y = np.arange(100000.).reshape(1000,100)

def sum(A,B):
    return A*B

def iterate(X):
	for i in range(len(X)):
		for j in range(len(X[i])):
			X[i][j] = 0.000002
			print("Value:", X[i][j], "Index i = %i" %i, "Index j = %i" %j)
			

def main():
	start = timer()
	z = sum(x,y)
	final = timer() - start
	print(z)
	print("Execution time %f" %final)
	start1 = timer()
	iterate(z)
	final = timer() - start
	print("Execution time %f" %final)

if __name__ == '__main__':
	main()
	
