import os
from BoundingBoxes import BoundingBoxes

def ParsData(trainingFile):
    """Parses text file to extract the pothole location according to pixels, the type of data training/testing positive/negative, and image name

        :param trainingFile:    text file with information about dataset
        :type  trainingFile:    String
        :returns:               parsed
    """
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
            """
            tempParsed.append(parsedData)
            tempParsed.append(fileType[2])
            parsed.append(tempParsed)
            """
            parsed.append(fileType[2])
            counter += 1
        return parsed



if __name__ == '__main__': ParsData('/'.join(str(Path().absolute()).split('\\')), "simpleTrainFullPhotosSortedFullAnnotations.txt")
