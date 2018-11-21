import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

from PIL import Image#Delete This is shouldn't be used other than for testing cases


def Classifier(trainImg, trainLabels):
    """
    Return will be an excel file of weights founded from training, or we could have
        the weights saved as a list that is later converted to an excel file
    """

    """
    First step: How to get input images in to the first convolutional layer?

    Solution:
        For loop to iterate through the list extracting the numpy array of 2420X2420X3
    """

    for idx in range(len(trainImg)):
        input = trainImg[idx]



if '__name__' == __main__: Classifier(
[
 [
  [202 223 242]
  [202 223 242]
  [202 223 242]

  [108 145 187]
  [108 145 187]
  [110 147 191]
 ]

 [[202 223 242]
  [202 223 242]
  [202 223 242]

  [109 146 188]
  [109 146 188]
  [109 146 190]]

 [[202 223 242]
  [202 223 242]
  [202 223 242]

  [109 146 188]
  [109 146 188]
  [109 146 188]]



 [[ 12  10  13]
  [ 13  11  14]
  [ 13  11  14]

  [ 61  56  62]
  [ 61  56  62]
  [ 61  59  64]]

 [[ 13  11  14]
  [ 13  11  14]
  [ 13  11  14]

  [ 61  56  62]
  [ 61  56  62]
  [ 57  55  60]]

 [[ 13  11  14]
  [ 13  11  14]
  [ 13  11  14]

  [ 60  55  61]
  [ 61  56  62]
  [ 53  51  56]]],[1,1,1,0,0,0] )
