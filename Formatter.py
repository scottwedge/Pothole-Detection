import os
from PIL import Image
from pathlib import Path
import glob

from BoundingBoxes import BoundingBoxes

def ParsData(rootPath, trainingFile):

    counter = 0

    parsed = []
    with open(trainingFile) as file:
        for line in file.readlines():
            parsedData = []
            parsedFile = []
            tempParsed = []
            idx = 1

            tempLine = line
            tempLine = tempLine.split(".bmp")
            fileType = tempLine[0].split("\\")

            tempData = tempLine[1].split(" ")

            try:
                tempData.remove('')
            except:
                continue
            try:
                tempData.remove('\n')
            except:
                continue

            for i in range(len(tempData)):
                if tempData[idx] == '':
                    continue
                else:
                    try:
                        parsedData.append(tempData[idx:idx+4])
                        idx = idx + 4
                    except:
                        continue
            #print(parsedData[0])
            tempParsed.append(parsedData)
            #tempParsed.append(parsedFile)
            #print(fileType[2])
            tempParsed.append(fileType[2])
            parsed.append(tempParsed)
            #print(parsed[0])
            #BoundingBoxes(img, parsedData, parsedFile, counter)#was only needed for testing
            counter += 1
        return parsed

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

if __name__ == '__main__': ParsData('/'.join(str(Path().absolute()).split('\\')), "simpleTrainFullPhotosSortedFullAnnotations.txt")
