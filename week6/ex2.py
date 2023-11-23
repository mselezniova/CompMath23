import numpy as np

def OLS(X,y):
    return np.linalg.inv(X.T@X)@X.T@y # np.linalg.inv computes the inverse of a matrix

N = 100
p = 10

X = np.random.normal(size=(N,N)) # generate random gaussian matrix of shape (N,N)
y = np.random.normal(size=(N,1)) # generate random gaussian vector of shape (N,1)

w = OLS(X,y)


print(f"Xw-y={np.linalg.norm(X@w - y)}")



