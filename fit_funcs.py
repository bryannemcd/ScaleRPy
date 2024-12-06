"""
Contains ridge-finding and fitting functions for SpatGalDat objects

Created by Bryanne McDonough 12/5
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from scipy.optimize import curve_fit
import numpy.ma as ma
import math

def find_ridge(self, x, y, xrange = None, yrange = None, numxbins=40, numybins=40, fittype='max'):
    """
    This function creates a ridge line fit by constructing a 2D histogram of the x and y data, 
    identifying the "ridge" of the data (the value of y where the most spaxels are in a given column of x), 
    and performing a fit to those ridge points.

    x: a 1D array of length N containing the x values for the spatially resolved relationship (e.g., stellar mass surface density for N spaxels)
    y: a 1D array of length N the y values for the spatially resolved relationship (e.g., SFR surface density for N spaxels)
    xrange: the range in x that the scaling relation fit should be performed over; should exclude outlying data
    yrange: the range in y that the scaling relation fit shoudl be performed over; should exclude outlying data
    numxbins: the number of bins the x data will be divided into. Smaller bins are recommended for smaller data samples
    numybins: the number of bins the y data will be divided into
    fittype: the type of ridgeline fit to perform, the options are currently 'max' or 'Gauss'
        max (default) - from a 2D histogram, the fit will be done to the max value of a given column
        Gaussian - from a 2D histogram, a Gaussian will be fit to each column to obtain the max value with errors, 
                    and then the scaling relationship fit will be done to those max values


    Assumes spaxel sample has already been reasonably cleaned to remove spaxels with e.g., low mass surface density (<10^6 M_sun/kpc^2)
    """

    if xrange is None: xrange=(min(x), max(x))
    if yrange is None: yrange=(min(y), max(y))
    
    histfig,ax=plt.subplots()

    xbin=np.linspace(xrange[0], xrange[1], num = numxbins)
    ybin=np.linspace(yrange[0], yrange[1], num= numybins)

    #construct 2D histogram from data
    hist,xedges,yedges,image=ax.hist2d(x,y,bins=(xbin,ybin),
        norm=colors.LogNorm(),cmin=1,cmap=plt.cm.RdYlBu) #cmin=1 to exclude any bins without spaxels

    #mask any points without data
    mask=np.isinf(hist)
    goodhist=ma.masked_array(hist, mask=mask)
    
    #arrays to store the x and y values that will be fit to    
    fx=np.empty(len(hist[:,0])) # the middle value of each x bin
    fy=np.empty(len(hist[:,0])) # the middle value of the y bin that contains the most amount of spaxels in a given x bin
    fyerr=np.empty(len(hist[:,0])) # stores the error in fy if fittype='Gauss'
    
    #find the (x,y) points where histogram is peaked (ridge points)
    for i in range(0,len(xedges)-1):
        col=goodhist[i,:]
        if i==0: print(col)
        #good=np.isfinite(col)
        if fittype == 'max': hmax=np.nanargmax(col)
        elif fittype == 'Gauss': 
            ferr='abc'
            print('code this in!')
            return('Not supported')
        else:
            print(fittype + 'is not a recognized input for fittype, please check inputs and try again')
            return()
        fx[i]=(xedges[i]+xedges[i+1])/2.
        fy[i]=(yedges[hmax]+yedges[hmax+1])/2.
    if fittype == 'Gauss': ridge = np.asarray([fx,fy,ferr])
    else: ridge = np.asarray([fx,fy])
    
    return(histfig,ridge)

def fit_double(ridge):
    if len(ridge[:,0])<3: fyerr = None
    else: fyerr = ridge[2,:]
    #set bounds such that x0 is within xrange
    fx = ridge[0,:]
    fy = ridge[1,:]
    bounds = ((-1*np.inf, -1*np.inf, -1*np.inf, min(fx)), (np.inf, np.inf, np.inf, max(fx)))
    popt, pcov = curve_fit(doubline, fx, fy, sigma=fyerr, nan_policy='omit', bounds=bounds)
    # obtain errors from the covariant matrix
    perr = np.sqrt(np.diag(pcov))
    return(popt,perr)

def fit_single(ridge):
    if len(ridge[:,0])<3: fyerr = None
    else: fyerr = ridge[2,:]
    #set bounds such that x0 is within xrange
    fx = ridge[0,:]
    fy = ridge[1,:]
    bounds = ((-1*np.inf, -1*np.inf, -1*np.inf, min(fx)), (np.inf, np.inf, np.inf, max(fx)))
    popt, pcov = curve_fit(doubline, fx, fy, sigma=fyerr, nan_policy='omit', bounds=bounds)
    # obtain errors from the covariant matrix
    perr = np.sqrt(np.diag(pcov))
    return(popt,perr)

#add a double gauss??

def gauss(x, mean, std): #retain for fitting columns with Gaussian to obtain max with errors
    return(0.3989/std * math.e**(-.5*((x-mean)/std)**2)) #constant is 1/sqrt(2pi)

def line(x,m,b):
    return(m*x+b)

def doubline(x,m1,b1,m2,x0):
    b2 = m1*x0 + b1 - m2*x0
    y = np.zeros_like(x)
    y[x<x0] = m1*x[x<x0]+b1
    y[x>=x0] = m2*x[x>=x0]+b2
    return(y)

