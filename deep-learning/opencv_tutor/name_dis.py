import numpy as np
import cv2
from matplotlib import pyplot as plt
import calendar

img = np.zeros((600, 900, 3), np.uint8)

img = cv2.line(img, (0, 0), (600, 400), (255, 0, 0), 3)

plt.imshow(img)
plt.xticks(np.arange(5), ('Tom', 'Dick', 'Harry', 'Sally', 'Sue'))
plt.yticks(np.arange(12), calendar.month_name[1:13], rotation=45)  # to hide tick values on X and Y axis
plt.show()
