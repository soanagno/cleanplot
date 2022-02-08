# import sys
# sys.path.append('.')
import numpy as np
from cleanplot import interface
cplt = interface()

if __name__ == "__main__":

    X = np.linspace(0, 2*np.pi, 100)
    # Y = X**2/np.cos(X)+1
    Y = np.cos(X)*2

    n = 60
    x = np.zeros((n, X.size))
    y = np.zeros((n, Y.size))
    for i in range(n):
        y[i] = Y
        if i == 0:
            x[i] = X
        else:
            x[i] = x[i-1]+10/n

    # import cleanplot as cplt
    cplt.scatter(x, y)
    cplt.show()