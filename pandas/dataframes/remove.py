import pandas as pd
'''
#direct delete / remove column

df.drop(columns =[col_name1,col_name1], inplace= false/True)

false -> returns new dataframe


'''
data = {
  "name": ["Amit Sharma","Priya Verma","Rahul Singh","Neha Kapoor","Vikas Mehra","Sneha Nair","Karan Patel","Divya Reddy","Suresh Rao","Anita D'Souza"
  ],
  "age": [29, 34, 27, 31, 40, 26, 33, 28, 37, 30],
  "salary": [52000, 74000, 48000, 69000, 80000, 45000, 62000, 57000, 76000, 60000],
  "performanceScore": [78, 92, 65, 83, 89, 72, 88, 76, 94, 81]
}

df = pd.DataFrame(data)

print(df)
print("=-=-=-=-=-=-=-=-=-=  modified dataframe  -=-==-=-=-=-=-=-=-=-=-=-==----=")
# df.drop(["performanceScore"])
print(df)
#updating col values

df.drop(columns =["performanceScore"], inplace= True)
print(df)