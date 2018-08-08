"""Functions related to visulizing ROIs drawn in Ca-imaging data

Assumes that ROI data is saved in dictionary (as generated in 'AnalyzeImaging' notebook)

roiData = {
    'imgData': rawtiff,
    'img': refimg,
    'numframes': slct_numframes,
    'slctframes': slct_frames,
    'fpv': fpv
    'numRoi': len(rois)
    'Fraw': time series of raw average of points in roi
    'DFF': time series of delta F/F in roi
    'Pts: points defining outline of roi
}

install shapely (pip install shapely) and descartes (pip install descartes) 

"""

from matplotlib import pyplot as plt
import numpy as np


# axis beautification
def myAxisTheme(myax):
    myax.get_xaxis().tick_bottom()
    myax.get_yaxis().tick_left()
    myax.spines['top'].set_visible(False)
    myax.spines['right'].set_visible(False)


def illustrateRoiOutline(roidat, ax, roicmap, title):
    from shapely.geometry.polygon import LinearRing
    
    ax.imshow(roidat['img'].T,cmap='Greys_r', vmin=0, origin='upper')
    
    for i, roi in enumerate(roidat['Pts']):
        roiOutl = LinearRing(roi)
        xr, yr = roiOutl.coords.xy
        ax.plot(xr, yr, color=roicmap.to_rgba(i), lw=2)
        ax.text(xr[0], yr[0], 'roi'+str(i+1), color='w', fontsize=10)
    
    ax.set_title(title)
    return ax

def illustrateRoiArea(roidat, ax, roicmap, title):
    from shapely.geometry.polygon import Polygon
    from descartes import PolygonPatch
    
    ax.imshow(roidat['img'].T,cmap='Greys_r', vmin=0, origin='upper')
    
    for i, roi in enumerate(roidat['Pts']):
        roiArea = Polygon(roi)
        
        roipatch = PolygonPatch(roiArea,alpha=0.7, color=roicmap.to_rgba(i))
        ax.add_patch(roipatch)
        
        ax.text(roi[0,0], roi[0,1], 'roi'+str(i+1), color='w', fontsize=10)
    ax.set_title(title)
    return ax


def illustrateRoiTrace(roidat, ax, roicmap, framerange, xlab, ylab, title):
    
    for i in range(roidat['numRoi']):
        ax.plot(roidat['DFF'][framerange,i],'-', color=roicmap.to_rgba(i))
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    
    ax.set_title(title)
    return ax
