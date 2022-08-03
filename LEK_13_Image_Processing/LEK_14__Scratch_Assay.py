#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 11:43:07 2022
@author: vera
"""

"""
Scratch assay or Wound healing assay is one of the common assays in biology. 
It involves segmenting time series images for 'clean' vs cell-filled regions. 
This task can be very challenging as histogram segmentation does not yield 
desired results.
This video tutorial explains the segmentation process using Entropy filter and 
Otsu thresholding in Python. It also explains the process of looping through 
images to analyze and plot the results.
"""

"""
Scratch Assay: cells are on the glass slide, cell layer is scratched and images are taken over time to observe healing.

Challenge - pixels are alike -> hard to separate filter enropy (measure of disorder):
- low entropy (clean area), high entropy (the whole area)

"""

# =============================================================================
# Load libraries
from skimage.filters.rank import entropy
from skimage.morphology import disk

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

from skimage.filters import threshold_otsu

import glob # walk over folders
from scipy.stats import linregress
import os
# =============================================================================
# Read image
img = io.imread("images/scratch.jpg")
plt.hist(img.flat, bins = 50)
print(img.shape)
plt.imshow(img, cmap="gray") 
 
# Create an entropy filter image
entropy_img = entropy(img, disk(10))
plt.imshow(entropy_img,cmap="gray")
plt.hist(entropy_img.flat, bins = 50)


# thresholding for separation (automated)
thresh = threshold_otsu(entropy_img)
plt.imshow(entropy_img, cmap="gray")
print(thresh) # a single value (not a ndim array)
# the best value for separation
 
# Segmentation (by a sweet spot)
binary = entropy_img <= thresh # False and True 
plt.imshow(binary, cmap="gray") # great segmentation!
 
# Getting some information
print(np.sum(binary == 1)) # number of pixesl corr. to yellow area
# 1 or True
print(binary.sum()) 
# =============================================================================

# Loop over a bunch of images (folder) 

# time association (end-to-end analysis)

time = 0 # capture time -> plot

time_list = [] 
area_list = []
images = []

path = "images/scratch_assay/*.*"


list_of_files = sorted(filter(os.path.isfile, glob.glob(path)))

for file in list_of_files:
    img = io.imread(file)
    entropy_img = entropy(img, disk(10)) # disk value taken from the paper
    thresh = threshold_otsu(entropy_img)
    binary = entropy_img <= thresh
    scratch_area = np.sum(binary == True)
    print(time, scratch_area)
    time_list.append(time)
    area_list.append(scratch_area)
    time += 1 # update time
    images.append(binary)
    

    
print(time_list, area_list)    
print(images)

plt.plot(time_list, area_list, "bo")

print(linregress(time_list, area_list))
slope, intercept, r_value, p_value , std_err = linregress(time_list, area_list)
print(f"y = {slope.round(2)}x + {intercept.round(2)} ")
print("R\N{SUPERSCRIPT TWO} = ", r_value**2)

# =============================================================================
# Plot all images

fig, ims = plt.subplots(nrows=2,ncols=5, figsize=(8,4))
ims[0, 0].imshow(images[0])
ims[0, 0].set_title(f"Time: {time_list[0]}")

ims[0, 1].imshow(images[1])
ims[0, 1].set_title(f"Time: {time_list[1]}")

ims[0, 2].imshow(images[2])
ims[0, 2].set_title(f"Time: {time_list[2]}")

ims[0, 3].imshow(images[3])
ims[0, 3].set_title(f"Time: {time_list[3]}")

ims[0, 4].imshow(images[4])
ims[0, 4].set_title(f"Time: {time_list[4]}")

ims[1, 0].imshow(images[5])
ims[1, 0].set_title(f"Time: {time_list[5]}")

ims[1, 1].imshow(images[6])
ims[1, 1].set_title(f"Time: {time_list[6]}")

ims[1, 2].imshow(images[7])
ims[1, 2].set_title(f"Time: {time_list[7]}")

ims[1, 3].imshow(images[8])
ims[1, 3].set_title(f"Time: {time_list[8]}")

ims[1, 4].imshow(images[9])
ims[1, 4].set_title(f"Time: {time_list[9]}")
plt.show()