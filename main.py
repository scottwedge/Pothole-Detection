
import Formatter
from pathlib import Path

def main():
    rootPath = '/'.join(str(Path().absolute()).split('\\'))
    trainingFile = "simpleTrainFullPhotosSortedFullAnnotations.txt"
    folderPath = "/Dataset 1 (Simplex)"
    parsedData = Formatter.ParsData(rootPath, trainingFile) #[[xy position, type, image]
    #print(parsedData[2])


    posTrainingImgs = Formatter.LoadFile(rootPath+folderPath+"/Train data/Positive data", parsedData)
    print(posTrainingImgs[0])
    print("Positive Trainging Images Loaded")
    negTrainingImgs = Formatter.LoadFile(rootPath+folderPath+"/Train data/Negative data", parsedData)
    print("Negative Training Images Loaded")

if __name__ == '__main__': main()
