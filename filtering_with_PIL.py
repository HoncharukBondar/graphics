from PIL import Image
from PIL import ImageFilter
from sys import argv
from pylab import *

def get_contoured(im):
    return im.filter(ImageFilter.CONTOUR)

def get_detailed(im):
    return im.filter(ImageFilter.DETAIL)

def get_edge_enhanced(im):
    return im.filter(ImageFilter.EDGE_ENHANCE)

def get_edge_enhanced_more(im):
    return im.filter(ImageFilter.EDGE_ENHANCE_MORE)

def get_embossed(im):
    return im.filter(ImageFilter.EMBOSS)

def get_with_found_edges(im):
    return im.filter(ImageFilter.FIND_EDGES)

def get_smoothed(im):
    return im.filter(ImageFilter.SMOOTH)

def get_smoothed_more(im):
    return im.filter(ImageFilter.SMOOTH_MORE)

def get_sharpened(im):
    return im.filter(ImageFilter.SHARPEN)

def get_filtered_custom_kernel(im, kernel):
    size = (3, 3)
    kerFilter = ImageFilter.Kernel(size, kernel, scale=None, offset=0)
    return im.filter(kerFilter)

if __name__ == '__main__':
    im_link = './images/p8.jpg'
    if len(argv) > 1:
        im_link = './images/' + argv[1]
    im = Image.open(im_link)
    figure(figsize=(15, 15))

    subplot(3, 4, 1, title='Original')
    imshow(im)
    
    subplot(3, 4, 2, title='contoured')
    imshow(get_contoured(im))

    subplot(3, 4, 3, title='detailed')
    imshow(get_detailed(im))

    subplot(3, 4, 4, title='edge enhanced')
    imshow(get_edge_enhanced(im))

    subplot(3, 4, 5, title='edge enhanced more')
    imshow(get_edge_enhanced_more(im))

    subplot(3, 4, 6, title='embossed')
    imshow(get_embossed(im))

    subplot(3, 4, 7, title='with found edges')
    imshow(get_with_found_edges(im))

    subplot(3, 4, 8, title='smoothed')
    imshow(get_smoothed(im))

    subplot(3, 4, 9, title='smoothed more')
    imshow(get_smoothed_more(im))

    subplot(3, 4, 10, title='sharpened')
    imshow(get_sharpened(im))

    subplot(3, 4, 11, title='filtered custom kernel 1')
    imshow(get_filtered_custom_kernel(im, [1,1,1,1,-1,1,-1,-1,-1]))

    subplot(3, 4, 12, title='filtered custom kernel 2')
    imshow(get_filtered_custom_kernel(im, [1,0,-1,1,0,-1,0,0,-1]))


    show()
