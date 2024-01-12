# Week 12: SymPy I

This week we start working with [SymPy](https://docs.sympy.org/latest/index.html) library for *symbolic computation*. In symbolic computation, mathematical objects are represented exactly, not approximately (recall Exercise 1 of week 9, where we implemented a class of exact rational numbers), and variables in mathematical expressions can be manipulated as abstract symbols without a given value. To get started with SymPy, you can read [this introductory tutorial](https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html).  

## Exercise 1: Basic operations with SymPy

**a)** Use SymPy to factor the following polynomial:
$$2x^5 - 19x^4 + 58x^3 - 67x^2 + 56x - 48$$

**b)** Implement a function ```uparrow(x, n)```, where $x$ is a SymPy symbol and $n$ is an integer, which returns

$${\underbrace{x^{{}^{.^{.^{.^x}}}}}_\text{n copies of x}}$$

as a SymPy expression. Use the function with argument $n=4$ to define the following expression: 

$$x^{{}^{x^{x^{x}}}}$$

Then calculate the value of the above expression symbolically for $x=2$ (use ```subs``` method). 

**c)** Implement a function ```compose(f,n)```, which composes a SymPy expression $f$ with itself $n$ times, i.e., returns ${\underbrace{f(f(\dots f(x))\dots )}_\text{n copies of f}}$. Test your function using expression $f(x)=x^2$ and $n=5$.

**d)** Consider the following sequence of functions 

$$f_n(x) = \dfrac{x}{n}\exp(-\dfrac{x}{n})$$

Plot $f_1, f_2, \dots, f_{20}$ for $x\in[0,10]$ in the same graph (use ```sympy.plot``` for plotting).
