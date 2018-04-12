import numpy as np

def rand_upper_mat(size, min_val, max_val):
    m = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i <= j:
                m[i][j] = np.random.rand() * (max_val - min_val) + min_val
    return m

def rand_lower_mat(size, min_val, max_val):
    m = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i >= j:
                m[i][j] = np.random.rand() * (max_val - min_val) + min_val
    return m

def rand_vect(size, min_val, max_val):
    return np.random.rand(size) * (max_val - min_val) + min_val

def rand_mat(rows, cols, min_val, max_val):
    return np.random.rand(rows, cols) * (max_val - min_val) + min_val
