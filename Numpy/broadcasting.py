import numpy as np
prices = np.array([100,300,500])

discount = 10 #scalar single value

final_prices = prices - (prices * discount/100)

print(final_prices)

print("-------- broadcasting ------------")
'''
broadcasting  ke 3 rules:-
1. check size
2. expand the single arr

3.incompatible shapes
'''
f_arr = np.array([[100,300,500],[3,4,5]])
s_arr = np.array([[2,3,4]])

sum_arr = f_arr + s_arr

print(sum_arr)
