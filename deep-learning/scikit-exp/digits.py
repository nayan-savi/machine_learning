from scipy import misc
from sklearn.svm import SVC
# from sklearn.externals import joblib
import numpy as np

file_names = ["../numbers/number1.jpg", "../numbers/number2.jpg",
              "../numbers/number3.jpg", "../numbers/number4.jpg",
              "../numbers/number5.jpg", "../numbers/number6.jpg",
              "../numbers/number7.jpg", "../numbers/number8.jpg",
              "../numbers/number9.jpg", "../numbers/number1_.jpg",
              "../numbers/number0.jpg", "../numbers/number00.jpg",
              "../numbers/number000.jpg", "../numbers/number22.jpg",
              "../numbers/number222.jpg", "../numbers/number22_.jpg",
              "../numbers/number33.jpg", "../numbers/number33_.jpg",
              "../numbers/number3_3.jpg", "../numbers/number_3_.jpg",
              "../numbers/number44.jpg", "../numbers/number55.jpg",
              "../numbers/number5_5.jpg"]


def load_data(list_file_names):
    x_train = []
    y_labels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 0, 0, 2, 2, 2, 3, 3, 3, 3, 4, 5, 5]
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


trains, labels = load_data(file_names)


clf = SVC(gamma=0.001)
clf.fit(trains, labels)
# joblib.dump(clf, '../model/saved_digit_model.pkl')
# clf_load = joblib.load('../model/saved_digit_model.pkl')


img_test = misc.imread("../test/test0.jpg")
img_test = misc.imresize(img_test, (8, 8))
img_test = img_test.astype(np.float64)
img_test = misc.bytescale(img_test, high=16, low=0)

x_input = []

for eachRow in img_test:
    for eachPixel in eachRow:
        x_input.append(sum(eachPixel) / 3.0)

print(clf.predict([x_input]))
