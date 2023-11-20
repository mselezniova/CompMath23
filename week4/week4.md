# Week 4: Arithmetics in Python

In this exercise class, your goal is to write *a separate Python script* (i.e, a ```*.py``` file) for each of the two exercises. Each script has to print solutions for each part of the exercise, e.g., like this:

```python
print(f"The solution to exercise 1a) is {sol}")
```

where ```sol``` is the value of your solution. You can use the materials of the previous exercise class to recall how to write, edit, and execute Python scripts.

## Exercise 1: Arithmetics 
Using functions and constants from the ``math`` library, solve the following tasks:

**a)**  Calculate $|\pi^e-e^\pi|$.

**b)** Calculate $\sqrt{n + \sqrt{n}} - \sqrt{n - \sqrt{n}}$ for $n=1000$.

**c)** Stirling's formula approximates the factorial for large $n$ as follows:

$$n! \approx S = \sqrt{2\pi}n^{n+1/2}e^{-n}$$

Calculate $S$ for $n\in\{5,10,15,20\}$ and compare with the value of $n!$ given by the ``math`` library function.

## Exercise 2: Floating point numbers 

Computers represent real numbers as binary (base 2) fractions. For example, a decimal number ```0.625``` is represented as $`0*2^{0}+1*2^{-1}+0*2^{-2}+1*2^{-3}`$, which gives a binary fraction ```0.101```. Since most real numbers cannot be represented *exactly* as a *finite* binary fraction, computers cannot represent real numbers perfectly. This can lead to problems with accuracy of machine calculations. The goal of this exercise is to demonstrate limitations of the floating point arithmetics used in computers. You can read more about how floating point numbers are represented by computers, and issues of the floating point arithmetics, in this chapter of the Python tutorial: [https://docs.python.org/3/tutorial/floatingpoint.html](https://docs.python.org/3/tutorial/floatingpoint.html)

**a)** Calculate and print the value of the experssion ```0.3+0.3+0.3``` in Python. Is the output correct? Try comparing the output value with the correct aswer, e.g., as follows: 

```python
print(0.3+0.3+0.3==0.9)
``` 
(returns True or False)

**b)** Define the following variables:

$$x = 1,\quad y = 1 + 10^{-16}\sqrt{3}.$$

In exact arithmetics, it should then be true that:

$$10^{16}(y-x) = \sqrt{3}.$$

Check how accurately this equation holds in Python. To do so, you can calculate the left hand side and the right hand side separately, and then print the difference between the two.

**c)** Roots of a quadratic polynom 

$$x^2 - 2px + q$$ 

can be found using the formula 

$$x_{1,2} = p \pm \sqrt{p^2-q}$$

Alternatively, one can calculate only $x_1$ and then find $x_2$ using Vieta's formula:

$$x_2 = \dfrac q x_1$$

Consider a quadratic polynom with $q=1$ and $p=(a+1/a)/2$. The correct roots of this polynom are given by $a$ and $1./a$. Calculate the roots of the polynom using the two methods described above for two values of $a$: $a=2$ and $a=100$. How do the results of the two methods compare? Which method gives (more) correct results?
