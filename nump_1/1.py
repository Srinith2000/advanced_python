import time
import numpy as np

size_of_vec = 1000

def py_ver():
    t1= time.time()
    x = range(size_of_vec)
    y = range(size_of_vec)
    z = [x[i] + y[i] for i in range(len(x))]
    return time.time() - t1

def py_ver2():
    t1= time.time()
    x = np.arange(size_of_vec)
    y = np.arange(size_of_vec)
    z = x+y
    return time.time() - t1

t1 = py_ver()
t2 = py_ver2()
print(t1)
print(t2)
