
## Arange function
- - -
- syntax : arange([start, stop), step, dtype=None])

- np.arange returns evenly spaced values within a given interval.
- here start is included, stop is excluded
- when it is used with integers it almost acts as range()
- range() is a python built-in function
- key difference: arange returns an ndarray (N-dimensional array) ,while range returns a list
- if start is not given, it defaults to 0
- if stop is not given, it defaults to N-1

- - - 

### How the arange function works

- first the memory of the array is allocated by performing few mathematical operations 
- length = ceil((stop - start / step))
- next the array is filled with values
- it works this way because it all happens in c internally
- arange works in an unexpected way when you specify the dtype to be int and you specify the step value as a float value, since this is internally a c level array it needs to allocate memory first, so it calculates the memory size first and next it fills the memory with values by rounding off or by truncating the fractional part
- ex-

    x = np.arange(0.5, 10, 0.5, dtype = int)

    print(x)
- here the expected output is [0 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9]
- but the actual output is [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18]
- this is a well known bug in the numpy library and should be avoided 


