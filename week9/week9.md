# Week 9: Classes and objects (II)

This week, we continue the introduction into Python classes and objects, and practice using **magic** or **dunder** methods in Python. We also practice creating and importing Python **modules** or libraries. 

## Exercise 1: Rational numbers class

In this exercise, we create our own class of rational numbers. We want instances of this class to work as *exact rational numbers*, not as usual floating point numbers represented by computers. In particular, we want our rational numbers to avoid problems with precision of computations described in the Exercise 2 of Week 4. 

To achive this, we can represent a rational number $q \in \mathbb{Q}$ using two *relatively prime* integers: numerator $z$ and denominator $n$, such that $q=\frac{z}{n}$. 


**a)** Create a file called `rational_numbers.py`, where we will define our class of rational numbers. In this file, define a function `normal_form` that takes a nominator $z'$ and a denominator $n'$ as arguments and returns relatively prime numbers $z$ and $n$, such that $\frac{z'}{n'}=\frac{z}{n}$ (you can use `math.gcd` function to find the greatest common denominator of two numbers). Test this function on $q=3/2$, $q=15/3$ and $q=20/42$. 

**b)** Create a class `Rational` with attributes $z$ and $n$ (relatively prime nominator and denominator). Use the `normal_form` function to initialize a class instance given a nominator and a denominator (not necessarily relatively prime). 

**c)** Override the `__repr__` method (used to represent an object as a string for printing) to display the rational numbers as fractions using print function.

**d)** Override the addition method `__add__`. Test it on $\frac{1}{2}+\frac{1}{3}+\frac{1}{6}=1$.

**e)** Override the `__rmul__` method, which multiplies an object with an integer. Test it on $\frac{1}{2}\cdot 2 = 1$ and $\frac{1}{2} + (-1)\cdot\frac{1}{2} = 0$

**f)** Override the multiplication method `__mul__`. Test it on $\frac{1}{2}\cdot\frac{15}{2}\cdot\frac{2}{5}=1$.

**g)** Override the method `__sub__` (subtraction). Test it on $\frac{1}{2} - \frac{1}{2} = 0$.

**h)** Override the method `__float__`, which should return a floating point approximation of a rational number. Test it on $\frac{1}{2}$, $\frac{1}{3}$ and $\frac{1}{11}$.

**i)** Override the "less than" method `__lt__`, which should check whether a rational number is smaller than another one. To test this method, create a list of rational numbers with denominators $n=2,3,\dots,11$ and nominators equal to $z=n//2$ for each $n$ (here $//$ is integer division, i.e. $n//2 = \lfloor n/2 \rfloor$) and sort this list with the built-in function `sorted` (which uses the `__lt__` method internally). 


## Exercise 2: Creating an importing Python modules

**a)** Recall from the lectures that the Python idiom `if __name__ == "__main__"` allows you to execute some code only when a ```.py``` file is executed as a script, but *not when it’s imported as a module*. Use this idiom in your file `rational_numbers.py` from the previous exercise to run all the required tests of your methods only when the file is executed as a script. Now we can use the same file as a Python *module* or library, which can be imported in other Python files!

**b)** The Wallis product formula for $\pi$ is given by

$$\pi = 2\prod_{i=1}^\infty \dfrac{(2n)^2}{(2n-1)(2n+1)}$$
Then the partial products 

$$\pi_N = 2\prod_{i=1}^N \dfrac{(2n)^2}{(2n-1)(2n+1)}$$
are all rational numbers. 

Create a new Python file `wallis_product.py` and import your class of rational numbers in this file (`from rational_numbers import Rational`). In the new script, generate and print a list of the first 20 approximations of $\pi$ by the partial Wallis products. Then convert the sequence to floating point, create a numpy array out of it, and compare the values in the array to $\pi$ (i.e., ```math.pi``` or ```np.pi```) to determine the precision of the approximation at each step.





