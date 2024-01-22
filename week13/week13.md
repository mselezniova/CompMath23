# Week 13: SymPy II

This week we continue working with [SymPy](https://docs.sympy.org/latest/index.html) library for symbolic computation.

## Exercise 1: Symbolic calculation

**a)** Calculate the sum $1 + \dfrac{1}{2} + \dfrac{1}{3} + \dfrac{1}{4} + \dots + \dfrac{1}{100}$ symbolically as an exact fraction, and also as a floating point number. You can use ```sympy.Sum``` function to define the sum, then use ```doit``` method to evaluate the sum symbolically, and ```evalf``` method to evaluate the sum as a floating point number.

**b)** For large $n\in\mathbb{N}$, the factorial $n!$ can be approximated with the Stirling's formula:

$$S(n) := \sqrt{2\pi n}\Bigl(\dfrac{n}{e}\Bigr)^n$$

Define $S$ as a SymPy expression and calculate the relative error given by

$$\dfrac{n! - S(n)}{n!}$$

for $n=100$ as a floating point number.

**c)** Show that the following two limits hold:

$$\lim_{n\to\infty} \dfrac{n!}{S(n)} = 1$$

$$\lim_{n\to\infty} n \Bigl( \dfrac{n!}{S(n)} - 1\Bigr) = \dfrac{1}{12}$$

To do so, define the equations above as SymPy expressions (use ```sym.Eq``` function). 


**d)** Define the function $f(x) = 1 - x^2$, and compute the expression of a tangent line that touches $f(x)$ at the point $x_0=(1/2,3/4)$. You can obtain the equation of the tangent line using Taylor expansion (```f.series``` method) at point $x_0$ up to the first-order term. Plot $f(x)$ together with the tangent line.

**e)** The Gaussian density function is given by 

$$f(x) = \dfrac{1}{\sigma\sqrt{2\pi}}e^{-\dfrac{1}{2}\Bigl(\dfrac{x-\mu}{\sigma}\Bigr)^2}$$

Define $f(x)$ as a SymPy expression. Note that you need to specify that $\sigma$ is positive in the above expression. Compute the expectation and the variance of the Gaussian distribution using integrals of $x\cdot f(x)$ and $x^2 \cdot f(x)$.

## Exercise 2: SIS model

An alternative to the SIR model of epidemics, which we studied in Exercise 1 of week 10, is the [SIS model](https://de.wikipedia.org/wiki/SIS-Modell). In SIS model, an individual does not become immune after recovering from an infection but becomes susceptible again. Thus, there are only two states: $S$ (susceptible) and $I$ (infectious). As before, there are also two hyperparameters: infection rate $\beta$ and recovery/death rate $\gamma$. Then the differential equations system describing the model is given by

$$\dfrac{dS}{dt} = -\beta IS + \gamma I, \quad \dfrac{dI}{dt} = \beta IS - \gamma I$$

We further assume that $I+S = 1$ and denote $\delta := \beta-\gamma$. Then the above system simplifies to the following single ODE:

$$\dfrac{dI}{dt} = (\delta - \beta I) I$$

**a)** Obtain a general solution of the ODE using ```sympy.dsolve``` function. The general solution will depend on a constant $C_1$, which can be specified using initial conditions. 

**b)** Incorporate the initial condition $I(0) = I_0$ into the general solution. As a result, you should obtain the ODE solution as a function of $I_0$. To do this, you can compute the general solution at $t=0$ and solve the equation $I(0) = I_0$ for the constant $C_1$.

**c)** Check that $1-I(t)$ satisfies the equation for $S(t)$.

**d)** The number of infectious individuals $I(t)$ will approach a stable point (equilibrium) over time. Determine the limit of $I(t)$ as $t\to\infty$. You need to consider two cases separately here: 1) $\delta>0$, 2) $\delta\leq 0$.

**e)** Plot the solutions $S(t), I(t)$ over $t\in[0,100]$ for $\beta=0.4$, $\gamma=0.04$, and initial conditions $S(0)=0.997$, $I(0)=0.03$. 