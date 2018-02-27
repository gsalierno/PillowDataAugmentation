# -*- coding: utf-8 -*- 
import os  # handle system path and filenames
from PIL import Image
from random import randint

''' This class perform data augmentation on the input image set'''
IMGSIZE = 100
SCALING_SIZE80 = 80,80
SCALING_SIZE150 = 150,150
SCALING_SIZE200 = 200,200

imgInPath = "$INPUTFOLDER"
imgOutPath = "$OUTPUTFOLDER"
def get_image_paths():
    folder = imgInPath
    files = os.listdir(folder)
    files.sort()
    files = ['{}/{}'.format(folder, file) for file in files]
    return files

#Image Resizing
def resizeImages(FilesArray):
	for f in FilesArray:
		im = Image.open(f)
		out = im.resize((IMGSIZE, IMGSIZE))
		storeImage(out)

def rotate(FilesArray,degree):
	for f in FilesArray:
		im = Image.open(f)
		out = im.rotate(degree,expand=True)
		storeImage(out)

def scaling(FilesArray,size):
	for f in FilesArray:
		im = Image.open(f)
		try:
			im.thumbnail(size)
			storeImage(im)
		except AttributeError:
            			print ("cannot create thumbnail for '%s'" % im)


def grayScale(FilesArray):
	for f in FilesArray:
		im = Image.open(f)
		storeImage(im.convert('LA'))



def storeImage(im):
	im.save(imgOutPath+str(randint(0,100000))+".png")


def main():
	filearr = get_image_paths()
	#RESIZE IMAGES
	resizeImages(filearr)
	#ROTATE 90°
	rotate(filearr,90)
	#ROTATE 180°
	rotate(filearr,180)
	#ROTATE 270°
	rotate(filearr,270)
	#SCALE 80,150,200
	scaling(filearr,SCALING_SIZE80)
	scaling(filearr,SCALING_SIZE150)
	scaling(filearr,SCALING_SIZE200)
	#Convert to grayscale 
	grayScale(filearr)



    

if __name__ == "__main__":
    main()   