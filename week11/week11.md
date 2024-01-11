# Week 11: Data Analysis

This week we practice basic data analysis tools, such as curve fitting and computing statistical characteristic of data, using [SciPy](https://scipy.org) and [Pandas](https://pandas.pydata.org) libraries.

## Exercise 1: Anscombe's quartet 

[Anscombe's quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet) consists of four small datasets that have identical simple statistical characteristics (such as mean and variance), yet have very different distributions, and look very different when plotted. The goal of this task is to investigate these datasets.

**a)** Load the datasets from `Anscombe.txt` file and store them as numpy arrays (you can use `numpy.loadtxt` function to load a text file). The file contains a matrix of 8 columns and 11 rows. Each two columns of this matrix represent $(x,y)-$coordinates of a singe dataset. 

**b)** Calculate and print statistical characteristics of all the four datasets: expected value (`np.mean`) and variance (`np.var`).

**c)** Use ```scipy.optimize.curve_fit``` to fit a straight line, i.e., a function of the form $f(x)=ax+b$, to each of the datasets. Then plot each dataset together with the corresponding fitted curve. Place all the four plots in a single figure using suplots. The output of this task should look as follows:

![](https://raw.githubusercontent.com/mselezniova/CompMath23/media/images/week11/anscombe.svg)

Notice that the lines fitted to all the datasets are the same, even though the datasets look very different!

**d)** One can see that the relationship between $x$ and $y$ is non-linear in Dataset 2. Use ```scipy.optimize.curve_fit``` to fit a quadratic function, i.e. $f(x)=a+bx+cx^2$, to this dataset, and plot the results. What do you observe? 

## Exercise 2: Irises

![](https://raw.githubusercontent.com/mselezniova/CompMath23/media/images/week11/irises.png)

[The iris flower dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set) is often used as an example for data analysis methods. This dataset contains four features: length and width of sepals and petals of iris flowers, in centimeters. There are 50 samples per each of three species of Iris (*Iris setosa*, *Iris virginica* and *Iris versicolor*). 
The goal is to distiguish between the species based on the features.

**a)** Download the `iris.csv` file and load it in Python (you can use `pandas.read_csv` function).

**b)** Get familiar with the data. You can use `df.head` and `df.tail` methods of a Pandas dataframe `df` to display first and last rows of the dataset. You can also use `df.describe` to compute basic descriptive statistics of the data.

**c)** Use ```pd.plotting.scatter_matrix``` function to plot a matrix of all the two-dimensional projections of the data together with histograms of each feature.

**d)** Now change the same figure so that points corresponding to different classes have different colors in the scatter plots. The output of this task may look like this: 

![](https://raw.githubusercontent.com/mselezniova/CompMath23/media/images/week11/irises_scatter_matrix.png)

Note that you can use the argument ```c``` of function ```pd.plotting.scatter_matrix``` to specify the color of the scatter plots' points. See the function's documentation to learn how to use this argument, and apply it to your case.

**e)** Use ```df.groupby``` to compute mean and variance of each of the four features separately for each class of irises.

**f)** Use ```df.groupby(...).boxplot``` method to generate boxplots of all the features separately for each class.