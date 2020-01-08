import json
import tensorflow as tf


class CNN(tf.keras.Model):
    """
        base cnn lstm model
    """

    def __init__(self, input_shape):
        super(CNN, self).__init__(name="")
        self.input_shape_ = input_shape

        ##cnn model 
        self.conv1 = tf.keras.layers.Conv1D(64, 3 , activation="tanh")
        self.maxpool1 = tf.keras.layers.MaxPooling1D(pool_size=2)
        self.conv2 = tf.keras.layers.Conv1D(128, 3 , activation="tanh")
        self.maxpool2 = tf.keras.layers.MaxPooling1D(pool_size=2)
        self.flatten1 = tf.keras.layers.Flatten()
        self.dropout1 = tf.keras.layers.Dropout(0.1)
        self.dense1 = tf.keras.layers.Dense(2048)
        self.dense2 = tf.keras.layers.Dense(1024)
        self.dense3 = tf.keras.layers.Dense(1)

    def call(self,input_tensor):
        
        x = self.conv1(input_tensor)
        x = self.maxpool1(x)
        x = self.conv2(x)
        x = self.maxpool2(x)
        x = self.flatten1(x)
        x = self.dropout1(x)
        x = self.dense1(x)
        x = self.dense2(x)
        x = self.dense3(x)
      
        return x


