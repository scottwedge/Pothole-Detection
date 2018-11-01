<<<<<<< HEAD
import Formatter
from pathlib import Path

def main():
    rootPath = '/'.join(str(Path().absolute()).split('\\'))
    trainingFile = "simpleTrainFullPhotosSortedFullAnnotations.txt"
    folderPath = "/Dataset 1 (Simplex)"
    parsedData = Formatter.ParsData(rootPath, trainingFile) #[[xy position, type, image]
    #print(parsedData[2])

    
    posTrainingImgs = Formatter.LoadFile(rootPath+folderPath+"Train data/Positive data", parsedData )
    negTrainingImgs = Formatter.LoadFile(rootPath+folderPath+"Train data/Negative data", parsedData )#this will load the wrong images. We need to find a way to walk a folder one open the images within it
if __name__ == '__main__': main()
=======
import Formatter
from pathlib import Path

def main():
    rootPath = '/'.join(str(Path().absolute()).split('\\'))
    trainingFile = "simpleTrainFullPhotosSortedFullAnnotations.txt"
    folderPath = "/Dataset 1 (Simplex)"
    parsedData = Formatter.ParsData(rootPath, trainingFile) #[[xy position, type, image]
    #print(parsedData[2])

    
    posTrainingImgs = Formatter.LoadFile(rootPath+folderPath+"Train data/Positive data", parsedData )
    negTrainingImgs = Formatter.LoadFile(rootPath+folderPath+"Train data/Negative data", parsedData )#this will load the wrong images. We need to find a way to walk a folder one open the images within it
if __name__ == '__main__': main()
>>>>>>> 93ad83c589cb2a8763787ea2b0935625e259cebd
