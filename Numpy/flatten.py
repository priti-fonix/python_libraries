import numpy as np
'''
ravel() -> view ----------modifies previous array
flatten() -> copy
'''

# arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
# print(arr)

# flatten_arr = arr.ravel()
# flatten_arr += 2

# print(arr," array to \n",flatten_arr)

# flatten_arr2 = arr.flatten()
# flatten_arr2 += 2

# print(arr,"\n",flatten_arr2)

# print("---------array insertion----------")
# '''
# arr.insert(arr,iindex,value,axis:0->row=wise, 1-> col-wise)

# '''

# new_arr = np.array([[12,23,34,56],[67,78,89,90]])
# print(new_arr)
# modified_arr = np.insert(arr,2,600,0)

# print(modified_arr)
# modified_arr2 = np.insert(arr,2,600)

# print(modified_arr2)
# modified_arr3 = np.append(arr,700)
# print(modified_arr3)
# concated_arr = np.concatenate([(modified_arr2,modified_arr3)])
# print(concated_arr)

# #delete array

# '''
# np.delete(arr,index,axis =0/None/1)


# '''
# new_arr = np.delete(modified_arr,2)

# print(new_arr)
new_arr = np.array([[12,23,34,56],[67,78,89,90]])
print(new_arr)
del_arr = np.delete(new_arr,1,axis=1)
print(del_arr)