# Week 8: Classes and objects


This week we start working with Python **classes**, which allow to create new *types* of objects. To learn more about Python classes, as well as *namespaces* and *scopes*, you can read [this chapter of The Python Tutorial](https://docs.python.org/3/tutorial/classes.html).

## Exercise 1: Astronomical bodies

In this task, we will create three classes representing astronomical bodies: *parent class* ```Body``` for general astronomical bodies, and its *child classes* ```Planet``` and ```Star```.

**a)** Create a class ```Body``` that has two arguments: ```position``` and ```velocity```. Both arguments should be given values during initialization of a class instance (i.e., in function ```__init__```).

**b)** Create a class ```Star``` as a child class of ```Body```. This class should inherit all the arguments of its parent, and also have three additional arguments: ```name``` (name of the star), ```mass``` and ```radius```. All the arguments should be given values during initialization of a class instance.

**c)** Create a class ```Planet``` as a child class of ```Body```. This class should inherit all the arguments of its parent, and also have three additional arguments: ```name``` (name of the star), ```mass``` and ```radius```. All the arguments should be given values during initialization of a class instance.

**d)** Add a method ```info()``` to the ```Planet``` class. This method should print information about the planet: its name, mass, and radius. You can also add a similar method to the ```Star``` class to print the information about a star.

## Exercise 2 $^*$: Planetary orbits

In this task, we will (approximately) compute trajectories that Earth can follow while orbiting the Sun. Since planetary orbits lie on a plane, we will consider the motion of Earth in just two dimensions. To simplify the problem as much as possible, we will consider the motion of Earth as a [one-body problem](https://en.wikipedia.org/wiki/Classical_central-force_problem), where Earth is accelerated by the gravitational force of the Sun, but the Sun itself is motionless. This approximation gives reasonable results in our case since the mass of the Sun is much larger than the mass of Earth. On the other hand, if the masses of two bodies are comparable, one would need to implement the [two-body problem](https://en.wikipedia.org/wiki/Two-body_problem) instead, which is a bit more complex (you can do it if you are really motivated). 

To avoid giant numbers and overflows, we will use *astronomical units* instead of usual SI units in this task. This means that we will measure time in *years* ($yr$) instead of seconds, distances in *astronomical units* ($AU$) instead of meters, and mass in *solar masses* ($SM$) instead of kilograms. Here $1 AU$ is the average distance between the Sun and Earth, and $1 SM$ is equal to the mass of the Sun.

**a)** Add methods ```update_position``` and ```update_velocity``` in the class ```Body```. 

The method ```update_position``` should take a time step ```dt``` as argument and update the body's position using the body's current velocity as follows:

$$x_{new} = x + v\cdot dt,$$

where $x$ is the current position, $v$ is the current velocity, and $x_{new}$ it the new updated value of the position. 

The method ```update_velocity``` should take a time step ```dt``` and acceleration ```a``` as arguments and update the body's velocity as follows:

$$v_{new} = v + a\cdot dt,$$

where $v$ is the current velocity, and $v_{new}$ it the new updated value of the velocity. 

**b)** Create an instance of the class ```Star``` that represents the Sun and an instance of the class ```Planet``` that represents Earth. 

In  astronomical units, the mass of the Sun is equal to $1 SM$, and its radius is $\approx 4.7\cdot 10^{-3} AU$. Since the Sun is motionless, we can set it's initial velocity as $v^{Sun}_0 =(0,0)$, and place the Sun in the origin of the coordinate system (i.e., set the initial position as $x^{Sun}_0=(0,0)$).

The mass of Earth in astronomical units is $\approx 3\cdot 10^{-6}SM$, and its radius is $\approx 4.3\cdot 10^{-5}AU$. You can set the initial coordinate of Earth as $x_0^{Earth}=(0,1)$ (i.e., Earth is $1AU$ away from the Sun), and the initial velocity as $v_0^{Earth}=(2\pi,0)$. Notice that if Earth revolves around the sun in a circular orbit with velocity $2\pi AU$, then it makes exactly one circle in one year.

**c)** Add a method ```gravitational_force``` to class ```Planet```. This method computes the gravitational force vector that acts on the planet in the gravitational field of a given star. The gravitational force is given by

$$F = - G\dfrac{m^{planet}m^{star}}{\|x^{planet} - x^{star}\|^2}\cdot\dfrac{x^{planet} - x^{star}}{\|x^{planet} - x^{star}\|},$$

where $m^{planet}$ and $x^{planet}$ are the mass and the position of the planet, and $m^{star}$ and $x^{star}$ are the mass and the position of the star. Here $G=4\pi^2$ is the gravitational constant given in the astronomical units $(AU^{3}yr^{-2}SM^{-1})$.

**d)** Add a method ```compute_orbit_step``` to the class ```Planet```. This method takes time step ```dt``` and ```star``` as arguments, and changes the position and the velocity of the planet as if the planet is in the gravitational field of the ```star```. In other words, you need to calculate the planet's acceleration as follows:

$$a^{planet} = F/m^{star},$$

where $F$ is the gravitational force between the star and the planet. And then apply the following changes to the planet's position and velocity (use methods ```update_position``` and ```update_velocity``` of the parent class ```Body``` here):

$$x^{planet}_{new} = x^{planet} + v^{planet}dt,$$
$$v^{planet}_{new} = v^{planet} + a^{planet}dt.$$

**e)** Compute the Earth's orbit with the given initial conditions for 10 years ahead and plot the trajectory. To avoid large accumulated computational error, use small values of ```dt```, e.g., $10^{-5}$. Try slightly changing the initial velocity of Earth and observe how the orbit changes (changing the velocity too much may lead to computational errors though). The plot generated in this task may look like this:

<p align="center">
  <img src="https://raw.githubusercontent.com/mselezniova/CompMath23/a80dba28d25d1e11fdfaea7f4f15a63724d538a3/images/week8/ex2.svg">
</p>

You can see that initial velocity such that $\|v_0\|=2\pi$ gives a circular orbit, while slightly larger or smaller velocities create eliptic orbits. When the initial velocity becomes too large, the trajectory becomes hyperbolic, i.e., the planet escapes the orbit of the star. 


