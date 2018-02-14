"""Functions related to visulizing ROIs drawn in Ca-imaging data"""
# Assumes that ROI data is saved in dictionary as generated in 'AnalyzeImaging notebook

from matplotlib import pyplot as plt
import numpy as np

def illustrateRois(roidat):
    from scipy.spatial import ConvexHull

    roifig, axs = plt.subplots(nrows=1,ncols=2, figsize=(15,8))
    
    axs[0].imshow(roidat['img'], 'gray')
    axs[1].imshow(roidat['img'], 'gray')
    
    for i in np.arange(0,roidat['numRoi']):
        xr = roidat['roiShapes'][i][0]
        yr = roidat['roiShapes'][i][1]
       
        points = np.zeros((len(xr),2))
        points[:,0] = yr; points[:,1] = xr
        hull = ConvexHull(points)

        axs[0].text(yr[0], xr[0], 'roi'+str(i+1), color='w', fontsize=10)
        axs[0].plot(points[hull.vertices,0], points[hull.vertices,1], 'r', lw=1)
        axs[1].text(yr[0], xr[0], 'roi'+str(i+1), color='w', fontsize=10)
        axs[1].scatter(roidat['roiShapes'][i][1],roidat['roiShapes'][i][0],alpha=0.07,
                       marker='.', edgecolors='none')
    
    return roifig