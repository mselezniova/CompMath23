# Week 5: Functions, cycles, if/else operators

In this exercise class, we practice using Python **functions**, **cycles**, and **if/else** operators. We also get even more comfortable with printing and string formatting. As in the last week, you need to write a separate Python script for each exercise.

If you want to recall something or learn more about the topics of this class, you can check these parts of the (very long) Python tutorial:

* **Control flow tools** (for, if, etc.; only sections 4.1-4.6): [https://docs.python.org/3/tutorial/controlflow.html](https://docs.python.org/3/tutorial/controlflow.html)
* **Functions**: [https://docs.python.org/3/tutorial/controlflow.html#defining-functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
* **Python data structures** (lists, sets, dictionaries, etc.): [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)
* **Printing and string formatting**: [https://docs.python.org/3/tutorial/datastructures.html](https://docs.python.org/3/tutorial/datastructures.html)

## Exercise 1: Prime numbers

**a)** Write a function that tests if a number is prime. Test your function on several simple examples of prime and nonprime numbers, e.g., 17, 28, 131, 1573.

**b)** Write a function that returns factorization of an integer, i.e., all the prime factors and their multiplicities, as a *dictionary*. Test your function on several numbers, e.g., 17, 28, 131, 1573. 

An example of factorization output for number $28=2^2*7^1$ can look like this:

```The factors of 28 are: {2: 2, 7: 1} ```

**c)$`^*`$** You can measure how much time it takes to run some code using ```time.time()``` function from ```time``` library. For example, you can measure and print how much time it takes to run function ```is_prime``` with input ```n``` using the following code snippet:

```python
start = time.time()
is_prime(n) 
end = time.time()
print(f"Time to check if {n} is prime: {end - start}")
```

Try to time your functions from exercises a) and b) on some larger prime and nonprime numbers, e.g., 526891377 (nonprime) and 479001599 (prime). This may take a while if your implementations are not optimal. However, a good implementation takes just fractions of a second for these numbers. Do you have any ideas how to make your implementations in a) and b) more efficient?

## Exercise 2: Let's Make a Deal!
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Monty_open_door.svg/440px-Monty_open_door.svg.png">
</p>

**a)** Write a text-based game that simulates the famous [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem):

*The **player** is on a show and has to choose one out of three doors: Behind one door is a car; behind the others, goats. The game goes like this:*

- *The player picks a door, say No. 1.*
- *The **host** (who knows what's behind the doors) opens another door, say No. 3. This is always a door that has a goat behind.*
- *The host then asks the player, "Do you want to pick door No. 2 instead?" (i.e., if the player wants to change the initial choice).*
- *The player answers "Yes" or "No".*
- *The host opens the door of choice and reveals if the player won or lost the game.*

In this task, you can use in-built Python method ```input()``` to record the player's responses. For example, the following code snippet asks the player to type a door number (1, 2 or 3), and saves the player's response in variable ```choice```:
```python
print("HOST: Guess which door has the car behind! You can type 1, 2 or 3.\n")

choice = input()
```
And an example of the game's full output in the terminal can look like this:
```bash
HOST: Guess which door has the car behind! You can type 1, 2 or 3.

........

1
........

HOST: You chose door 1!

........

*The host opens door 3*
........

HOST: There is a goat behind door 3!

........

HOST: Do you want to change your choice from door 1 to door 2? You can type 'yes' or 'no'.

........

yes
........

HOST: Your final choice is door 2!

........

*The host opens door 2*

........

HOST: YOU LOST!
```

**b)$`^*`$** Run two following scenarios of the game automatically many times:

1. The player starts with a random choice and then decides not to change the initial choice.
2. The player starts with a random choice and then decides to change the initial choice.

Estimate the probability of winning the game in both scenarios using your results. Which of the two strategies is better?

In this task, you can use ```random.choice()``` function from module ```random``` to choose a random element out of a list as follows:

```python
start_choice=random.choice([1,2,3])
```

---
Image from: [https://en.wikipedia.org/wiki/Monty_Hall_problem#/media/File:Monty_open_door.svg](https://en.wikipedia.org/wiki/Monty_Hall_problem#/media/File:Monty_open_door.svg)
