import pandas as pd

# load dataset
df = pd.read_csv("data/data.csv")

# remove extra spaces from column names
df.columns = df.columns.str.strip()

print("COLUMN NAMES:")
print(df.columns)
print()

print("FIRST 5 ROWS:")
print(df.head())
print()

# replace ? with real missing values
df = df.replace("?", pd.NA)

print("MISSING VALUES AFTER REPLACING ?:")
print(df.isnull().sum())
print()

print("DUPLICATES BEFORE REMOVAL:", df.duplicated().sum())
df = df.drop_duplicates()
print("DUPLICATES AFTER REMOVAL:", df.duplicated().sum())
print()

# rename num to target
df = df.rename(columns={"num": "target"})

print("COLUMN NAMES AFTER RENAME:")
print(df.columns)
print()

# columns that should be numeric
numeric_columns = [
    "age", "sex", "cp", "trestbps", "chol", "fbs",
    "restecg", "thalach", "exang", "oldpeak",
    "slope", "ca", "thal", "target"
]

# convert columns to numeric
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

print("DATA TYPES AFTER CONVERSION:")
print(df.dtypes)
print()

print("MISSING VALUES AFTER CONVERSION:")
print(df.isnull().sum())
print()

print("SUMMARY STATS:")
print(df.describe())
print()

# for this dataset, drop columns with too many missing values
df = df.drop(columns=["slope", "ca", "thal"])

# drop remaining rows with missing values
df_clean = df.dropna()

print("ROWS BEFORE CLEANING:", len(df))
print("ROWS AFTER DROPPING MISSING VALUES:", len(df_clean))
print()

# save cleaned file
df_clean.to_csv("data/heart_clean.csv", index=False)

print("Cleaned file saved as data/heart_clean.csv")