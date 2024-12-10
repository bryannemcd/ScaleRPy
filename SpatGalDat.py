import numpy as np
import matplotlib.pyplot as plt
import math
import fit_funcs as fit
"""
Functions to add:
    rem_low : remove low s_mass from the sample
    wrappers for ridge fit 
    
"""

class SpatGalDat:
    """
    Class for handling pre-processed 'spaxel' data from spatially-resolved galaxies
    Measure the slopes of spatially resolved scaling relationships
    Produce publication-quality plots

    """

    def __init__(self, s_mass, sfr, gas, scale='log'):
        """Instance variables should be arrays or lists. 
        At least two variables should be defined as non-empty arrays.
        Default assumes spaxel values are already in base-10 log space"""

        # ADD ERROR: check that at least two arrays are non-empty and the same length
      
        #initialize variables, ensure any non-finite values are handled as NaNs
        self.s_mass = np.where(np.isfinite(s_mass),s_mass, np.nan*np.array(s_mass))
        self.sfr = np.where(np.isfinite(sfr), sfr, np.nan*np.array(sfr))
        self.g_mass = np.where(np.isfinite(gas), gas, np.nan*np.array(gas))

        if scale != 'log':
            #take the base10 log and replace zeros with NaNs
            self.s_mass = np.log10(self.s_mass, out = np.nan*self.s_mass, where = (self.s_mass>0))
            self.sfr = np.log10(self.sfr, out = np.nan*self.sfr, where = (self.sfr>0))
            self.g_mass = np.log10(self.g_mass, out = np.nan*self.g_mass, where = (self.g_mass>0))
        
        self.s_mass_unit = r'$M_\odot \mathrm{kpc}^{-2}$'
        self.sfr_unit = r'$M_\odot \mathrm{yr}^{-1} \mathrm{kpc}^{-2}$'
        self.gas_unit = r'$M_{\mathrm{gas}} \mathrm{kpc}^{-2}$'
        #self.s_mass_label = r'log$_{10}$[$\Sigma_*$ / ($M_\odot$ kp$\mathrm{c}^{-2}$)]'
        
    

    
    def SFMS_ridge(self, **kwarg):
        """Identify the 'ridge' of data for the star-forming main sequence
            Keyword arguments passed to find_ridge"""
        xlab = 'log$_{10} (\Sigma_* / $ [%s])' % self.s_mass_unit
        ylab = 'log$_{10} (\Sigma_{\mathrm{SFR}}/$ [%s])' % self.sfr_unit
        self.SFMS_hist, self.SFMS_ridge = fit.find_ridge(self.s_mass, self.sfr, xlabel = xlab, ylabel=ylab, **kwarg)
        return(self.SFMS_hist,self.SFMS_ridge)

    def KS_ridge(self, **kwarg):
        xlab = 'log$_{10} (\Sigma_{\mathrm{gas}} /$ [%s])' % self.gas_unit
        ylab = 'log$_{10} (\Sigma_{\mathrm{SFR}}/$ [%s])' % self.sfr_unit
        self.KS_hist, self.KS_ridge = fit.find_ridge(self.g_mass, self.sfr, xlabel=xlab, ylabel= ylab, **kwarg)
        return(self.KS_hist,self.KS_ridge)
    
    def MGMS_ridge(self,**kwarg):
        xlab = 'log$_{10} (\Sigma_* /$ [%s])' % self.s_mass_unit
        ylab = 'log$_{10} (\Sigma_{\mathrm{gas}} /$ [%s])' % self.gas_unit
        self.MGMS_hist, self.MGMS_ridge = fit.find_ridge(self.s_mass, self.g_mass, xlabel=xlab, ylabel=ylab, **kwarg)
        return(self.MGMS_hist, self.MGMS_ridge)

        """
        if fittype != 'Gauss': fyerr=None
        
        if fitline == '1line': popt,pcov = curve_fit(line, fx, fy, sigma=fyerr, nan_policy='omit')
        elif fitline == '2line': 
            #set bounds such that x0 is within xrange
            bounds = ((-1*np.inf, -1*np.inf, -1*np.inf, xrange[0]), (np.inf, np.inf, np.inf, xrange[1]))
            popt, pcov = curve_fit(doubline, fx, fy, sigma=fyerr, nan_policy='omit', bounds=bounds)
        # obtain errors from the covariant matrix
        perr = np.sqrt(np.diag(pcov))

        #if not savefitparams is None: np.savetxt(savefitparams, np.vstack((popt,perr)).T)

        #if not savefitfig is None:
        ax.scatter(fx, fy, c='black', marker='o', zorder=2)
        if fitline == '1line': ax.plot(fx, line(fx, popt[0],popt[1]), color = 'cyan')
        elif fitline == '2line': ax.plot(fx, doubline(fx, popt[0],popt[1],popt[2],popt[3]), color='cyan')
            #plt.savefig(savefitfig)

        return(popt, perr, hist, )
        #update returns to feed into a wrapper function for specific relations
        #wrapper will return fit and save variables to the class
        #specifically, pass then save figure, ridge points, fit params
        """

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
