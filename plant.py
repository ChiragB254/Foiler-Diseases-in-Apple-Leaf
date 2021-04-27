import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from re import search
import natsort
from PIL import Image
from tqdm import tqdm
import tensorflow as tf

# print(tf.test.is_gpu_available())
# tf.test.is_gpu_available(
#     cuda_only=False, min_cuda_compute_capability=None
# )

import tensorflow as tf

if tf.test.gpu_device_name():

    print('Default GPU Device:{}'.format(tf.test.gpu_device_name()))

else:

   print("Please install GPU version of TF")
