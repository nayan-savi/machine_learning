from sklearn import datasets
from sklearn.svm import SVC
from scipy import misc
import imageio as image


digits = datasets.load_digits()
feature = digits.data
label = digits.target
clf = SVC(gamma=0.001)
clf.fit(feature, label)

img = image.imread("resources/number9.jpg")
img = misc.imresize(img, (8, 8))
img = img.astype(digits.images.dtype)
img = misc.bytescale(img, high=16, low=0)

data_set = []
for imgRow in img:
    for imgData in imgRow:
        data_set.append(sum(imgData)/3.0)


print(clf.predict([data_set]))


