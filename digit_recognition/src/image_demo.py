from sklearn import datasets, svm, metrics
from scipy import misc
import numpy as np
import imageio as image

digits = datasets.load_digits()
# print(digits.target)
#
# feature = digits.data
# label = digits.target


img = image.imread("E:/data/number.jpg")
# img = misc.imresize(img, (8, 8))
img = img.astype(np.float64)
# img = misc.bytescale(img, high=16, low=0)


data_set = []
data_label = [0]
for imgRow in img:
    for imgData in imgRow:
        data_set.append(sum(imgData) / 3.0)
#
# n_samples = len(data_set)
# print(n_samples)
# data = digits.images.reshape((n_samples, -1))


n_samples = len(data_set)
# print(n_samples)
data = digits.images.reshape((n_samples, -2))
print(data)

# print(img)
# clf = svm.SVC(gamma=0.001)
# clf.fit(data_set, data_label)
