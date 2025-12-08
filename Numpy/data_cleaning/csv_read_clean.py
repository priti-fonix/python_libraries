# import numpy as np

# data = np.loadtxt("data.csv", delimiter=",")
# print(data)

# import pandas as pd

    # dtype=None,          # auto-detect types
    # encoding="utf-8",
    # skip_header=1,
    # missing_values=["", "NaN", "None"],
    
# )

# heterogeneous_dataset_extended.csv
# D:\pythonPrograms\data_cleaning\heterogeneous_dataset_extended.csv


# print(data.head())

# print(data.isnull().sum())
''''

[5 rows x 8 columns]
id                0
name            506
salary          989
dob             469
join_date       486
performance    1049
remarks        2066
sector         1476

'''

import numpy as np
data = np.genfromtxt(
    r"D:\pythonPrograms\data_cleaning\heterogeneous_dataset_extended.csv",delimiter=',',dtype=str, skip_header=1)

# 2-d array(row) with each field(col)
ids = data[:, 0].astype(int)
names = data[:, 1]
salary = data[:, 2]
dob=data[:, 3]
join_date =data[:, 4]
performance= data[:, 5]
remarks =data[:, 6]
sector =data[:, 7]

print(ids)

missing_names = np.isin(names, ["", "None", "none", "NaN", "nan"])
print(missing_names)
'''

missing_values = ["", "unknown", "invalid_date", "—"]
clean = raw.copy()

for mv in missing_values:
    clean[clean == mv] = "nan"
salary = clean[:, 2]
salary = np.where(salary == "nan", np.nan, salary.astype(float))

'''

missing_values = ["", "unknown", "invalid_date", "—"]
clean = data.copy()

for mv in missing_values:
    clean[clean == mv] = "nan"
salary = clean[:, 2]
salary = np.where(salary == "nan", np.nan, salary.astype(float))


perf_map = {
    "excellent": 5.0,
    "good worker": 4.0,
    "promising": 4.5,
    "average": 3.0,
    "poor": 1.0,
    "needs improvement": 2.0,
    "unreliable": 1.5,
}


performance = clean[:, 5]

# convert strings → lowercase
perf_lower = np.char.lower(performance)

perf_numeric = np.full(perf_lower.shape, np.nan)

for key, val in perf_map.items():
    perf_numeric = np.where(perf_lower == key, val, perf_numeric)

# numeric values remain as float
mask_num = np.char.isnumeric(np.char.replace(perf_lower, ".", ""))
perf_numeric = np.where(mask_num, perf_lower.astype(float), perf_numeric)

# print(np.isnan(names))

































# salary = np.array(salary)
# ids = np.array(ids)
# names = np.array(names)
# dob = np.array(dob)
# join_date= np.array(join_date)
# remarks = np.array(remarks)
# sector = np.array(sector)
# performance = np.array(performance)

# salary = np.where(salary == "", "nan", salary)
# # salary = salary.astype(float)

# # salary = np.where(np.isinf(salary), np.nan, salary)
# # salary = np.nan_to_num(salary, nan=np.nanmean(salary))
# salary = np.isnan(salary)
# print(np.isnan(salary))

# print(sector)
# print(dob)
# print(performance)
# print(remarks)
# print(names)
# print(ids)
# print(join_date)

# Convert salary to float, replacing empty strings with NaN
# First replace empty strings with 'nan', then convert to float
# salary_clean = np.array([float(x) if x != '' else np.nan for x in salary])
# print(np.isnan(salary_clean))