import pickle

from annoy import AnnoyIndex

from features_extraction import color_histogram


class NNSearch:

    def __init__(self, image_file_bin, index_file_bin):
        """
        initialize annoy index
        and image files
        """

        self.ann_index = AnnoyIndex(96)

        self.image_files = pickle.load(open(image_file_bin, "rb"))
        self.ann_index.load(index_file_bin)

    def search(self, image, n=10):
        """
        a method to perform search
        """

        # extract features for query image
        query_features = color_histogram(image)

        # get similar image indices
        indices = self.ann_index.get_nns_by_vector(query_features, n)

        # return path of similar images
        return [self.image_files[i] for i in indices]


if __name__ == "__main__":
    import imageio

    image_test = imageio.imread("static/images/200900.jpg")
    search_engine = NNSearch("image_files.bin", "index.ann")
    result = search_engine.search(image_test)
    print(result)
