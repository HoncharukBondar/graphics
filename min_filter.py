import scipy.ndimage
from PIL import Image
from sys import argv
from pylab import *


def get_min_filter(im):
	return Image.fromarray(scipy.ndimage.filters.minimum_filter(im,size=5, footprint = None, output = None, mode= 'reflect', cval =0.0,origin =0))

if __name__ == '__main__':
	im_link = './images/p3.jpg'
	if len(argv) > 1:
		im_link = './images/' + argv[1]
	im = Image.open(im_link)

	figure(figsize=(15, 15))
	
	subplot(2, 1, 1, title='Original')
	imshow(im)

	subplot(2, 1, 2, title='Min filter')
	imshow(get_min_filter(im))

	show()
