from bigfish import stack
import os
import bigfish
from pathlib import Path
from tqdm import tqdm
import tkinter as tk
from tkinter import filedialog
import bigfish.plot as plot
from cellpose import models
from matplotlib import pyplot as plt
from cellpose import plot as plt2
import pandas as pd
import numpy as np
import bigfish.segmentation as segmentation

def cell_nuc_segmentation(DAPI_2D, RNA_3D, RNA_2D, diam = 100, thresh=40):
    model = models.Cellpose(gpu=False,model_type='cyto')
    channels = [[3,3]]
    masks, flows, styles, diams = model.eval(DAPI_2D, diameter=diam, channels=channels, do_3D=False)
    
    ##display of results
    fig = plt.figure(figsize=(50,50))
    plt2.show_segmentation(fig, DAPI_2D, masks, flows[0], channels=[[3,0]])
    plt.tight_layout()
    plt.show()
    
    ##segement nucleus and cells
    nuc_label = np.int64(masks)
    cell_label = segmentation.cell_watershed(RNA_3D, nuc_label, threshold=thresh, alpha=0.95)
    
    # Plot the labelled nuclei and cells
    bigfish.plot.plot_segmentation_boundary(RNA_2D, cell_label, nuc_label, framesize=(40, 40), contrast=True, boundary_size=2)
    
    return (nuc_label, cell_label)
