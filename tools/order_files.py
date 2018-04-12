'''
Usage: input_dir output_dir extension
search all dirs and subdirs in <input_dir> for files wiht extension <extension>, and move them to the root of <output_dir>
ex: order_files ./Downloads ./videos mp4 
'''

import os
import sys

in_path = sys.argv[1]
out_path = sys.argv[2]
ext = sys.argv[3]

def explore_tree_rec(path, before_dir, after_dir, file_cb):

    if before_dir: before_dir(path)

    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            explore_tree_rec(file_path, before_dir, after_dir, file_cb)
        else:
            file_cb(file_path)

    if after_dir: after_dir(path)

    

def tree_explore(path, before_dir = None, after_dir = None, file_cb = None):

    path = os.path.abspath(path)
    
    if not os.path.isdir(path):
        raise Exception('explore_tree: path is not a dir')

    explore_tree_rec(path, before_dir, after_dir, file_cb)


def tree_filter(path, pred):

    res = []

    def cb(path):
        if (pred(path)):
            res.append(path)

    tree_explore(path, file_cb = cb)
    return res

def is_valid(path):
    return os.path.splitext(path)[1] == '.' + ext

    
files = tree_filter(in_path, is_valid)

for f in files:
    name = os.path.basename(f)
    os.rename(f, os.path.join(out_path, name))
