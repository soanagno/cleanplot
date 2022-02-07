from cycler import cycler
import numpy as np
import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

        
def cleanplot(X, Y, n = 40, true_scale=True, aspect=1):
    
    # plt.rc('lines', linewidth=2)
    # plt.style.use('seaborn-notebook')
    plt.rcParams['font.family'] = 'sans-serif'

    x = np.zeros((n, X.size))
    y = np.zeros((n, Y.size))

    for i in range(n):
        y[i] = Y
        if i == 0:
            x[i] = X
        else:
            x[i] = x[i-1]+10/n

    # Define top and bottom colormaps 
    c1 = cm.get_cmap('twilight_shifted', 128)  # c1
    c2 = cm.get_cmap('magma', 128)             # c2
    c3 = cm.get_cmap('viridis', 128)           # c3
    newcolors = np.vstack((c1(np.linspace(0, 1, 128)),
                        c2(np.linspace(0, 1, 128))))
                        # c3(np.linspace(0, 1, 128))))

    viridis_plasma = ListedColormap(newcolors, name='ViridisPlasma')
    # viridis_plasma = 'magma'

    cmap = plt.get_cmap(viridis_plasma)
    colors = cmap(np.linspace(0, 1, n)) # get n colors from cmap

    fig, ax = plt.subplots()
    ax.set_prop_cycle(color=colors)     # set colors to cycle prop

    for i in range(n):
        plt.plot(x[i], y[i])

    xrange = [np.min(x), np.max(x)]
    yrange = [np.min(y), np.max(y)]

    
    if true_scale == True:

        # xdif = xrange[1]-xrange[0]
        # ydif = yrange[1]-yrange[0]

        ax.set_aspect('equal', adjustable='box')

    else:
        ax.set_aspect(aspect)

    tiny = 1e-3
    plt.xlim([np.min(x), np.max(x)])
    plt.ylim([np.min(y)-tiny, np.max(y)])

    ax.tick_params(direction="in")
    plt.title('cos(θ)')
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    # plt.tight_layout()

    # save as tiff -> word document -> save as png
    fig.savefig('figure.tiff', dpi=1200)

    plt.show()



if __name__ == "__main__":

    X = np.linspace(0, 2*np.pi, 100)
    Y = np.cos(X)*2
    cleanplot(X, Y, n=40, true_scale=True, aspect=1/3)
