""" Functions related to processing of analog squerical treadmill (TM) recordings """
import numpy as np


def processTMSignals(rawtmsignal, tmParams, wsParams):
    tmchan = rawtmsignal.keys()
    tmticks= {} # new dict for digitizes values
    
    maxTicks = 3
    
    for i, ch in enumerate(tmchan):
        chfilt = mysmooth(rawtmsignal[ch]-np.median(rawtmsignal[ch]),int(wsParams['fps']*tmParams['tickLength']))
        chquant = quantizeTicks(chfilt, maxTicks, tmParams['tickAmp'])
        
        tmticks[ch] = chquant
        
    return tmticks

def mysmooth(y, box_pts):
    box = np.ones(box_pts)/box_pts
    y_smooth = np.convolve(y, box, mode='same')
    return y_smooth

def quantizeTicks(y, maxTicks, tickAmp):
    yq = y.copy()
    digBins = np.linspace(-maxTicks, maxTicks,2*maxTicks+1)*tickAmp*0.7-(tickAmp*0.7)/2.0
    yq = np.digitize(y, digBins)
    yq = (yq - (maxTicks+1))
    return yq


def myInterpol(ts, t, y):
    from scipy.interpolate import interp1d
    
    f_y = interp1d(t, y, kind = 'linear')
    
    return f_y(ts)