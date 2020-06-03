


import tensorflow as tf
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd 

LABEL_COLUMN="Speed"
LABELS=[1,1.5,2,2.5,3,3.5,4,4.5,5,5.5,6,6.5,7,7.5,8,8.5,9,9.5,10]

df = pd.read_csv("tests.csv")
print(df.dtypes)
print(df.values)
print(df.head)
target = df.pop("Speed")
print(target.values)

dataset = tf.data.Dataset.from_tensor_slices((df.values, target.values))
# for feat, targ in dataset.take(5):
#   print ('Features: {}, Target: {}'.format(feat, targ))
# dataset = tf.data.experimental.make_csv_dataset("tests.csv",batch_size=249, label_name=LABEL_COLUMN, num_epochs=3)
# features, labels = next(iter(dataset))
# print(features)



