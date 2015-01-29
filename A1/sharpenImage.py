import blurMetric
import imenh_lib as imenh
import imfilter_lib as imfilter
import laplacian_unsharp_masking as unsharp
import os
import sys
import Image

images = ["images/chalet.tif",
		"images/edgeblur.tif",
		"images/house.tif",
		"images/milano.tif",
		"images/photogravure.tif"]

def test():
	img = Image.open(images[1])
	print img.histogram()
	# print imenh.enh_alphaTMean(img, 0.5)


test()