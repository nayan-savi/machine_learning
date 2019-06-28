import numpy as np
import cv2
from matplotlib import pyplot as plt

# Create a black image
img = np.zeros((600, 600, 3), np.uint8)

img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 1)
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
img = cv2.circle(img, (447, 63), 63, (0, 0, 255), -1)
img = cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 180, 255, -1)

# Draw a diagonal blue line with thickness of 5 px

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
