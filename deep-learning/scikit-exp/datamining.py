import cv2
import numpy as np

img = cv2.imread('../numbers/number4.png')
img = img.astype(np.float64)

n_samples = len(img)
data = img.reshape((n_samples, -1))
while 1:
    cv2.imshow("Window", img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()

print(data)
