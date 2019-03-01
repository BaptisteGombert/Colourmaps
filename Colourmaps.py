'''
A colourmaps module 

Written by B. Gombert, March 2019
All colourmaps are created by Fabio Crameri
(http://www.fabiocrameri.ch/colourmaps.php)

I am in England as I write this so there is a 'u' in
every 'colour' word, deal with it.

'''
# Externals
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

from os.path import join,dirname
from matplotlib.colors import LinearSegmentedColormap


#class Colourmaps(object):

# ----------------------------------------------------------------------
def getCMAPnames():    
    '''
    Return colourmap names
    Return:
        # List of cmap names
    '''
    # Initialization
    cnames = ['devon','davos','oslo','bilbao','lajolla','broc',\
              'cork','vik','grayC','lisbon','tofino','berlin',\
              'turku','tokyo','lapaz','roma','oleron','acton',\
              'batlow','nuuk','bamako','hawaii','buda','imola']

    # All done
    return cnames


# ----------------------------------------------------------------------
def getdiverging():
    '''
    Return a list of only diverging cmaps
    '''

    cnames_div = ['broc','cork','vik','lisbon','tofino',\
                  'berlin','roma','oleron']

    # All done
    return cnames_div

# ----------------------------------------------------------------------
def getsequentials():
    '''
    Return a list of only sequentials cmaps
    '''

    cnames_seq = ['devon','davos','oslo','lapaz','acton','lajolla',\
                  'bilbao','grayC','tokyo','turku','bamako','nuuk',\
                  'hawaii','buda','imola','batlow']

    # All done
    return cnames_seq

# ----------------------------------------------------------------------
def printCMAP():
    '''
    Print to screen the cmap names
    '''
    print('')
    print('---- Sequential CMAPS: ----')
    print('devon - davos - oslo - lapaz - acton - lajolla')
    print('bilbao - grayC - tokyo - turku - bamako -nuuk')
    print('hawaii - buda - imola - batlow')
    print('')
    print('---- Diverging CMAPS: ----')
    print('broc - cork - vik - lisbon - tofino')
    print('berlin - roma - oleron')
    print('')

    return

# ----------------------------------------------------------------------
def getCMAP(cmap='batlow'):
    '''
    Return matplotlib cmap
    Args:   
            * cmap : name of cmap. Default is batlow
    '''
    
    # Check you didn't use a wrong cmap
    cnames = ['devon','davos','oslo','bilbao','lajolla','broc',\
              'cork','vik','grayC','lisbon','tofino','berlin',\
              'turku','tokyo','lapaz','roma','oleron','acton',\
              'batlow','nuuk','bamako','hawaii','buda','imola']
    
    assert cmap in cnames,'cmap must be in {}'.format(cnames)
    
    # Read colourmap file
    fid = join(dirname(__file__),'COLOURS','{}.txt'.format(cmap))
    cm_data = np.loadtxt(fid)

    # Create colormap object 
    cm = LinearSegmentedColormap.from_list(cmap,cm_data)

    # All done
    return cm 



# ----------------------------------------------------------------------
def plotCMAP(cmap='batlow',useviscm=True):
    '''
    Plot the CMAP, for your eyes only (and whoever is looking over your shoulder)
    Args:   
            * cmap : name of cmap. Default is batlow
            * useviscm : [True] use viscm package to plot cmap
    '''

    cm = getCMAP(cmap)
    try:      
        from viscm import viscm      
        viscm(cm)      
    except ImportError:      
        print("viscm not found, falling back on simple display")      
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',      
                   cmap=cm)      
    plt.show()   
    
    return

# ----------------------------------------------------------------------
def compareCMAPs(category=['S','D']):
    ''' 
    Make a figure showing the different colourmaps
    separated by sequentials and diverging
    Args:
            * category:    plot sequential and/or diverging?
    '''

    # Make a list
    if type(category) is not list:
        category = [category]


    # I don't why it's there, I stole it from the internet
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))

    # Get colormap names
    names_div = getdiverging()
    names_seq = getsequentials()

    # Loop on what to plot
    for cat in category:
        if cat in ['S','s','sequential']:
            names = names_seq
            title = 'Sequential colormaps'
        elif cat in ['D','d','diverging']:
            title = 'Diverging colormaps'
            names = names_div
        else:
            sys.exit('category must be "S", "D", or both')
         
        # Create figure    
        fig, axes = plt.subplots(nrows=len(names))
        fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
        axes[0].set_title(title, fontsize=14)

        # Loop in colourmaps
        for ax, name in zip(axes, names):
            cmap = getCMAP(name)
            ax.imshow(gradient, aspect='auto', cmap=cmap)
            pos = list(ax.get_position().bounds)
            x_text = pos[0] - 0.01
            y_text = pos[1] + pos[3]/2.
            fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

        # Turn off *all* ticks & spines, not just the ones with colormaps.
        for ax in axes:
            ax.set_axis_off()       

    # All done
    plt.show()
    return

# ----------------------------------------------------------------------
def compareMatplotlibCMAPs(category=['P','S','D','M','Q']):    
    '''
    Shamelessy stolent from https://matplotlib.org/examples/color/colormaps_reference.html
    '''

    # Get Pyplot already implemented colourmaps
    cmaps = {'Perceptually Uniform Sequential': [
            'viridis', 'plasma', 'inferno', 'magma'],
         'Sequential': [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn'],
         'Sequential (2)': [
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper'],
         'Diverging': [
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic'],
         'Qualitative': [
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c'],
         'Miscellaneous': [
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar']
            }
    # Define few stuffs
    nrows = max(len(cmaps[k]) for k in cmaps.keys())
    gradient = np.linspace(0, 1, 256)
    gradient = np.vstack((gradient, gradient))            

    # Make a list
    if type(category) is not list:
        category = [category]

    # Loop on what to plot
    for cat in category:
        if cat in ['S','s','sequential']:
            key = ['Sequential','Sequential (2)']

        elif cat in ['D','d','diverging']:
            key = ['Diverging']
        elif cat in ['P','p']:
            key = ['Perceptually Uniform Sequential']
        elif cat in ['M','m','Miscellaneous']:
            key = ['Miscellaneous']
        elif cat in ['Q','q','Qualitative']:
            key = ['Qualitative']        
        else:
            sys.exit('category must be "P","S","D","M","Q", or a list containing any of them')

        for cmap_category in key:
            cmap_list = cmaps[cmap_category]
            fig, axes = plt.subplots(nrows=nrows)
            fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
            axes[0].set_title(cmap_category + ' colormaps', fontsize=14)

            for ax, name in zip(axes, cmap_list):
                ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
                pos = list(ax.get_position().bounds)
                x_text = pos[0] - 0.01
                y_text = pos[1] + pos[3]/2.
                fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

            # Turn off *all* ticks & spines, not just the ones with colormaps.
            for ax in axes:
                ax.set_axis_off()

    # All done
    plt.show()
    return
