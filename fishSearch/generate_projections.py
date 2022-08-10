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

def generate_projections(img):
    # Define DAPI Channel
    DAPI_3D = img[:,0,:,:]
    DAPI_2D = stack.maximum_projection(DAPI_3D)

    # Probe Channel
    RNA_3D = img[:,1,:,:]
    RNA_2D = stack.maximum_projection(RNA_3D)
    
    images = [DAPI_2D, RNA_2D]
    bigfish.plot.plot_images(images,rescale=True, contrast=True)
    
    return [DAPI_3D, DAPI_2D, RNA_3D, RNA_2D]
