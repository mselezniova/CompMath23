import random
import time

# We write a function that can run a game either with player's input (using input() method) 
# or with initially set start_choice and change_choice as the function's parameters (to run the game automatically)

# The description of the function in ''' ''', which goes directly after the function definition,
# is the text that will be displayed if you call help() for this function
# Try calling help(monthy_hall) !
def monthy_hall(start_choice=None, change_choice=None, verbose=True):
    '''Simulation of the Monty Hall problem. 
    
    start_choice: If None, the player is asked to choose a door at the start of the game (as input). If start_choice is in [1,2,3], it specifies the initial door choice.
                  
    change_choice: If None, the player is asked if they want to change the choice or not (as input). If change_choice is in ['yes','no'], it specifies whether the player changes the choice after the host opens a door.
                  
    verbose: If True, the conversation between the player and the host is printed. If False, the game runs silently.
    
    '''
    
    all_doors = set([1,2,3])
    
    car = random.choice(list(all_doors))

    if start_choice is None:
        if verbose is True:
            print('HOST: Guess which door has the car behind! You can type 1, 2 or 3.\n')
            print("........\n")
        choice = input()
        while choice.strip() not in ['1','2','3']:     # This line checks whether the player's input is valid 
                                                       # and asks the player to give a valid input otherwise
            if verbose is True:
                print('HOST: There is no such a door! Choose 1, 2 or 3.\n')
            choice = input()
        choice = int(choice)
    else:
        choice = start_choice


    if verbose is True:
        print("........\n")
        print(f'HOST: You chose door {choice}!\n')
        print("........\n")    
        time.sleep(1)
        
    door_with_goats = all_doors - set([car])
    door_to_open = random.choice(list(door_with_goats - set([choice])))
    door_left = list(all_doors - set([choice]) - set([door_to_open])).pop()
    
    if verbose is True:
        print(f"*The host opens door {door_to_open}*")
        print("........\n")
        time.sleep(1)
        print(f"HOST: There is a goat behind door {door_to_open}!\n")
        print("........\n")
        time.sleep(1)
        
    if change_choice is None:
        if verbose is True:
            print(f"HOST: Do you want to change your choice from door {choice} to door {door_left}? You can type 'yes' or 'no'.\n")
            print("........\n")
        change = input()
    else:
        change = change_choice
        if verbose is True:
            print(change_choice)
    
    while change.strip() not in ['yes', 'no']:     # This line checks whether the player's input is valid 
                                                   # and asks the player to give a valid input otherwise
        if verbose is True:
            print("HOST: I can't understand your answer! Type 'yes' or 'no.\n")
        change = input() 


    if change == 'yes':
        choice = door_left
    

    if verbose is True:  
        print("........\n")          
        print(f"HOST: Your final choice is door {choice}!\n")
        print("........\n")
        time.sleep(1)
        print("........\n")
        time.sleep(1)
        print("........\n")
        time.sleep(1)

    if choice == car:
        if verbose is True:
            print("YOU WON!")
        return 1
    else:
        if verbose is True:
            print("YOU LOST!")
        return 0
    
    return start_choice

if __name__ == "__main__":    # This line is a Python idiom to run some code only when the .py file is run as a script, and not imported as a module
                              # i.e., if you import ex2a.py as a module in a different Python script, the code under "if __name__ == "__main__":" will not be executed
    monthy_hall()

