from os import listdir
from os.path import isfile, join
import pickle

import imageio
from annoy import AnnoyIndex

from features_extraction import color_histogram


def get_image_files():
    """
    a method to get list of image files in the image directory
    """

    image_directory = "static/images/"
    return [join(image_directory, f) for f in listdir(image_directory) if isfile(join(image_directory, f))]


def nn_index(num_features=288, n_trees=10):
    """
    a method to perform annoy indexing
    and save into a bin file
    """

    image_files = get_image_files()

    # init annoy index
    ann_index = AnnoyIndex(num_features)

    for i, image_file in enumerate(image_files):
        print(i + 1, len(image_files))

        # load image

        # extract features

        # add features into annoy index

    # perform indexing

    # save the resulting index into a bin file


if __name__ == "__main__":
    nn_index()
