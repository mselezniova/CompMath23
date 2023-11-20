from math import pi, e, sqrt, factorial

# a)
print("-----------------------------------------------------------------------------------------")

res = abs(pi ** e - e ** pi) # abs() is a built-in Python function to compute the absolute value

print(f"The solution to exercise a) is {res:.3}\n") # '.3' means that we round to the first 3 digits
													# '\n' prints an empty line

# b)
print("-----------------------------------------------------------------------------------------")

n = 1000
res = sqrt(n + sqrt(n)) - sqrt(n - sqrt(n))

print(f"The solution to exercise b) is {res}\n") 

# c)
print("-----------------------------------------------------------------------------------------")
# we create a function to compute S(n)
def S(n):  
	return sqrt(2 * pi) * (n ** (n + 0.5)) * (e ** (- n)) 

print('The solution to exercise c):\n')
 
for n in [5,10,15,20]: # we calculate S(n) and compare with n! for each value of n in a cycle
	S_n = S(n)
	factorial_n = factorial(n)
	diff = abs(factorial_n - S_n) 

	print(f"    For n={n}, we get |S-n!|/n!={diff/factorial_n}.") # we compute a ratio |S-n!|/n! to compare S(n) witn n!

print("\n-----------------------------------------------------------------------------------------")
