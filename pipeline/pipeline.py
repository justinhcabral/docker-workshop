'''
This is a basic data pipeline that will get some input and produce some output
'''
import sys

import pandas as pd # pandas is a library for data processing

print("arguments", sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"day": [1, 2], "num_passengers": [3, 4]})
df["month"] = month
print(df.head())

df.to_parquet(f"output_month_{month}.parquet")

print(f"hello pipeline, month={month}")

# the reason why this is a pipeline is that it can be run with different inputs and produce different outputs. For example, you can run this pipeline with month=1 and it will produce a file called output_month_1.parquet, and you can run it with month=2 and it will produce a file called output_months_2.parquet. a pipeline is basically a series of steps that take some input and produce some output. In this case, the input is the month and the output is a parquet file with the number of passengers for that month.