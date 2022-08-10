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

def cell_level_visualization(fov_results):
    for i, cell_results in enumerate(fov_results):
        # print("cell {0}".format(i))

        # get cell results
        cell_mask = cell_results["cell_mask"]
        cell_coord = cell_results["cell_coord"]
        nuc_mask = cell_results["nuc_mask"]
        nuc_coord = cell_results["nuc_coord"]
        rna_coord = cell_results["rna_coord"]
        image_contrasted = cell_results["image"]
        # print("\r number of rna {0}".format(len(rna_coord)))

        #plot cell
        plot.plot_cell(
            ndim=2, cell_coord=cell_coord, nuc_coord=nuc_coord, 
            rna_coord=rna_coord, 
            image=image_contrasted, cell_mask=cell_mask, nuc_mask=nuc_mask, 
            title="Cell {0}".format(i))