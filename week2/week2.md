# Week 1: Installing Python, intro to Python 

The goal of the first exercise class is to install Python and start working with it. We will install **Miniconda**, which includes a Python distribution and a package installer called [pip](https://pypi.org/project/pip/). We will then use pip to install [numpy](https://numpy.org/install/) (a linear algebra package for Python), [Jupyter](https://jupyter.org/install), and [Spyder](https://www.spyder-ide.org) (integrated development environment for Python). We will also learn how to run Python code in different ways: in Python scripts, in Jupyter notebooks, and in Spyder. 

Below are step-by-step instructions to complete all the tasks on CIP computers, which use Linux OS. You may need to adapt the instructions if you are working with a different system.

## 1. Miniconda installation


We will install Miniconda in *command line*, or *terminal*. In terminal on CIP computers, you can use *bash* language to give commands to your computer. Just as Python, bash is a language with its own syntax. In this course, we do not focus on bash and working with Linux in general, but you will need to know some basic bash commands to navigate your file system and run programs. For now, you can just copy and paste the commands in the instructions below to install Miniconda. For later, you can read a bash tutorial for beginners under this link: [https://linuxconfig.org/bash-scripting-tutorial-for-beginners](https://linuxconfig.org/bash-scripting-tutorial-for-beginners)

The instructions to quickly install Miniconda using command line are under this link: [https://docs.conda.io/projects/miniconda/en/latest/](https://docs.conda.io/projects/miniconda/en/latest/). 

Below we explain each command of the instructions:

1. Open a terminal window. 
2. Type the following command to create a folder named "miniconda3" in your home directory: 
    
    ```bash
    mkdir -p ~/miniconda3
    ```
3. Download a Miniconda installer for Linux and save it as a file "miniconda.sh" in folder "~/miniconda3": 
    
    ```bash
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    ```
    
    The installer here is a bash script, i.e., it is a set of instructions that you can run using bash.  
4.  Run the installer using bash: 
       
       ```bash
       bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
       ```
5. Delete the installer script after the installation is complete:
    
    ```bash
    rm -rf ~/miniconda3/miniconda.sh
    ```
6. Initalize you Miniconda for bash shell (this command will let bash know the path to your miniconda and python): 
    
    ```bash
    ~/miniconda3/bin/conda init bash
    ```
8. Close and re-open the terminal window to reload bash (this is needed to aply all the changes that you made in the previous steps).
    
You can check that your installation worked by typing command ```conda``` in terminal. You can also type ```which conda``` or ```which python``` to display paths to your conda and python distributions.
    
## 2. Installing packages

You can use *pip* and *conda* package managers to install new packages on top of your python distribution. We installed both of these package managers together with Miniconda. In this class, we want to install three additional packages: [numpy](https://numpy.org/install/), [Jupyter](https://jupyter.org/install), and [Spyder](https://www.spyder-ide.org). To do so, you need to use the following commands:

1. Before installing the packages, update your conda environment:
    
    ```bash
    conda update -n base conda
    ```
2. Install numpy using pip: 
    
    ```bash
    pip install numpy
    ```
3. Install spyder using conda: 
    
    ```bash
    conda install spyder
    ```
4. Install jupyter using conda: 
    
    ```bash 
    conda install jupyter
    ``` 


## 3. Running Python code

We will use three different ways to run Python code in the class: Python scripts, Jupyter notebooks, and Spyder. Below you can find descriptions of each of these options. We will also practice them in the next classes.

### Python scripts

**What is a Python script?** Python scripts are simply ```*.py``` files, which contain a set of Python commands. Python scripts are the most basic way to run Python code.

**How to write/edit such files?** You can use a text editor (any standard editor on your computer
would work but there are also editors made specifically for code, such as [Sublime]()) or a Python IDE
(e.g. PyCharm or Spyder).

**How to run a script?** To run a Python script, you can simply type ```python script_name.py``` in
a terminal window. 

**How are scripts executed?** Python scripts are executed *linearly*, i.e. all the code contained in the scripts simpy runs in the order in which the script contains it. You cannot run or display output of only selected parts of the code.

### Jupyter notebooks

**What is a Jupyter notebook?** Jupyter notebooks are ```*.ipynb``` files that contain both Python code and rich text elements (e.g. figures, equations, formatted text, etc.). Unlike scripts, Jupyter notebooks are designed to be easily readable for people, and they are often used in presentations or tutorials. However, they are not a good choice for implementing complex coding projects.

**How to write/edit such files?** Jupyter notebooks are run by Jupyter Notebook App, which we installed today. This app allows creating, running, and editing notebooks *in web browser*. You can run notebooks locally on your desktop *without internet access* (we will do so in this class). It is also possible to run a notebook on a remote server and access in through the internet. 

**How to run a notebook?** You can launch Jupyter Notebook App by typing ```jupyter notebook``` in a terminal window. Within the app, you can create, edit, and run notebooks using the graphic interface. We will practice this in class.

**How are notebooks executed?** In Jupyter notebooks, you can have multiple code cells, which can be run individually. You do not have to run all the code in the notebook at once. However, all the variables, objects, functions, etc., which you create or change in a cell that you run, will be accessible or change in all the other cells. In other words, all the cells in a notebook share memory.

### Spyder 

**What is Spyder?** Spyder is an interactive delevopment environment (IDE) for Python. In general, IDEs are a good choice for complex coding projects that may contain multiple scripts, and need code analysis and debugging.
Spyder, in particular, is designed for scientific computing, and combines typical IDE features with interactivity similar to Jupyter notebooks (displaying figures, running parts of code, etc.). In Spyder, you can create and edit ```*.py``` files with Python code.

**How to write/edit code in Spyder?** You can launch Spyder by typing ```spyder``` in a terminal window. Note that a Spyder distribution has to be linked to a Python distribution on your conmputer. If you have multiple Python distributions installed, make sure you run Spyder with the right version. 

**How to run code in Spyder?** You can use the graphic inteface to run code in Spyder. We will practice this in class. 

**How is code executed in Spyder?** You can run code linearly (as a script) in Spyder, but you can also choose to run separate parts of the code, and separate code into cells, as in Jupyter notebook. 

---
### Additional resources
* A comprehensive Python tutorial: [https://docs.python.org/3/tutorial/](https://docs.python.org/3/tutorial/ ) 
* Jupyter tutorial: [https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html)
* Spyder tutorial: [https://docs.spyder-ide.org/current/quickstart.html](https://docs.spyder-ide.org/current/quickstart.html)