import os
from PIL import Image
from BoundingBoxes import BoundingBoxes

def ParsData(trainingFile):

    counter = 0
    with open(trainingFile) as file:
        for line in file.readlines():
            parsedData = []
            parsedFile = []
            idx = 1

            tempLine = line
            tempLine = tempLine.split(".bmp")
            fileType = tempLine[0].split("\\")
            parsesdFile = parsedFile.append(fileType[0]+"/"+fileType[1]+"/")

            try:
                img = "C:/CNN/Pothole Dataset/Potholes Dataset/Dataset 1 Simplex/Train data/Positive data/"+fileType[2]+".jpg"
            except:
                img = None

            tempData = tempLine[1].split(" ")
            tempData.remove('')
            tempData.remove('\n')

            for i in range(len(tempData)):
                if tempData[idx] == '':
                    continue
                else:
                    try:
                        parsedData.append(tempData[idx:idx+4])
                        idx = idx + 4
                    except:
                        continue

            BoundingBoxes(img, parsedData, parsedFile, counter)
            counter += 1


if __name__ == '__main__': ParsData("simpleTrainFullPhotosSortedFullAnnotations.txt")
