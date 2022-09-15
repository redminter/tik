import cv2
import numpy as np
from matplotlib import pyplot as plt

#function for calculating entopy by photo
def entropyByPhoto(img):
  entropy = []
  hist = cv2.calcHist([img], [0], None, [256], [0, 255])
  total_pixel = img.shape[0] * img.shape[1]
  for item in hist:
      probability = item / total_pixel #calculating the propability of appereance of each pixel
      if probability == 0:
          en = 0
      else:
          en = -1 * probability * (np.log(probability) / np.log(2)) #implementing the formula
      entropy.append(en)
  sum_en = np.sum(entropy)
  return sum_en

#function for displaying a photo histogram 
def showHistogram(img, pltfigure, colors):

    fig = plt.figure(pltfigure)#creating a window
    fig.patch.set_facecolor('xkcd:light green')#color of background
    for i, color in enumerate(colors):

        polygon = cv2.calcHist([img], [i], None, [256], [0, 256])#creating a plot by each color
        plt.plot(polygon, color=color)
    



img_png = cv2.imread('img.png')#reading of image in png format
img_jpg = cv2.imread('img.jpg')#reading of image in jpg format
img_bmp = cv2.imread('img.bmp')#reading of image in bmp format

colors = ('red', 'green', 'blue')#initialization of colors

showHistogram(img_png, 1, colors)#using histogram function on png image
plt.title('PNG Image histogram')

res = entropyByPhoto(img_png)#using entropy function on png image
print('Png entropy:', res)



showHistogram(img_jpg, 2, colors)#using histogram function on jpg image
plt.title('JPG Image histogram')

res = entropyByPhoto(img_jpg)#using entropy function on jpg image
print('Jpg entropy:', res)



showHistogram(img_bmp, 3, colors)#using histogram function on bmp image
plt.title('BMP Image histogram')

res = entropyByPhoto(img_bmp)#using entropy function on bmp image
print('Bmp entropy: ', res)

plt.show()#opens a windows