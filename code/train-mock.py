# -*- coding: utf-8 -*-
# Mock-up ML training

import datetime
import fnmatch
import os
import time


def list_dir(dir, pattern='*.csv'):
    listOfFiles = os.listdir(dir)
    fn = []
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            fn.append(entry)
    return fn


BASE_DIR = os.path.dirname(os.path.dirname((os.path.realpath(__file__))))
app_data_dir = BASE_DIR + '/data/'
data_dir = list_dir(app_data_dir, '*.csv')
model_dir = BASE_DIR + '/models/'
model_name = 'model_2021.tgz'
model_type = 'SVM'
note = 'some note or another input argument'
sleep_loop = 10


def set_train_args():
    train_args = {
        'data': {
            'default': data_dir,
            'help': 'Training data to train on',
            'required': False
        },
        'model_dir': {
            'default': model_dir,
            'help': 'Dir to store trained models',
            'required': False
        },
        'model_name': {
            'default': model_name,
            'help': 'Name of the model to train',
            'type': str,
            'required': False
        },
        'model_type': {
            'default': model_type,
            'help': 'Training method e.g. SVM',
            'required': False
        },
        'note': {
            'default': note,
            'help': '',
            'required': False
        }
    }
    return train_args


def training():
    train_args = set_train_args()
    for key, val in train_args.items():
        val['default'] = str(val['default'])
        print(val['default'], type(val['default']))
    print('\n', train_args)

    print('\nLong training process ... ')
    for i in range(sleep_loop):
        time.sleep(1)
        print(i, end=' ')
    print('\nSaved ...', model_dir + model_name)

    return


if __name__ == "__main__":
    # timestamp
    timer_start = datetime.datetime.now()

    training()

    # runtime report
    print('\nRuntime =', datetime.datetime.now() - timer_start)
