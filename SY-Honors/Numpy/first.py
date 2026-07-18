# import numpy 

# arr = numpy.array([1, 2, 3, 4, 5])

# print("Original array:", arr)
# print("First element:", arr[0])


import numpy as np
arr = np.array([1,2,3,4,5])
arr1 = np.array((1,2,3,4,5)) # convert tuple into array

print(np.__version__)

print(arr)
print(type(arr)) # <class 'numpy.ndarray'>
print(arr1)


# Dimensions in arrays

#0-D
arr2 = np.array(24) # Each value in an array is a 0-D array
print("\n0-D array:") 
print(arr2)

#1-D
arr3 = np.array([1,2,3,4,5])
print("\n1-D array:")
print(arr3)

#2-D
arr4 = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2-D array:") 
print(arr4)

#3-D
arr5 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("\n3-D array:")
print(arr5)

print("\nNumber of dimensions:")
print(arr2.ndim)  # prints the number of dimensions of the array
print(arr3.ndim)
print(arr4.ndim)
print(arr5.ndim)

#Higher dimensional arrays
arr6 = np.array([1, 2, 3, 4], ndmin=3)
print("\nArray with 3 dimensions:")
print(arr6)
print("Number of dimensions:", arr6.ndim)

arr7 = np.array([1, 2, 3, 4], ndmin=5)
print("\nArray with 5 dimensions:")   
print(arr7)
print("Number of dimensions:", arr7.ndim)

# Changing the data type of an array
arr8 = np.array([1, 2, 3, 4], dtype=complex) # set data type to complex
print("\nArray with complex data type:")  
print(arr8)
print("Data type of the array:", arr8.dtype)

arr9 = np.array([1.5, 2.5, 3.5], dtype=int) # set data type to integer
print("\nArray with integer data type:")
print(arr9)
print("Data type of the array:", arr9.dtype)

arr10 = np.array([[1, 2, 3], [4, 5, 6]], dtype=float) # set data type to float
print("\nArray with float data type:")  
print(arr10)
print("Data type of the array:", arr10.dtype)

# Array Size and shape
arr11 = np.array([[1, 2, 3], [4, 5, 6]])
print("\nArray:")
print(arr11)
print("Shape of the array:", arr11.shape)
print("Size of the array:", arr11.size)

# Array indexing
arr12 = np.array([10, 20, 30, 40, 50])
print("\nArray for indexing:")
print(arr12)
print("First element:", arr12[0])
print("Last element:", arr12[-1])
print("Elements from index 1 to 3:", arr12[1:4])

# 2-D array indexing
arr13 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2-D Array for indexing:")
print(arr13)
print("Element at row 1, column 2:", arr13[1, 2])
print("First row:", arr13[0]) 
print("Second column:", arr13[:, 1])
print("Sub-array from row 0-1 and column 1-2:")
print(arr13[0:2, 1:3])
