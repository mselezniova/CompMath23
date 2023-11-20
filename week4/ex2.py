from math import sqrt

# a)
print("-----------------------------------------------------------------------------------------")
print("The solution to exercise a):\n")

res = 0.3+0.3+0.3 
print(f"    In Python, 0.3+0.3+0.3={res}.")
res = (0.3+0.3+0.3 == 0.9) # here "0.3+0.3+0.3 == 0.9" is either True or False, so res is a binary variable equal to either True or False 
print(f"    And \"0.3+0.3+0.3==0.9\" returns \"{res}\". Wow!\n")

# b)
print("-----------------------------------------------------------------------------------------")
print("The solution to exercise b):\n")

x=1
y=1 + 10**-16*sqrt(3)
z1 = sqrt(3) 
z2 = 10**16*(y-x)

print(f"    The difference between 10^16*(y-x) and sqrt(3) is {z2-z1}. This is a lot. \n")

# c) 
print("-----------------------------------------------------------------------------------------")
print("The solution to exercise c):\n")

def method1(p, q): # a function to compute the roots using the first method
    return p + sqrt(p ** 2 - q), p - sqrt(p ** 2 - q)

def method2(p,q): # a function to compute the roots using the second method
    x1 = p + sqrt(p ** 2 - q)
    return x1, q / x1


for a in [2,100]: # we use both methods for a=2 and a=100 
    q = 1
    p = (a + 1/ a)/ 2
    
    print(f"    Case a={a}:")
    print(f"      - The correct roots are {a} and {1/a}.")
    
    x1, x2 = method1(p, q)
    print(f"      - The first method gives roots {x1} und {x2}")
    
    x1, x2 = method2(p, q)
    print(f"      - The second method gives roots {x1} und {x2}\n")

print("-----------------------------------------------------------------------------------------")