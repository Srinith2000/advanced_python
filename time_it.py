import timeit
import numpy as np

size_of_vec = 100000000

def pure_py():
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = [X[i] + Y[i] for i in range(len(X))]

def numpy_ver():
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y

t1 = min(timeit.repeat(pure_py, number=1, repeat=5))
t2 = min(timeit.repeat(numpy_ver, number=1, repeat=5))
print("\nPython:", (timeit.repeat(pure_py, number=1, repeat=5)))
print("\nNumpy:", (timeit.repeat(numpy_ver, number=1, repeat=5)), "\n")
print(t1, t2)
print(f"Numpy is {t1-t2} seconds faster")

'''
read this to understand how timeit works:
as you know the time member function from the time library stores the timestamp (before and after) and the difference returns the time taken for the said function to fully run
timeit does something similar, but since the time library has a lot of noise, timeit improves this by running the function internally and keeps track of the time

take for example: min(stmt, number=1, repeat=5))
here timeit.repeat repeats the entire expression the specified number of times, and stores the times in an array
and stmt specifies which function to call internally, in t1 it is the function pure_py() and in t2 it is the function numpy_ver()
then number specifies the amount of times the said function needs to be called, in the above example we are only calling it once since we are already working with a large amount of elements within the function
it is then enclosed by min(), which returns the least time taken out of the said number of repetitions, since that is said to be the most accurate

you can then choose how you want to use the time, you can check how many times faster it is by using t1/t2 and how many seconds faster it is by using t1-t2

OUTPUT:

Python: [8.521020400105044, 8.564105600118637, 8.547411100007594, 8.5150704998523, 8.533503599930555]

Numpy: [0.45811980008147657, 0.47421279991976917, 0.47555009997449815, 0.4641112999524921, 0.47435809997841716] 

8.44627150008455 0.46577779995277524
Numpy is 7.980493700131774 seconds faster

'''