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

def read_img():
    root = tk.Tk()
    root.withdraw()
    img_path = filedialog.askopenfilename()
    img_name = img_path.split("/")
    img_name = img_name[-1]
    img = stack.read_image(img_path)
    print("\r shape: {0}".format(img.shape))
    print("\r dtype: {0}".format(img.dtype))
    return (img, img_name)
