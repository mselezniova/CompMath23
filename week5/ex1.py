from math import sqrt 
import time

# a)
print("-----------------------------------------------------------------------------------------")
print("Exercise a):\n")

def is_prime(n):
    for i in range(2,int(sqrt(n))+1): # Notice that any nonprime number n has a factor not larger than sqrt(n). 
                                      # Therefore, it is enough to run the cycle until sqrt(n
        
        if n % i == 0: # n % i returns the remainder of dividing n by i
            return False
    return True


tests = [17,28,131,1573]

for n in tests:
    if is_prime(n):
        print(f"    {n} is a prime.")
    else:
        print(f"    {n} is not a prime.")


# b)
print("-----------------------------------------------------------------------------------------")
print("Exercise b):\n")

def factorize(n):
    factors = dict()
    
    i = 2
    while i <= int(sqrt(n))+1: # As before, the cycle only goes until sqrt(n)
                               # Note that it is much better (for efficiency) to use a while cycle than a for cycle here
                               # because while cycle updates the value of int(sqrt(n))+1 as you change n inside the cycle
                               # (for cycle only creates the list to iterate over once when you enter a cycle)
        while n%i == 0:
            if i in factors:
                factors[i] += 1
            else: 
                factors[i] = 1
            n = n//i # n//i is integer division of n by i 
        i += 1
     
    if n != 1: # If there is no divisor smaller than sqrt(n)+1 then the final value of n is the last prime divisor with multiplicity 1!
        factors[n] = 1
        
    return factors


tests = [17,28,131,1573]

for n in tests:
    print(f"    The factors of {n} are: {factorize(n)}")

# c)
print("-----------------------------------------------------------------------------------------")
print("Exercise c):\n")

for n in [526891377, 479001599]:

    start = time.time()
    factors = is_prime(n) 
    end = time.time()
    print(f"    Time to check if {n} is prime: {end - start}s")

    start = time.time()
    factors = factorize(n) 
    end = time.time()
    print(f"    Time to factorize {n}: {end - start}s\n")

print("    This is already quite efficient! Check how your implementation compares!")
print("-----------------------------------------------------------------------------------------")

