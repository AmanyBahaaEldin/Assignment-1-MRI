import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('mri.jpeg',0)
dft = np.fft.fft2(img)
magnitude = np.abs(dft)
phase = np.angle(dft)
real=np.real(dft)
imaginary=np.imag(dft)
plt.subplot(151),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(152),plt.imshow(magnitude, cmap = 'gray')
plt.title('   magnitude'), plt.xticks([]), plt.yticks([])
plt.subplot(153),plt.imshow(phase, cmap = 'gray')
plt.title('phase'), plt.xticks([]), plt.yticks([])
plt.subplot(154),plt.imshow(real, cmap = 'gray')
plt.title('real'), plt.xticks([]), plt.yticks([])
plt.subplot(155),plt.imshow(imaginary, cmap = 'gray')
plt.title('imaginary'), plt.xticks([]), plt.yticks([])
plt.show()



