# Week 7: Visualization

In this class, we learn how to generate plots in Python using [matplotlib](https://matplotlib.org) library. You can find many useful tutorials and code examples for matplotlib [here](https://matplotlib.org/stable/tutorials/index). 

Since we want to create and explore figures in this class, we will use Jupyter Notebook to write the solutions.

## Exercise 5.1: Gaussian random walk
A Gaussian random walk can be represented as a sum of independent Gaussian variables $X_i\sim\mathcal{N}(0,1)$:

$$S_n = \sum_{i=1}^n X_i$$

**a)** Generate $n=1000$ independent draws from the standard Gaussian distribution and plot the Gaussian random walk that they create.

**b)** Plot many (e.g. 100) independent Gaussian random walks in the same plot using only one color. You can decrease the line width and increase the plot size to improve readability of your figure. Notice that the standart deviation of $S_n$ is given by $\sqrt{n}$. Plot curves $3\sqrt{n}$ and $-3\sqrt{n}$ using a different color on the same plot. 

The output for this task may look like this:

<p align="center">
  <img src="https://raw.githubusercontent.com/mselezniova/CompMath23/fc74d9fa86ad6a78409baadc89ae1866f7649226/images/week7/ex1b.svg">
</p>

# Exercise 5.2: Bifurcation diagram

The *logistic map* generates a sequence $\{x_n\}$ using the following relation:
$$x_{n+1} = r x_n(1-x_n),$$
where $r$ is a postive constant and $x_0\in(0,1)$. The goal of this task is to plot the so-called *bifurcation diagram* of this map as a function of $r$ (also called the bifurcation parameter).

To get motivated, you can check out [this great Veritasium video](https://www.youtube.com/watch?v=ovJcsL7vyrk) about the logistic map.

**a)** Write a function that calculates the first $n$ members of the logistic map sequence, given $x_0$, $r$ and $n$.

**b)** Plot the first 100 elements of the sequence for several values of $r$, e.g. $r\in\{1.0,2.5,3.0\}$, as a line plot (i.e., using function ```plt.plot()```). You can try different values of $x_0$. What do you observe?

**c)** Now we finally plot the well-known [bifurcation diagram](https://en.wikipedia.org/wiki/Bifurcation_diagram). For values of $r$ between $0$ and $4$ with step $0.01$, calculate the first $n=1000$ elements of the sequence $\{x_n\}$. Then, for each value of $r$, plot the last $100$ values of the sequence in the same x-coordinate $r$. You can do this using a scatter plot (i.e., function ```plt.scatter()```). 

The output of this task may look like this:

<p align="center">
  <img src="https://raw.githubusercontent.com/mselezniova/CompMath23/fc74d9fa86ad6a78409baadc89ae1866f7649226/images/week7/ex2c.svg">
</p>

You can see that $x_n$ converges to a single point for $r<3$. However, for $r>3$, $x_n$ oscillates between several values. For larger values of $r$, the behavior of $x_n$ becomes chaotic.

