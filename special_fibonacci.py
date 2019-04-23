# author - Manoj T M 
# program finds the nth fib term and adds all the fib term and then prints the result in modulo of m 
import math
m = input("Enter the modulo - ")
def fib(n):
    sqrt_5 = math.sqrt(5)
    lambda_1 = (1 + sqrt_5) * 0.5 # due to math.sqrt function the required value of fib is no accurate, it is only approximate
    lambda_2 = (1 - sqrt_5) * 0.5
    return int((((lambda_1 ** (n+1)) - (lambda_2 ** (n+1)))/sqrt_5+0.5)) % int(m)
    
number_atoms = input("Enter Number of atoms - ")
dia = input("Enter the dias of %s atoms - " % number_atoms)
dias = (int(e) for e in dia.split(', '))
print(ans(dias))

# alternate - accurate - using the Fibonacci Q-matrix

import numpy as np
m = input("Enter the modulo - ")

def fib(n):
    return (np.matrix("0 1; 1 1", dtype=np.object)**(n+1)).item(1) % int(m) #[0,1;1,1] - Fibonacci Q-matrix

def ans(dias_):
    fibs = list(map(fib, dias_))
    print(fibs)
    fib_sum = sum(fibs)
    return fib_sum % int(m)

number_atoms = input("Enter Number of fib_numbers - ")
fib_seq = input("Enter the values of %s fib_numbers - " % fib_numbers)
fib_seq = (int(e) for e in dia.split(', '))
print(ans(fib_seq))

# alternately
# the nth fib term can also be determined by matrix exponentiation with O(logN) time complexity
