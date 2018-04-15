from keras.applications.inception_v3 import InceptionV3
from keras.models import Model
from keras.layers import Dense, GlobalAveragePooling2D
from data import DataSet
import numpy as np
from PIL import Image
from sys import argv

data = DataSet()

def get_model(weights='imagenet'):
    # create the base pre-trained model
    base_model = InceptionV3(weights=weights, include_top=False)

    # add a global spatial average pooling layer
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    # let's add a fully-connected layer
    x = Dense(1024, activation='relu')(x)
    # and a logistic layer
    predictions = Dense(len(data.classes), activation='softmax')(x)

    # this is the model we will train
    model = Model(inputs=base_model.input, outputs=predictions)
    return model

if __name__ == '__main__':
    #file_name_range = ['./data/train/TaiChi/v_TaiChi_g08_c01-000' + str(i) for i in range(1,9)]
    file_class_set = {}
    class_need = ['applying eye makeup', 'applying lipstick', 'playing basketball', 'playing basketball dunk', 'doing bench press', 'biking', \
                  'blowing dry hair', 'blowing candles', 'doing body weight squats', 'brushing teeth', 'cutting in kitchen', \
                  'drumming', 'cutting hair', 'doing hand stand pushups', 'doing head massage', 'playing hula hoop', 'juggling balls', 'playing jump rope', \
                  'jumping jack', 'knitting', 'mopping floor', 'playing guitar', 'playing piano', 'playing pommel horse', \
                  'doing pull ups', 'doing push ups', 'SalsaSpin', 'shaving beard', 'playing soccer juggling', 'playing table tennis', 'playing TaiChi',\
                  'swing tennis', 'typing', 'doing wall push ups', 'writing on board']
    #for file_name in file_name_range
    img_name=argv[1]
    tmp = Image.open(img_name)
    tmp = tmp.resize([299,299])
    tmp_np = np.array(tmp) / 255.0
    model = get_model()
    model.load_weights('../../motion_recog/data/checkpoints/inception.008-0.98.hdf5')
    result = model.predict(np.array([tmp_np]), batch_size=1)
    result = result.reshape([len(result[0])])
    result_class = (class_need)[result.tolist().index(max(result))]
    if result_class in file_class_set:
        file_class_set[result_class] += 1
    else:
        file_class_set[result_class] = 1
    max_class = -1
    max_num = -1
    for file_class in file_class_set:
        if file_class_set[file_class] > max_num:
            max_class = file_class
            max_num = file_class_set[file_class]
    print(max_class)
