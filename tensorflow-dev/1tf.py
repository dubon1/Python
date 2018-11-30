#!/usr/bin/python3

import tensorflow as tf

# disable CPU
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

hello = tf.constant("Hello, world!")
sess=tf.Session()
print(sess.run(hello))
