import random
from ex2a import monthy_hall # We import the solution of exercise 2a) as a module! 
                             # Now we can use the monthy_hall() function in this script as well!
                             # Note the idiom " if __name__ == "__main__": " that we used in ex2a.py
                             # to differentiate the behavior of ex2a.py when it is run as a script 
                             # and when it is imported as a module (as here)


n = 10000

scenario_1 = []
scenario_2 = []

for i in range(n):
    scenario_1.append(monthy_hall(start_choice=random.choice([1,2,3]),
                                  change_choice='no', verbose=False))
    scenario_2.append(monthy_hall(start_choice=random.choice([1,2,3]),
                                  change_choice='yes', verbose=False))


print(f"The probability to win in the first scenario is {sum(scenario_1)/n*100:.2f}%.")
print(f"The probability to win in the second scenario is {sum(scenario_2)/n*100:.2f}%.")