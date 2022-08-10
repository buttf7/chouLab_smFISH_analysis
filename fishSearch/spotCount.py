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

def spotCount(fov_results, img_name):
    averageCount = []
    img_name = img_name.split('.tif')
    img_name = img_name[0]
    for i, cell_results in enumerate(fov_results):
        # print("cell {0}".format(i))

        # get cell results
        cell_mask = cell_results["cell_mask"]
        cell_coord = cell_results["cell_coord"]
        nuc_mask = cell_results["nuc_mask"]
        nuc_coord = cell_results["nuc_coord"]
        rna_coord = cell_results["rna_coord"]
        image_contrasted = cell_results["image"]
        averageCount.append(len(rna_coord))
        
    spotCountCSV = pd.DataFrame(averageCount)
    spotCountCSV.to_csv(f'{os.path.abspath(os.path.join(os.getcwd(), os.pardir))}/data/graph_data/cellSpotCount_{img_name}.csv', index=False)
