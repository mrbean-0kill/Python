import numpy as np
arr = []
n = int(input("Enter number of elements for array:"))
for i in range(n):
    print(f"Enter element:{i+1}")
    a = int(input())
    arr.append(a)

array = np.array(arr)
print("Spliting of array:")
print("2 arrays:",np.array_split(array,2))
print("3 arrays:",np.array_split(array,3))
print("4 arrays:",np.array_split(array,4))

      