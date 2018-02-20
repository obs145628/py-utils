import numpy as np

def write_mat(os, m):
    r = m.shape[0]
    c = m.shape[1]

    os.write(str(r) + '\n')
    os.write(str(c) + '\n')

    for i in range(r):
        for j in range(c):
            os.write(str(m[i][j]) + '\n')

def write_tensor(os, m):
    os.write(str(len(m.shape)) + '\n')
    for d in m.shape:
        os.write(str(d) + '\n')

    for x in m.flatten():
        os.write(str(x) + '\n')

def load_tensor(iss):

    ndims = int(iss.readline())
    dims = []
    size = 1
    for _ in range(ndims):
        dim = int(iss.readline())
        size *= dim
        dims.append(dim)

    dims = tuple(dims)
    vect = np.zeros(size)

    for i in range(size):
        vect[i] = float(iss.readline())
    
    return vect.reshape(dims)

def load_tensors(iss):

    n = int(iss.readline())
    res = []
    for _ in range(n):
        res.append(load_tensor(iss))
    return res
    
    ndims = int(iss.readline())
    dims = []
    size = 1
    for _ in range(ndims):
        dim = int(iss.readline())
        size *= dim
        dims.append(dim)

    dims = tuple(dims)
    vect = np.zeros(size)

    for i in size:
        vect[i] = float(iss.readline())
    
    return vect.reshape(shape)
        

def write_mats(os, mats):
    os.write(str(len(mats)) + '\n')
    for m in mats:
        write_mat(os, m)


def write_tensors(os, ts):
    os.write(str(len(ts)) + '\n')
    for t in ts:
        write_tensor(os, t)
