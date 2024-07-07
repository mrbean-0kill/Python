import numpy as np
arr = []
for i in range(12):
    print(f"Enter element:{i+1}")
    a = int(input())
    arr.append(a)

array = np.array(arr)
array_2D = array.reshape(3,4)
array_3D = array.reshape(1,3,4)
print("2D array:\n",array_2D)
print("3D array:\n",array_3D)