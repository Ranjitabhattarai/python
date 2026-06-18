import numpy as np
#to add the number
arr = np.array([1, 2, 5, 9])
print (arr[2] + arr[3])

# to multiply the number
arr = np.array([1, 2, 5, 9])
print (arr[2] * arr[3])

# to substract the number
arr = np.array([1, 2, 5, 9])
print (arr[2] - arr[3])

# to divide the number
arr = np.array([1, 2, 5, 9])
print (arr[2] / arr[3])


# to define out the dimension
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

#to reverse the number
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::-1])


arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:4:2])