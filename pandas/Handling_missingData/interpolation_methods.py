import pandas as pd
import numpy as np

# Sample data with missing values
data = pd.DataFrame({
    "value": [1, np.nan, 4, np.nan, 10]
})

print("Original Data:\n", data, "\n")

methods = [
    "linear", "time", "index", "values",
    "nearest","zero", "slinear",
    "quadratic",
     # "cubic",
    "polynomial", "spline",
    "ffill", "bfill", "pchip", "akima"
]

# For time method, set a DatetimeIndex
data_time = data.copy()
data_time.index = pd.date_range("2025-01-01", periods=len(data))

for m in methods:
    try:
        if m in ["time"]:
            result = data_time.interpolate(method=m)
        elif m in ["polynomial", "spline"]:
            result = data.interpolate(method=m, order=2)
        else:
            result = data.interpolate(method=m)

        print(f"Method: {m}")
        print(result, "\n")

    except Exception as e:
        print(f"Method {m} failed → {e}\n")
