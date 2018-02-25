import numpy as np
from skimage.color import rgb2hsv


def color_histogram(image):
    """
    This method do these following:
    1. convert RGB image to HSV image
    2. calculate image histogram
    3. normalize the histogram
    """

    # convert to hsv
    hsv_image = rgb2hsv(image)

    # calculate histogram
    (h_hist, h_bins) = np.histogram(hsv_image[:, :, 0], bins=32)
    (s_hist, s_bins) = np.histogram(hsv_image[:, :, 1], bins=32)
    (v_hist, v_bins) = np.histogram(hsv_image[:, :, 2], bins=32)

    # return flatten histogram
    return np.hstack([h_hist, s_hist, v_hist]) 
