import pandas as pd

data ={
    "timer":[1,2,3,4,5,6,7,8],
    "value":[2,None,4,None,5,None,7,8]
}
df = pd.DataFrame(data)

df["value"]= df["value"].interpolate(method = "linear")
'''
linear interpolation uses the avg of neighbour to fill the nan data value

missing_value = (neighbr1 + neighbr2) /2

'''

print(df)

