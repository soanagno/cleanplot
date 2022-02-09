from cycler import cycler
import numpy as np
import matplotlib as mpl
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class interface():

    def __init__(self):


        # Initialise figure
        self.fig, self.ax = plt.subplots()

        # Public
        self.dpi = 1200
        self.save_fig = True
        self.saveas = 'figure.tiff'
        self.title = 'cos(θ)'
        self.xlabel = 'x axis'
        self.ylabel = 'y axis'
        self.font = 'sans-serif'
        # self.cmaps = ['r', 'b']
        # self.cmaps = ['twilight_shifted_r', 'viridis']
        self.cmaps = ['twilight_shifted_r', 'plasma']
        # self.cmaps = ['twilight_shifted_r', 'magma', 'inferno_r', 'twilight']
        self.ms = 4
        self.c_spec = 1
        # self.linestyle = [':', '-.', '--', '-']
        # self.marker = ['^', 'o', 'x', 'v']
        self.linestyle = None
        self.marker = None


    def setup(self, x, y, true_scale=True, aspect=None, domain=None):
        
        # Plots size
        n = x.shape[0]

        if self.linestyle == None:
            self.linestyle = [None]*n
        if self.marker == None:
            self.marker = [None]*n

        # Parameters
        # plt.rc('lines', linewidth=2)
        # plt.style.use('seaborn-notebook')
        plt.rcParams['font.family'] = self.font

        # Define colormap stack
        mapstack = []
        for i in range(len(self.cmaps)):
            try:
                mapstack.append(cm.get_cmap(self.cmaps[i], 128))
            except:
                continue
        try:
            newcolors = mapstack[0](np.linspace(0, 1, 128))
            for i in range(1, len(self.cmaps)):
                newcolors = np.vstack((newcolors, mapstack[i](np.linspace(0, 1, 128))))
        except:
                newcolors = self.cmaps

        # Create custom map instance
        customap = ListedColormap(newcolors, name='customap')
        cmap = plt.get_cmap(customap)
        colors = cmap(np.linspace(0, 1*self.c_spec, n)) # get n colors from cmap
        self.ax.set_prop_cycle(color=colors)     # set colors to cycle prop

        # # Plot graphs
        # for i in range(n):
        #     plt.plot(x[i], y[i])

        # Define domain dimensions
        if domain == None:
            xrange = [np.min(x), np.max(x)]
            yrange = [np.min(y), np.max(y)]
        else:
            if len(domain) == 2:
                xrange = [domain[0], domain[1]]
                yrange = [np.min(y), np.max(y)]
            elif domain[0] == 0 and domain[1] == 0:
                xrange = [np.min(x), np.max(x)]
                yrange = [domain[2], domain[3]]
            else:
                xrange = [domain[0], domain[1]]
                yrange = [domain[2], domain[3]]
        xdif = xrange[1]-xrange[0]
        ydif = yrange[1]-yrange[0]

        # Set dimensions
        tiny = np.abs(ydif)*1e-3  # req. for bottom y-tick
        plt.xlim([xrange[0], xrange[1]])
        plt.ylim([yrange[0]-tiny, yrange[1]])

        # Define scaling
        if true_scale == True:
            self.ax.set_aspect('equal', adjustable='box')
        elif aspect != None:
            self.ax.set_aspect(aspect*xdif/ydif)

        # Ticks and labels
        # plt.tight_layout()
        self.ax.tick_params(direction="in")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)


    def plot(self, x, y):

        # Plots size
        n = x.shape[0]

        self.setup(x, y)
        for i in range(n):
            plt.plot(x[i], y[i], linestyle=self.linestyle[i], marker=self.marker[i], ms=self.ms)

        # Save figure
        # save as tiff -> word document -> save as png
        if self.save_fig == True:
            self.fig.savefig(self.saveas, dpi=self.dpi)


    def scatter(self, x, y):

        # Plots size
        n = x.shape[0]

        self.setup(x, y)
        for i in range(n):
            plt.scatter(x[i], y[i], s=3)

        # Save figure
        # save as tiff -> word document -> save as png
        if self.save_fig == True:
            self.fig.savefig(self.saveas, dpi=self.dpi)


    def show(self,):
        plt.show()


    def forceAspect(ax, aspect=1):
        im = ax.get_images()
        extent = im[0].get_extent()
        ax.set_aspect(abs((extent[1]-extent[0])/(extent[3]-extent[2]))/aspect)

# Todo 
# 2d plots, 2d scatter, 2d contour
# 2d plot with points
# 3d plots, 3d scatter, 3d contour
# imshow-extend
# animations
# heatmaps
