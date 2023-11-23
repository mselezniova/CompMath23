import numpy as np
import time
from itertools import combinations 


# a)
print("-----------------------------------------------------------------------------------------")
print("Exercise a:\n")
print(f"The equation (*) is {27**5 + 84**5 + 110**5 + 133**5 == 144**5}") # print True or False 

# b)
print("-----------------------------------------------------------------------------------------")
print("Exercise b:\n")

nums = np.arange(1,145,1)**5  # array of integers from 1 to 144 in fifth power
combs = np.array(list(combinations(nums, 4))) # create a *generator* with all the combinations of 4 elements from array nums
                                              # and convert it to a numpy array 

sums = combs.sum(axis=1) # create an array of sums of the integers in fifth power 
                         # by summing elements of each row in the combinations array

start = time.time()

num_counterexamples = 0
for s, c in zip(sums,combs): # zip() function creates a single iterator out of several paired iterators
                             # i.e., zip(sums,combs) iterates over ( (sums[0], combs[0]),  (sums[1], combs[1]), ... , (sums[n], combs[n]) )


    if s in nums:
        print(f"Integers {[int(i**(1/5)) for i in c]} in fifth power sum to {int(s**(1/5))}^5.")  
        num_counterexamples += 1

end = time.time()

if num_counterexamples == 1:
    print("Only one set of integers smaller than 144 satisfies the condition. Therefore, the statement is true! \n")

print(f"Time to check the statement with the for loop: {end-start}")

# c)
print("-----------------------------------------------------------------------------------------")
print("Exercise c:\n")
# We can also use numpy to avoid the long loops and thus check the statement much faster
start = time.time()

intersection = np.isin(sums, nums) # if sum[i] is an element of sums, intersection[i] = True
                                   # otherwise, intersection[i] = False

if np.sum(intersection) == 1: # np.sum() sums True as 1 and False as 0
    
    print("Only one set of integers smaller than 144 satisfies the condition. Therefore, the statement is true! \n")

end = time.time()

print(f"Time to check the statement with np.isin (without for loop): {end-start}") # around 10 times faster than the for loop!


