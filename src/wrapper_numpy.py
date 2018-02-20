import numpy as np

def random_randn(size):
    vec = np.random.randn(size)
    return vec.tolist()

def random_seed(s):
    np.random.seed(s)

    
if __name__=='__main__':
    random_seed(12)
    arr = random_randn(5)
    print(arr)
