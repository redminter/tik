import cv2
import numpy as np
from matplotlib import pyplot as plt

# reading the input image
img = cv2.imread('photo.png')
img1 = cv2.imread('photo.jpg')
img2 = cv2.imread('photo.bmp')
# define colors to plot the histograms
colors = ('b', 'g', 'r')

# compute and plot the image histograms
fig = plt.figure(1)
print('fig')
print(type(fig))
print(type(plt))
fig.patch.set_facecolor('xkcd:light green')
for i, color in enumerate(colors):

    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title('Image Histogram GFG PNG')

fig = plt.figure(2)
fig.patch.set_facecolor('xkcd:light green')
for i, color in enumerate(colors):

    hist = cv2.calcHist([img1], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title('Image Histogram GFG JPG')

fig = plt.figure(3)
fig.patch.set_facecolor('xkcd:light green')
for i, color in enumerate(colors):

    hist = cv2.calcHist([img2], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title('Image Histogram GFG BMP')

plt.show()
