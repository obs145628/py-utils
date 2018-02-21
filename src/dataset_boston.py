import sklearn.datasets
import numpy as np
import pickle


TRAIN_TEST_FILE = './boston.bin'

def sep_train_test(data, target, train_len, test_len):
    total_len = train_len + test_len

    arr = list(zip(data, target))
    np.random.shuffle(arr)
    arr = arr[:total_len]
    train = arr[:train_len]
    test = arr[train_len:]

    X_train, y_train = zip(*train)
    X_test, y_test = zip(*test)

    return np.array(X_train), np.array(y_train), np.array(X_test), np.array(y_test)


def load_dataset():
    print('Downloading dataset...')
    ds = sklearn.datasets.load_boston()
    X = ds.data
    y = ds.target
    data = (X, y)
    with open(TRAIN_TEST_FILE, 'wb') as f:
        pickle.dump(data, f)
    print('Dataset downloaded')
    return data


def load_data():
    try:
        f = open(TRAIN_TEST_FILE, 'rb')
    except IOError:
        return load_dataset()
    with f:
        return pickle.load(f)

def load_boston():
    return load_data()
