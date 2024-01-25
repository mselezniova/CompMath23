# Week 14: SymPy III (Matrices)

This week we continue working with [SymPy](https://docs.sympy.org/latest/index.html) library for symbolic computation.

## Exercise 1: Linear equation

**a)** Define the following matrix in Sympy:

$$A = \begin{pmatrix}
2 & -1 & \alpha \\
-1 & 2 & -1 \\
\alpha & -1 & 2 
\end{pmatrix}$$

**b)** Compute the determinant of $A$ and factorize it as a polynomial of $\alpha$. 

**c)** Notice that $A$ is positive definite according to  Sylvester's criterion iff its determinant is positive, since the first two leading principal minors are positive. Use Sympy's ```solveset``` function to find when the determinant of $A$ is positive.

**d)** Set $\alpha=1$ and solve a linear equation $Ax=b$ for $x$, where $b=[2,4,6]$.

## Exercise 2: Gambler's Ruin

Consider the following two-player game: Alice and Bob toss a fair coin. In case of heads, Alice gets one euro from Bob, otherwise Bob gets one euro from Alice. Alice starts with 2 euros. The game ends if Alice has 4 euros or if she has lost all the money. 

This game can be illustrated by the following state graph, where the states' numbers indicate how much money Alice currently has, and the weights of arrows indicate the transition probabilities.

![](https://raw.githubusercontent.com/mselezniova/CompMath23/media/images/week14/game.png)

**a)** Create the transition matrix of the game $M$, where $M_{i,j}$ is the probability to transition from state $i$ to state $j$.

**b)** The matrix power $M^t$ gives the transition probabilities after $t$ rounds. Determine $M^\infty = \lim_{t\to\infty} M^t$.

*Hint: You can diagonalize $M$ and find the limit of powers of the the diagonal matrix components.*

**c)** Determine the probability that Alice will go bankrupt. To do so, create a vector $v=[0,0,1,0]$ and calculate $vM^\infty$.

**d)** What happens with the probability of bankruptcy if the game ends not when Alice has 4 euros but when she has 5 or 6 euros?

