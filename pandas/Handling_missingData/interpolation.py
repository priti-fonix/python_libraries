import pandas as pd

data = {
  "name": ["Amit Sharma","Priya Verma",None,"Neha Kapoor","Vikas Mehra","Sneha Nair","Karan Patel","Divya Reddy","Suresh Rao","Anita D'Souza"
  ],
  "age": [29, 34, None, 31, 40, 26, 33, 28, 37, 30],
  "salary": [52000, 74000, None, 69000, 80000, 45000, 62000, 57000, 76000, 60000],
  "performanceScore": [78, 92, None,83, 89, 72, 88, 76, 94, 81]
}

df = pd.DataFrame(data)
df["age"]= df["age"].interpolate(method = "linear")
print(df)