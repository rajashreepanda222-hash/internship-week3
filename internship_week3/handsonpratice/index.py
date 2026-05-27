import pandas as pd
data = pd.read_csv("students.csv")

print("First 5 Rows:")
print(data.head())


print("\nShape of Dataset:")
print(data.shape)


print("\nData Types:")
print(data.dtypes)


print("\nDataset Info:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())


data["Science"] = data["Science"].fillna(data["Science"].mean())
data["English"] = data["English"].fillna(data["English"].mean())

print("\nUpdated Dataset:")
print(data)


print("\nAverage Marks:")
print(data.mean(numeric_only=True))


print("\nHighest Marks:")
print(data.max(numeric_only=True))


print("\nLowest Marks:")
print(data.min(numeric_only=True))