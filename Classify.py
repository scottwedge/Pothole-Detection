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

    #for idx in range(len(trainImg)):
    for idx in range(1):
        input = trainImg[idx] #Dementions (2420, 2420, 3)
        print("TEST")
        conv1 = tf.layers.conv1d(inputs = input,activation='relu', filters=5,kernel_size=1 ,strides=1, padding='valid',name='conv1')
        print(conv1)
        print("TEST")







































if __name__ == '__main__': Classifier()
