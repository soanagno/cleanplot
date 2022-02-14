import json
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class interface():

    def __init__(self):


        # Open JSON file
        plot_info = open("plot_info.json",)
        # returns JSON object as a dictionary
        data = json.load(plot_info)
        # Close JSON file
        plot_info.close()

        # Initialise figure
        self.fig, self.ax = plt.subplots()

        # Public
        self.dpi = data['general']['dpi']
        self.save_fig = data['general']['save_fig']
        self.saveas = data['general']['saveas']
        self.title = data['general']['title']
        self.xlabel = data['general']['xlabel']
        self.ylabel = data['general']['ylabel']
        self.font = data['general']['font']
        self.legends = data['general']['legends']
        self.cmaps = data['general']['cmaps']
        # self.cmaps = ['twilight_shifted_r', 'viridis']
        # self.cmaps = ['twilight_shifted_r', 'plasma']
        # self.cmaps = ['twilight_shifted_r', 'magma', 'inferno_r', 'twilight']
        self.ms = data['general']['ms']
        self.c_spec = data['general']['c_spec']
        # self.linestyle = [':', '-.', '--', '-']
        # self.marker = ['^', 'o', 'x', 'v']
        self.linestyle = data['general']['linestyle']
        self.marker = data['general']['marker']


    def setup(self, x, y, true_scale=True, aspect=None, domain=None, c=None):
        
        # Set specific colors
        if c != None:
            self.cmaps = c

        # Plots size
        if x.ndim == 1:
            self.n = 1
            x = x.reshape((1, -1))
            y = y.reshape((1, -1))
        elif x.ndim == 2:
            self.n = x.shape[0]

        if self.linestyle == None:
            self.linestyle = [None]*self.n
        if self.marker == None:
            self.marker = [None]*self.n

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
        colors = cmap(np.linspace(0, 1*self.c_spec, self.n)) # get n colors from cmap
        self.ax.set_prop_cycle(color=colors)     # set colors to cycle prop

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

        return x, y


    def plot(self, x, y, c=None, true_scale=False):

        x, y = self.setup(x, y, c=c, true_scale=true_scale)
        for i in range(self.n):
            self.ax.plot(x[i], y[i], linestyle=self.linestyle[i], marker=self.marker[i], ms=self.ms)

        # Save figure
        # save as tiff -> word document -> save as png
        if self.save_fig == True:
            self.fig.savefig(self.saveas, dpi=self.dpi)


    def scatter(self, x, y, c=None, true_scale=False):

        x, y = self.setup(x, y, c=c, true_scale=true_scale)
        for i in range(self.n):
            self.ax.scatter(x[i], y[i], s=3)

        # Save figure
        # save as tiff -> word document -> save as png
        if self.save_fig == True:
            self.fig.savefig(self.saveas, dpi=self.dpi)


    def show(self,):

        # Ticks and labels
        # plt.tight_layout()
        self.ax.tick_params(direction="in")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        if self.legends != None:
            plt.legend(self.legends)
        plt.show()


# Todo:
# 2d plots, 2d scatter, 2d contour
# 2d plot with points
# 3d plots, 3d scatter, 3d contour
# imshow-extend
# animations
# heatmaps
