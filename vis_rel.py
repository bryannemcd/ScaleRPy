"""
Create publication-quality plots of scaling relationships from spatially resolved data
Created by Bryanne McDonough 11/22/2024
Part of ScaleRPy package
"""
import numpy as np
import matplotlib.pyplot as plt

def vis_res_rel(x, y, xlabel, ylabel, fitparams = [], fitparamserr = [], xrange=None, yrange=None):
    """ 
    This function produces a publication-quality plot visualizing a spatially-resolved scaling relationship.
    Spaxel density is plotted with hexbins and overplotted with contours. 
    Assumes x, y, xrange, and yrange are given in base-10 log space.

    x: a 1D array of length N containing the x values for the spatially resolved relationship (e.g., stellar mass surface density for N spaxels)
    y: a 1D array of length N the y values for the spatially resolved relationship (e.g., SFR surface density for N spaxels)
    xlabel: a string with the appropriate xlabel for the plot
    ylabel: a string with the appropriate ylabel for the plot
    fitparams: parameters for the fit to the scaling relationship as output from res_fit
    fitparamserr: error on the parameters fit to the scaling relationship as output from res_fit
    xrange: the range in x that should be plotted
    yrange: the range in y that should be plotted
    """

    

    ###ADD: error handling for data formats
    ###ADD: if fitparams empty, do fit

    #check length of fitparams for which line to use? - maybe not sustainable

