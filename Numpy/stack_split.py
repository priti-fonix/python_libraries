"""
vstack() -> row wise
hstack() -> col wise
"""

import numpy as np

# arr1 = np.array([10,20,30,40,50,60,70])
# arr2 = np.array([100,200,300,400,500,600,700])

# vstacked_arr = np.vstack((arr1,arr2))
# print(vstacked_arr)
# hstacked_arr = np.hstack((arr1,arr2))
# print(hstacked_arr)

#---------------------- splitting --------------------

'''
.split() -> equal
.vsplit() -> vertically
.hsplit() -> horizontally

'''
arr1 = np.array([10,20,30,40,50,60,70,80])
eq_split_arr = np.split(arr1,2)
arr_2d = np.reshape(arr1,shape =(2,4))
v_Split_arr = np.vsplit(arr_2d,1)
h_Split_arr = np.hsplit(arr_2d,1)

print(eq_split_arr)
print(v_Split_arr)
print(h_Split_arr)