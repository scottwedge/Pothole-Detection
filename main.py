from pathlib import Path
from PIL import Image
import numpy as np

import Preprocess
import Formatter

def main():
    rootPath = '/'.join(str(Path().absolute()).split('\\'))
    folderPath = "/Dataset 1 (Simplex)"
    trainingFile = "simpleTrainFullPhotosSortedFullAnnotations.txt"
    bounds = (765,0,3185,2420) #Predefined by looking at dataset -- will need to be changed based on dataset

    posTrainingData = []
    negTrainingData = []
    #Format Data
    parsedData = Formatter.ParsData(rootPath+folderPath+'/'+trainingFile) #[[xy position], type, image]

    posTrainingImgs = Preprocess.LoadFile(rootPath+folderPath+"/Train data/Positive data", parsedData, type = "jpg")
    print("Positive Trainging Images Loaded")

    negTrainingImgs = Preprocess.LoadFile(rootPath+folderPath+"/Train data/Negative data", parsedData="Negative", type = "jpg")
    print(negTrainingImgs[0][0])
    print("Negative Training Images Loaded")


    #Preprocessing
    """
    1) Uniform Aspect Ratio -- we'll want to crop the image into a square and detemin where in the image we want to be looking
        pass

    2) Image Scaling -- After determining the width and hight of the image in pixels we'll either need to up/down-scal the imageInfo

    3) Mean, Std of input data: used to find the underlying stucture of the image, not alwasy needed; Personally I think we should try
        with and without it to see what returns a high accuracy

    4) Normalization -- we need to scale the image to a range of [0, 1] or [0, 255]; Personally, I think scalling the image to a range of
        [0, 1] would be more benificial for speed, but [0, 255] could produce a higher accuracy

    5) Dimensionality Reduction -- Not neccesary although used to collapse the RGB channels into a gray scale imageInfo

    6) Data Augmentation -- Commonly used to increase training images by scaling, rotating, and other affine transformations used to expose
        the neural network to a wider array of variations if data is small; out data will be small so we will definietly need to do this

    Each of these are useful for other applications as well and should be their own functions within their own
    script (class) so that we can use them for future use
    """
    #Aspect Ratio
    #Need to OPTIMIZE  this portion -- it takes to long for real time applications
    for idx in range(len(posTrainingImgs)):
        pos = Preprocess.Crop(posTrainingImgs[idx][0], bounds)
        posTrainingData.append(np.asarray(pos, dtype="int32"))
    print("Positive Trainging Images Cropped")
    print(posTrainingData)
    print(posTrainingData[0])
    """
    for idx in range(len(negTrainingImgs)):
        negTrainingImgs[idx][0] = Preprocess.Crop(negTrainingImgs[idx][0], bounds)
        negTrainingData.append(np.asarray(negTrainingImgs[idx][0], dtype="int32"))
    print("Negative Training Images Cropped")
    """
    #Image Scaling


    #Train CNN

    #Classifier

if __name__ == '__main__': main()
