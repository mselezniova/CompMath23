from rational_numbers import Rational # import class Rational from rational_numbers.py
import numpy as np

N = 20

# Generate the first 20 factors of the Wallis product formula
factors = [Rational((2*n)**2, (2*n-1)*(2*n+1)) for n in range(1,N+1) ]

# Generate the first 20 approximations of pi as products of the factors up to index i=1,...,20
partial_products = [2*np.prod(factors[:i]) for i in range(1,N+1)]

# Print the partial products
print(f"Partial products as Rational numbers:\n {[partial_products[i] for i in range(0,N)]}\n")

# Now we study the convergence to pi using the value of np.pi
print(f"Difference between pi and partial products as floating point numbers:\n {np.pi - np.array([float(i) for i in partial_products])}")
print("We see that the difference between pi and the partial products decreases with N!")