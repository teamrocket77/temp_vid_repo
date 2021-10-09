import numpy as np
import  cv2 as cv

image = cv.imread('hey1.jpg')

row,col,ch = image.shape
s_vs_p = 0.5
amount = 0.004
out = np.copy(image)
      # Salt mode 
num_salt = np.ceil(amount * image.size * s_vs_p)
coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
out[coords] = 1
    # Pepper mode
num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
out[coords] = 0

cv.imshow("n", out)
cv.waitKey(0)
