from PIL import Image
from pathlib import Path
import glob


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
        for s in parsedData[counter][1]:
            for fileName in glob.glob(imageFolder+'/*.jpg'):
                for counter in range(len(parsedData)):
                    s = parsedData[counter][1]
                    if s in fileName:
                        im=Image.open(fileName)
                        imageInfo.append(im)
                        imageInfo.append(parsedData[counter][0])
                        imageList.append(imageInfo)

                    imageInfo = []
    return imageList
