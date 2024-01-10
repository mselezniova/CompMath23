# Week 11: SymPy I

This week we start working with [SymPy](https://docs.sympy.org/latest/index.html) library for *symbolic computation*. In symbolic computation, mathematical objects are represented exactly, not approximately (recall Exercise 1 of week 9, where we implemented a class of exact rational numbers), and variables in mathematical expressions can be manipulated as abstract symbols without a given value. To get started with SymPy, you can read [this introductory tutorial](https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html).  

## Exercise 1: Symbolic calculation

**a)** Calculate the sum $1 + \dfrac{1}{2} + \dfrac{1}{3} + \dfrac{1}{4} + \dots + \dfrac{1}{100}$ as an exact fraction (i.e., in the form $\dfrac{p}{q}$) and as a decimal number. You can use ```sympy.Sum``` function to define the sum, and then use ```doit``` method to evaluate the sum symbolically, and ```evalf``` method to evaluate the sum as a floating point number.

**b)** For large $n\in\mathbb{N}$, the factorial $n!$ can be approximated with the Stirling's formula:

$$S(n) := \sqrt{2\pi n}\Bigl(\dfrac{n}{e}\Bigr)^n$$

Define $S$ as a SymPy expression and calculate the relative error given by

$$\dfrac{n! - S(n)}{n!}$$

for $n=100$ as a decimal number.

**c)** Show that the following two limits hold:

$$\lim_{n\to\infty} \dfrac{n!}{S(n)} = 1$$

$$\lim_{n\to\infty} n \Bigl( \dfrac{n!}{S(n)} - 1\Bigr) = \dfrac{1}{12}$$

To do so, define the equations above as SymPy expressions (use ```sym.Eq``` function). 

## Exercise 2: Plotting with SymPy

**a)** Consider the following sequence of functions 

$$f_n(x) = \dfrac{x}{n}\exp(-\dfrac{x}{n})$$

Plot $f_1, f_2, \dots, f_{20}$ for $x\in[0,10]$ in the same graph (use ```sympy.plot``` for plotting).

**b)** Define the function $f(x) = 1 - x^2$, and compute the expression of a tangent line that touches $f(x)$ at the point $x_0=(1/2,3/4)$. You can obtain the equation of the tangent line using Taylor expansion (```f.series``` method) at point $x_0$ up to the first-order term. Plot $f(x)$ together with the tangent line.