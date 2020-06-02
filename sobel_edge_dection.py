import cv2
import numpy as np
from PIL import Image
from pylab import *
from sys import argv



def get_sobel_edge_dection(im):
	sobel_x  = cv2.Sobel(im, -1, 1, 0, ksize=5)
	sobel_y  = cv2.Sobel(im, -1, 0, 1, ksize=5)
	return (sobel_x, sobel_y)


if __name__ == '__main__':
	im_link = './images/p5.jpg'
	if len(argv) > 1:
		im_link = './images/' + argv[1]
	im = cv2.imread(im_link, 0)

	figure(figsize=(15, 15))
	sobel_x, sobel_y = get_sobel_edge_dection(im)

	subplot(3, 1, 1, title='Original')
	imshow(Image.open(im_link))

	subplot(3, 1, 2, title='Sobel x')
	imshow(sobel_x, cmap ='gray')
	
	subplot(3, 1, 3, title='Sobel y')
	imshow(sobel_y, cmap ='gray')

	show()
