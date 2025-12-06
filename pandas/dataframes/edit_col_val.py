import pandas as pd
'''
#direct new value insert 

df.loc[row_index,"col_name"] =values




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
print("=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-==----=")
#Edit col, directly
df.loc[1,"salary"] =9000000
print(df)
#updating col values

df["salary"] += df['salary'] * 0.1
print(df)