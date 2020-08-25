#!/usr/bin/env python
# coding: utf-8

# In[4]:


import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.transform import resize
from IPython.display import HTML
import warnings
warnings.filterwarnings("ignore")


# In[7]:


source_image = imageio.imread('/home/rahil/Downloads/web downloads/download.jpeg')
driving_video = imageio.mimread('/home/rahil/Downloads/Induction Motor - Funny scene _ 3 Idiots _ Aamir Khan _ R Madhavan _ Sharman Joshi.mp4',memtest=False)

