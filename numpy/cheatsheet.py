import numpy as np

# 1. Creating a one dimensional array

# a. Create a numpy array from the list
li = [1, 2, 3, 4]
print(np.array(li))

# b. Create a NumPy array from a tuple
tup = (5, 6, 7, 8)
print(np.array(tup))

# c. create a numpy array using fromiter()
itertable = (a for a in range(8))
print(np.fromiter(itertable, float))

# 2. Creating a Multi - Dimensional Array
# a. Create a NumPy array from a list
list_1 = [1, 2, 3, 4]
list_2 = [5, 6, 7, 8]
list_3 = [9, 10, 11, 12]
print(np.array([list_1, list_2, list_3]))

# b. Create a NumPy array using numpy.empty()
print(np.empty([4, 3], dtype = int))

# 3. Initial Placeholders (1-D array)
# a. Create a NumPy array using numpy.arange()
print(np.arange(1, 10))

# b. Create a NumPy array using numpy.linspace()
print(np.linspace(1, 10, 3))

# c. Create a numpy array using numpy.zeros()
print(np.zeros(5, dtype = int))

# d. Create a NumPy array usnig numpy.ones()
print(np.ones(5, dtype = int))

# e. Create a NumPy array using numpy.random.rand()
print(np.random.rand(5))

# f. Create a NumPy array using numpy.random.randint()
print(np.random.randint(5, size = 10))


# 4. Initial Placeholders (N-dimensional Numpy Arrays)
# a. Create a NumPy array using numpy.zeros()
print(np.arange(1, 10))

# b. Create a NumPy array using numpy.ones()
print(np.ones([4, 3], dtype=np.int32))

# c. create a numpy array using numpy.full()
print(np.full([2, 2], 67, dtype = int))

# d. Create a NumPy array usnig numpy.eye()
print(np.eye(4)) # eye() function is used  to return a 2-D array with ones on the diagonal and zeros elsewhere

# 5. Inspecting Properties
# a. Size
arr = np.ones([4, 3])
print(arr.size)

# b. Length
print(len(arr))

# c. Shape
print(arr.shape)

# d. Data Type
print(arr.dtype)

# e. Changing Data Type of Array
arr.astype('float64')
print(arr.dtype)

# f. Convert array to list
l = arr.tolist()
print(l)

# 6. Data Types
# Signed 64-bit integer - np.int64
# Standard double-precision floating point - np.float32
# Complex numbers represented by 128 floats - np.complex
# Boolean type storing True and False values - np.bool
# Python object type = np.object
# Fixed length string type - np.string_
# Fixed length unicode type - np.unicode_

# 7. Sorting array
# a. Sort 1D array
a = [2, 45, 6, 89, 70]
a.sort()
print(a)

# b. Sorting along the first axis of the 2D array
print(np.sort(a, axis = 0))