import numpy as np

arr = []
arr1 = []

a = int(input("Enter number of elements in the array: "))

for i in range(a):
    b = int(input(f"Enter element {i+1} for the first array: "))
    c = int(input(f"Enter element {i+1} for the second array: "))
    arr.append(b)
    arr1.append(c)

array = np.array(arr)
array1 = np.array(arr1)

print("1-D array 1:", array)
print(type(array))
print("1-D array 2:", array1)
print(type(array1))

common_elements = list(set(array) & set(array1))

common_elements = [int(element) for element in common_elements]

print("Common elements in both arrays => ", common_elements)
