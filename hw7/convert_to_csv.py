#Daniel Ryaboshapka

import io
import os
import sys
import glob
import shutil
import numpy as np
import pandas as pd
import tensorflow as tf
import xml.etree.ElementTree as xt
from collections import namedtuple

image_set_dir = 'legotrainset'
pascal_voc_dir = 'legotrainset_annotated'
csv_labels_dir = 'Labels/'
csv_labels_split_dir = 'Labels_Split/'
tfrecord_dir = 'TFRecord/'
train_dir = 'Train/'

csv_labels_path = csv_labels_dir + 'labels.csv'
csv_train_labels_path = csv_labels_split_dir + 'train_labels.csv'
csv_test_labels_path = csv_labels_split_dir + 'test_labels.csv'
tfrecord_train_path = tfrecord_dir + 'train.record'
tfrecord_test_path = tfrecord_dir + 'test.record'

def pascal_voc_to_csv(input_dir, output_path):
    annot_list = []
    for file in glob.glob(input_dir + '/*.xml'):
        tree = xt.parse(file)
        root = tree.getroot()
        for element in root.findall('object'):
            item = (root.find('filename').text,
                    int(root.find('size')[0].text),
                    int(root.find('size')[1].text),
                    element[0].text,
                    int(element[4][0].text),
                    int(element[4][1].text),
                    int(element[4][2].text),
                    int(element[4][3].text))
            annot_list.append(item)
        csv_headers = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
        csv_data = pd.DataFrame(annot_list, columns=csv_headers)
    csv_data.to_csv(output_path, index=None)
    return csv_data

def create_tf_example(label_group, label_map, image_set_path):
    with tf.gfile.GFile(os.path.join(image_set_path, '{}'.format(label_group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
        
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = label_group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in label_group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(label_map[row['class']])

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    
    return tf_example    


def create_tfrecord_file(labels, label_map_path, input_path, output_path):
    tfrecord_writer = tf.python_io.TFRecordWriter(output_path)
    image_set_path = os.path.join(os.getcwd(), image_set_dir)
    
    grouped_labels = labels.groupby('filename')
    label_sdata = namedtuple('data', ['filename', 'object'])
    label_map = label_map_util.get_label_map_dict(label_map_path)
    
    grouped_label_data = [label_data(filename, grouped_labels.get_group(x)) 
            for filename, x in zip(grouped_labels.groups.keys(), grouped_labels.groups)]
    
    for label_group in grouped_label_data:
        tf_example = create_tf_example(label_group, label_map, image_set_path)
        tfrecord_writer.write(tf_example.SerializeToString())

labels = pascal_voc_to_csv(pascal_voc_dir, csv_labels_path)

train_percent = 0.6

# group all the labels by filename (image)
labels_grouped = labels.groupby('filename')
labels_grouped_list = [labels_grouped.get_group(x) for x in labels_grouped.groups]
image_count = len(labels_grouped_list)

# get training count by specified percentage
train_count = round(image_count * train_percent)

train_indicies = np.random.choice(image_count, size=train_count, replace=False)
test_indicies = np.setdiff1d(list(range(image_count)), train_indicies)

print('Image count: ' + str(image_count) 
      + '\nTraining image count: ' + str(train_count)
      + '\nTest image count: ' + str(len(test_indicies)))

train = pd.concat([labels_grouped_list[i] for i in train_indicies])
test = pd.concat([labels_grouped_list[i] for i in test_indicies])

print('Total label count: ' + str(labels.shape[0]) 
      + '\nTraining label count: ' + str(len(train))
      + '\nTest label count: ' + str(len(test)))

train.to_csv(csv_train_labels_path, index=None)
test.to_csv(csv_test_labels_path, index=None)

label_map_path = 'label_map.pbtxt'

# TFRecord training file
create_tfrecord_file(labels, label_map_path, csv_train_labels_path, tfrecord_train_path)

# TFRecord test file
create_tfrecord_file(labels, label_map_path, csv_test_labels_path, tfrecord_test_path)



