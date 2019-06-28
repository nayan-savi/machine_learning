import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
from os import walk
import glob
import imageio as image

train_data = []
train_label = []

keras.datasets

files = glob.glob("../numbers/*.jpg")

for fileName in files:
    label = fileName[11:18]
    data = cv.imread(fileName)
    data = cv.resize(data, (28, 28))
    img = image.imread(fileName)
    train_data.append(data.astype(np.float64))
    train_label.append(label)

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 3)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(9, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_data, train_label, epochs=5)

