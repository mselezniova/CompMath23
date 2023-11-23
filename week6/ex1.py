import numpy as np


# a)
print("-----------------------------------------------------------------------------------------")

seq_1 = np.sin(np.pi * np.arange(1,13))
print(f"Exercise a):\n {seq_1}\n") # each value in the array should be (approximately) zero

# b)
print("-----------------------------------------------------------------------------------------")
seq_2 = 1./ (1.+ np.arange(1,13)**2)
print(f"Exercise b):\n {seq_2}\n") 

# c)
print("-----------------------------------------------------------------------------------------")

vec = np.arange(1,100,2) # create an array of numbers from 1 to 99
vec[1::2] = -vec[1::2]   # take every second element of the array starting from index one (indexing [1::2]) 
						 # and replace its values with minus value 

print(f"Exercise c):\n {vec}\n")

# d)
print("-----------------------------------------------------------------------------------------")
print("Exercise d):")

# We first generate a matrix of powers of z in the disired matrix
n = 12 # size of the matrix

# construct a matrix with number i in all the columns of row i
mat = np.arange(n).repeat(n).reshape((n,n))  # numpy.repeat function repeats elements of an array a given number of times,
                                             # e.g. numpy.repeat([1,2,3],2)  = [1,1,2,2,3,3]

# replace all the diagonal values of the matrix with -1
mat[(np.arange(n), np.arange(n))] = np.array([-1]*n) # mat is now the matrix of powers of z that we need

print(f"Matrix of powers of z:\n {mat}\n")

z = (np.sqrt(3)+ 1j) / 2 # 1j is the imaginary unit in Python

# Now we get the desired matrix as z**mat
mat = z**mat

np.set_printoptions(precision=1) # np.set_printoptions() function determines the way numpy objects are printed
								 # here argument precision sets the number of digits to print for floating point numbers 

print(f"Final result:\n {mat}")





