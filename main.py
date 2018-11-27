from pathlib import Path
from PIL import Image #Look into using Matplotlib
import numpy as np
import tensorflow as tf

import time

import Preprocess
import Formatter
import Classify

def main():
    start = time.clock()

    rootPath = '/'.join(str(Path().absolute()).split('\\'))
    folderPath = "/Dataset 1 (Simplex)"
    trainingFile = "simpleTrainFullPhotosSortedFullAnnotations.txt"

    bounds = (765,0,3185,2420) #Predefined by looking at dataset -- will need to be changed based on dataset
    trainImg = []
    trainLabels = []
    #Format Data
    #parsedData = Formatter.ParsData(rootPath+folderPath+'/'+trainingFile) #[[xy position], type, image]

    posTrainingImgs = Preprocess.LoadFile(rootPath+folderPath+"/Train data/Positive data", parsedData="Positive", type = "jpg")
    print("Positive Trainging Images Loaded")

    negTrainingImgs = Preprocess.LoadFile(rootPath+folderPath+"/Train data/Negative data", parsedData="Negative", type = "jpg")
    print("Negative Training Images Loaded")

    #del parsedData

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

    """
    #Aspect Ratio
    #for idx in range(len(posTrainingImgs)):
    for idx in range(1):
        pos = Preprocess.Crop(posTrainingImgs[idx], bounds)
        #pos = np.asarray(pos, dtype="uint8")#Turns image in to a numpy array between 0 255
        pos = tf.convert_to_tensor(np.asarray(pos, dtype="uint8"), dtype=tf.float16)#Turns image in to a tensor
        trainImg.append(pos)
        trainLabels.append(1)
    print("Positive Trainging Images Cropped")

    del posTrainingImgs
    del pos

    """
    #for idx in range(len(negTrainingImgs)):
    for idx in range(1):
        neg = Preprocess.Crop(negTrainingImgs[idx], bounds)
        neg = tf.convert_to_tensor(np.asarray(neg, dtype="uint8"), dtype=tf.float16)#Turns image in to a tensor
        trainImg.append(neg)
        trainLabels.append(0)
    print("Negative Training Images Cropped")

    del negTrainingImgs
    del neg
    """
    #Image Scaling
    #posTrainingData =np.interp(posTrainingData, (posTrainingData.min(), posTrainingData.max()), (0, 1))#Normalize image between 0 and 1 --Does not look useful
    #img = Image.fromarray(trainImg[0], 'RGB')#Converts numpy array back to an image
    #img.show()

    #Train CNN
    Classify.Classifier(trainImg, trainLabels)











    stop = time.clock()
    print("Time: "+str((stop-start)/60))
if __name__ == '__main__': main()
