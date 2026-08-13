import numpy as np

# here we are just printing numbers from 1 to 10 without any step (remember: the stop value is always excluded)
x = np.arange(1, 10)
print(x)
print("\n")

# here we are printing float values from 1 to 10.4 with a step value of 1.4
x = np.arange(1,10.4 , 1.4)
print(x)
print("\n")

# here we are again printing values from 1 to 10 with a step 2, we are also specifying the dtype
x = np.arange(1, 10,2, dtype = int)
print(x)

x = np.arange(0.5, 10, 0.5, dtype = int)
print(x)