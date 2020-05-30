from PIL import Image
from pylab import *
from sys import argv

def get_negative(im):
	return 255 - im

def get_clamp_to_interval(im, limit_left, limit_right):
	return ((limit_right - limit_left) / 255 * im + limit_left).astype(np.uint8)

def get_darker(im, k):
	return (255 * (im / 255) ** k).astype(np.uint8)


if __name__ == '__main__':
	im_link = './images/p3.jpg'
	if len(argv) > 1:
		im_link = './images/' + argv[1]
	im = array(Image.open(im_link).convert('L'))

	figure(figsize=(15, 15))

	subplot(2, 2, 1, title='Original')
	imshow(im)
	gray()

	subplot(2, 2, 2, title='Negative')
	imshow(get_negative(im))
	
	subplot(2, 2, 3, title='Clamp to interval 250-255')
	imshow(get_clamp_to_interval(im, 250, 255))
	
	subplot(2, 2, 4, title='Darker(4)')
	imshow(get_darker(im, 4))
	show()
