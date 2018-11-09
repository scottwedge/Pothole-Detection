import os
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
            parsesdFile = parsedFile.append(fileType[0]+"/"+fileType[1]+"/")
            """
            #Only needed for testing
            try:
                img = rootPath+"/Dataset 1 (Simplex)/Train data/Positive data/"+fileType[2]+".jpg"
            except:
                img = None
                """
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

            tempParsed.append(parsedData)
            tempParsed.append(parsedFile)
            #print(fileType[2])
            tempParsed.append(fileType[2])
            parsed.append(tempParsed)
            #print(parsed[0])
            #BoundingBoxes(img, parsedData, parsedFile, counter)#was only needed for testing
            counter += 1
        return parsed



if __name__ == '__main__': ParsData('/'.join(str(Path().absolute()).split('\\')), "simpleTrainFullPhotosSortedFullAnnotations.txt")
