import numpy as np

# printing numbers from 1 to 10 with 7 values
print(np.linspace(1, 10, 10))

# printing numbers from 1 to 10 with 7 values
print(np.linspace(1, 10, 7))

# printing numbers from 1 to 10 by excluding the last value
print(np.linspace(1, 10, 7 , endpoint = False))

# printing the step size
print(np.linspace(1, 10, 7, endpoint = True, retstep=True))
print(np.linspace(1, 10, 7, endpoint = False, retstep=True))
