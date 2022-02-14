# import sys
# sys.path.append('.')
import numpy as np
from cleanplot import interface


cplt = interface()

def main():

    # # Create data
    # X = np.random.uniform(low=0.01, high=0.02, size=(1000,))
    # x = np.sort(X)
    # y = np.cos(1/x)/x
    # cplt.scatter(x, y, true_scale=False)
    # cplt.show()

    X = np.linspace(0, 2*np.pi, 100)
    # Y = X**2/np.cos(X)+1
    Y = np.cos(X)
    n = 40
    x = np.zeros((n, X.size))
    y = np.zeros((n, Y.size))
    for i in range(n):
        y[i] = Y
        if i == 0:
            x[i] = X
        else:
            x[i] = x[i-1]+10/n

    cplt.plot(x, y, true_scale=True)
    cplt.show()


if __name__ == "__main__":
    main()
    