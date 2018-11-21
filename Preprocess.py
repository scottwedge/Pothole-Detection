#This script is under construction to be updated for generalizability -- removed all 2D list and make them 1D
from PIL import Image
from pathlib import Path
import glob
import os


def LoadFile(imageFolder, parsedData, type):
    """Loads all images from specified file

        :param  imageFolder:    path to folder containing images
        :type   imageFolder:    String
        :param  parsedData:     Image name
        :type   parsedData:     String/2D List
        :param  type:           type of image to load ie png, jpg, gif
        :type   type:           String
        :returns:               imageList
    """

    imageList = []
    imageInfo = []
    counter = 0
    if parsedData == "Negative":
        for fileName in glob.glob(imageFolder+'/*.'+type):
            im=Image.open(fileName)
            """
            imageInfo.append(im)
            imageInfo.append(None)
            imageList.append(imageInfo)
            """
            imageList.append(im)
            imageInfo = []
    else:
        #Looks for Image within folder and ties it to the coorect coordinates for the boxes
        #for s in parsedData[counter][1]:
        for fileName in glob.glob(imageFolder+'/*.'+type):
            for counter in range(len(parsedData)):
                s = parsedData[counter]

                if s in fileName:
                    im=Image.open(fileName)
                    """
                    imageInfo.append(im)
                    imageInfo.append(parsedData[counter])
                    imageList.append(imageInfo)
                    """
                    imageList.append(im)
                imageInfo = []

    return imageList

def Crop(imgList, bounds):
    """Crops image to size specifiedby bounds

        :param  imgList:    Images
        :type   imgList:    Images.open()/2D List
        :param  bounds:     position of box corners given as [x, y, x+Delta_X, y+Delta_y]
        :type   bounds:     int/List
        :returns:
    """

    imgList = imgList.crop(bounds)#Crops image to a 2420X2420
    #imgList.show()
    return imgList
