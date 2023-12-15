# Week 10: Numeric integration and ODEs solving

In this class, we practice numeric integration and solving of ODEs using [scipy.integrate](https://docs.scipy.org/doc/scipy/tutorial/integrate.html) module. We also use [scipy.linalg.lstsq](https://docs.scipy.org/doc/scipy/reference/generated/scipy.linalg.lstsq.html) for solving a least squares problem automatically. 

## Exercise 1: SIR model

[The SIR model](https://en.wikipedia.org/wiki/Compartmental_models_in_epidemiology) is a simple mathematical model to simulate epidemics. In this model, the population is divided into three groups: **S**usceptible, **I**nfectious, and **R**emoved (recovered or dead). The size of the respective groups is given as functions of time $S(t)$, $I(t)$ and $R(t)$. It is also assumed that there is an infection rate $`\beta\in\mathbb{R}_{+}`$ and a recovery/death rate $`\gamma\in\mathbb{R}_{+}`$. Then the model is defined by the following system of differential equations:

$$\dfrac{dS}{dt} = -\beta I S, \quad \dfrac{dI}{dt} = \beta I S - \gamma I, \quad \dfrac{dR}{dt} = \gamma I$$

**a)** Solve the system of equations with initial conditions $S(0)=0.997$, $I(0)=0.03$, $R(0)=0$, and parameters $\beta=0.4$, $\gamma=0.04$, using ```scipy.integrate.solve_ivp``` function. Plot $S, I$ an $R$ over the time interval $t\in[0,100]$.

**b)** Determine the moment when the fraction of infectious individuals reaches its maximum and mark this point in the plot. 

The solution for this task may look like this:

![](https://raw.githubusercontent.com/mselezniova/CompMath23/media/images/week10/ex1.svg)

**c)**$^*$ Determine the maximal infection rate $\beta'$ such that for $\gamma=0.04$ and all $\beta\leq\beta'$ the epidemic does not break out, i.e. $I(t) < I(0)$ for any $t>0$. To do so, you can use *binary search* algorithm, described below:

1. Start with a reasonable interval $[l,r]$ for $\beta'$, e.g, $[0,0.4]$.
2. Check whether the infection is still breaking out in the center of the interval $m=(l+r)/2$ or not.
3. If the infection still breaks out, then $\beta' < m$ and we can restrict the interval to $[l,m]$. If the infection no longer breaks out, then $\beta' > m$ and we restrict the interval to $[m,r]$.
4. Repeat this procedure with the new interval until the desired accuracy is achieved (each step reduces the error by factor $1/2$).

## Exercise 2: Planetary orbits (II)

In exercise 2 of week 8, we computed possible orbits of Earth around the Sun with varying initial conditions. Our method to compute the orbits in that exercise was, in fact, an implementation of a very simple approach to numerical integration called [the Euler method](https://en.wikipedia.org/wiki/Euler_method). The Euler method is the simplest method of the class of [Runge–Kutta methods](https://en.wikipedia.org/wiki/Runge–Kutta_methods) for iterative numerical integration. As you can see in the documentation, the function ```scipy.integrate.solve_ivp``` uses Runge–Kutta methods of higher order to perform numerical integration with higher precision and much faster than we did in our naive implementation.

In this task, we will use ```scipy.integrate.solve_ivp``` to compute the Earth's orbits again. To do so, we can reformulate the ODEs governing Earth's movement as a following system of first-order equations:

$$\dot x_1 = v_1, \quad \dot x_2 = v_2, \quad \dot v_1 = -Gm^{star}\dfrac{x_1}{(x_1^2+x_2^2)^{3/2}}, \quad \dot v_2 = -Gm^{star}\dfrac{x_2}{(x_1^2+x_2^2)^{3/2}}.$$

Here $x=(x_1,x_2)$ is the position of Earth, and $v=(v_1,v_2)$ is the velocity of Earth. As before, we can set the initial conditions to $x(0) = (0,1)$ and $v(0)=(c\cdot 2\pi,0)$, where we can vary the constant $c$ to change the shape of the orbit.

**a)** Solve the ODE for a range of values of $c$ and plot the resulting orbits. You should obtain a plot identical to the one from exercise 2, week 8. Note that using the default parameters of ```scipy.integrate.solve_ivp``` in this task can lead to large accumulated computational error, so your orbits may not have a coorect shape in this case. To increase precision of your calculations, you can use the argument ```method='DOP853'``` of ```scipy.integrate.solve_ivp``` function to use Runge-Kutta method of order 8 for the numerical integration. Alternatively, you can decrease the parameter ```max_step``` (maximal time step in numerical integration) to bound the computational error. 

**b)** The velocity norm of Earth traveling along an elliptic orbit can be computed using the following formula with a certain constant C:

$$\|v\| = C\cdot\sqrt{\Bigl(\dfrac{2}{\|x\|} - \dfrac{1}{a}\Bigr)},$$

where $a$ is the *length of the semi-major axis* of the ellipse, i.e., $2a$ is the longest diameter of the ellipse. The objective of this task is to determine the value of the constant $C$. To do so, you can follow these steps:

1. Calculate an orbit as in exercise (a) using initial conditions that result in an elliptic orbit.
2. Use the solution to calculate parameter $a$.
3. Create a dataset of the form $Y=\Bigl[ \|v(0)\|, \dots, \|v(T)\| \Bigr]$ (velocity norms at different time steps), $X=\Bigl[ \bigl[\sqrt{{2}/{\|x(0)\|} - {1}/{a}}\bigr], \dots,\bigl[\sqrt{{2}/{\|x(T)\|} - {1}/{a}}\bigr] \Bigr]$. I.e., $Y$ contains the left-hand-side of the equation above, and $X$ contains the right-hand-side without the constant $C$. 
4. Use the least squares method (```np.linalg.lstsq```) to determine the value of C based on data $(X,Y)$ (i.e., you should use least squares to determine the best parameter $C$ for equation $Y=C\cdot X$).

Can you guess what is the meaning of the parameter $C$ here from the determined value?



