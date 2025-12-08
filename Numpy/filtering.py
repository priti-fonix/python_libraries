#------- boolean masking ----------- (true,false) --
# filtering through codn.

import numpy as np

arr = np . array([10,20,304,50,50,607,70,80,90])

print(arr[arr >50 ])

# reshaping and manipulating array

'''
reshape(rows,cols) specify new shape
if dimension matches
it returns a view(change reflect in old array)''' 

print(arr.reshape(3,3))