import atexit
import numpy as np
from os import environ

ENV_KEY = 'TENSOR_SAVER_PATH'

_objs = []
_out_path = './debug.npz'
if ENV_KEY in environ:
    _out_path = environ[ENV_KEY]


def add(obj):
    _objs.append(obj)

def set_out_path(path):
    global _out_path
    _out_path = path


def save():
    dobjs= {}
    for i in range(len(_objs)):
        name = 'obj_' + str(i).zfill(6)
        dobjs[name] = _objs[i]
    np.savez(_out_path, **dobjs)

def _on_exit():
    if len(_objs) != 0:
        save()

atexit.register(_on_exit)
