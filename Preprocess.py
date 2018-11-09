from PIL import Image
from pathlib import Path
import glob
import os


def LoadFile(imageFolder, parsedData):
    imageList = []
    imageInfo = []
    counter = 0

    if parsedData == "Negative":
        for fileName in glob.glob(imageFolder+'/*.jpg'):
            im=Image.open(fileName)
            imageInfo.append(im)
            imageInfo.append(None)
            imageList.append(imageInfo)
            imageInfo = []
    else:
        #Looks for Image within folder and ties it to the coorect coordinates for the boxes
        for s in parsedData[counter][2]:
            for fileName in glob.glob(imageFolder+'/*.jpg'):
                for counter in range(len(parsedData)):
                    s = parsedData[counter][2]
                    if s in fileName:
                        im=Image.open(fileName)
                        imageInfo.append(im)
                        imageInfo.append(parsedData[counter][0])
                        imageList.append(imageInfo)
                    imageInfo = []

    return imageList

def Crop(imgList, path, type):
    counter = 0
    for im in range(len(imgList)):
        im = imgList[counter][0]
        im = im.crop((765,0,3185,2420))#Crops image to a 2420X2420
        try:
            im.save(path+"/Croped/"+type+"/"+str(counter)+".JPG")
        except:
            os.mkdir(path+"/Croped/"+type)
            im.save(path+"/Croped/"+type+"/"+str(counter)+".JPG")
        counter += 1
