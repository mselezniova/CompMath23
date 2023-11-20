# Week 6: First steps with NumPy

This week we begin working with [NumPy](https://numpy.org), which we will use extensively in all the future classes. NumPy is a Python library for linear algebra and scientific computing. You can have a look at ["NumPy: the absolute basics for beginners"](https://numpy.org/doc/stable/user/absolute_beginners.html) guide to get familiar with the basic concepts of NumPy. 

In this and the next classes, you will use many new functions from NumPy and other Python libraries. For each of these functions, you will need to learn how it works: what it does, what parameters it takes, what type of output it produces, etc. This information is usually available in the function's *documentation*. You can google to find the documentation for a given function, but you can also use the Python's **help utility**, which you can call using ```help()``` function. For example, command ```help(np.sin)``` will display the documentation of ```np.sin()``` function, which computes sinus of a numpy array. You can also call the help function for any other Python object, or for the whole library (e.g., ```help(numpy)```). 

Reading documentation is one of the most important skills in programming, and we encourage you to practice it. So next time you want to ask a question about a Python function/package/etc., first try to check that the easiest answer is not "RTFM".

## Exercise 4.1: Say "No" to loops! 

Python loops are famously slow, so it is not a good idea to use them in large-scale computations. Fortunately, NumPy offers *vectorization*, [*indexing*](https://numpy.org/doc/stable/user/basics.indexing.html), and [*broadcasting*](https://numpy.org/doc/stable/user/basics.broadcasting.html) as tools to elliminate loops in your code! 

In this task, you need to generate the following sequences/vectors/matrices with ```numpy``` *without using loops*:

**a)** $\bigl(\sin(\pi n)\bigr)_{n=1,\dots,12}$

**b)** $\bigl( \frac{1}{1+n^2} \bigr)_{n=1,\dots,12}$

**c)** $(1,-3,5,-7,9,\dots,97,-99)$

**d)**$^*$ The matrix

$$\begin{pmatrix}
1/z & 1 & 1 & \dots & 1\\
z & 1/z & z & \dots & z\\
\vdots & & & \dots & \\
z^{11} & z^{11} & z^{11} & \dots & 1/z
\end{pmatrix},$$
where $i$ is the imaginary unit, and $z:=\frac{\sqrt{3}+i}{2}$.

## Exercise 4.2: Least squares

The ordinary least squares problem with matrix of observations $X\in\mathbb{R}^{N\times p}$ and vector of responses $y\in\mathbb{R}^N$ is given by

$$\min_{w\in\mathbb{R}^p} \|Xw-y\|_2^2$$

and has a well-known analytical solution (assuming that $X$ has full column rank):

$$w^* = (X^TX)^{-1}X^T y$$

Write a function that takes $X$ and $y$ as input and returns the solution of the ordinary least squares problem. Generate some arbitrary matrix $X$  and vector $y$ (such that $N>p$, and $X$ has a full column rank) and check if your function returns the right solution on these inputs (i.e., if it holds that $Xw^*-y=0$ up to a small constant).

## Exercise 4.3: The shortest mathematics paper

A [candidate for the shortest mathematics paper ever published](https://www.ams.org/journals/bull/1966-72-06/S0002-9904-1966-11654-3/S0002-9904-1966-11654-3.pdf) shows the following result:

\begin{equation}
27^5+84^5+110^5+133^5=144^5\tag{*}
\end{equation}

This is a counterexample to the [Euler's sum of powers conjecture](https://en.wikipedia.org/wiki/Euler%27s_sum_of_powers_conjecture), which states that if the sum of $n$ many $k-$th powers of positive integers is itself a $k-$th power, then $n\geq k$.

**a)** Check if equation (*) is true.

**b)** The more interesting statement in the paper is that the equation above gives the smallest counterexample, i.e., for any five integers smaller than $144$ denoted $a,b,c,d$ and $e$, it does not hold that $a^5+b^5+c^5+d^5=e^5$. Check this statement using Python.

Notice that the number of all the possible combinations of four integers $a,b,c,d$ smaller than $N$ grows very quickly with $N$:

$$\binom{N}{4} = \frac{N(N-1)(N-2)(N-3)}{24} = O(N^4)$$

In particular, there are around 17 million combinations for $N=144$. Therefore, you need to mind efficiency and memory issues while solving this task. You can, for example, follow this algorithm:

1. Construct a ```numpy``` array of integers from 1 to 144 raised to the fifth power.
2. Construct a list (or an array) of all combinations of four elements from this array. You can use ```combinations``` function from ```itertools``` package for this.
3. Construct a list (or an array) of sums of all these combinations.
4. Loop over the list of sums and check if the entry appears in the list from step 1.

**c)**$^*$ The last loop may still take some time in the proposed algorithm. Can you find a more efficient solution using ```numpy``` to avoid the loop? Hint: You can use ```np.isin``` function. 




