from scipy import misc
import numpy as np


class LoadData:

    def loadData(self, list_file_names):
        x_train = []
        y_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 0, 0, 2, 2, 2]
        for name in list_file_names:
            img = misc.imread(name)
            img = misc.imresize(img, (8, 8))
            img = img.astype(np.float64)
            img = misc.bytescale(img, high=16, low=0)
            x_test = []
            for row in img:
                for pixel in row:
                    x_test.append(sum(pixel) / 3.0)

            x_train.append(x_test)
        return x_train, y_labels
