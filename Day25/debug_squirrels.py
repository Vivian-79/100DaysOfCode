import os
import pandas as pd

# 1) Where are we running from?
print("CWD:", os.getcwd())
print("Files in this folder:", os.listdir("."))

# 2) Can pandas actually see & read your CSV?
try:
    df = pd.read_csv("Squirrel_data.csv", encoding="utf-8")
    print("✔️ read_csv succeeded")
except Exception as e:
    print("❌ read_csv FAILED with:", e)
    raise

# 3) What did pandas load?
print("DataFrame shape:", df.shape)
print("Columns:", df.columns.tolist())
print("First 3 rows:\n", df.head(3), sep="")

# 4) Is the fur-color column really there?
col = "Primary Fur Color"
if col not in df.columns:
    print(f"⚠️ Column {col!r} NOT found. Did you misspell it or include extra whitespace?")
    print("Exact column headers:", [repr(c) for c in df.columns])
    exit(1)

# 5) What are the exact unique values in that column?
uniques = df[col].dropna().unique()
print(f"Unique values in {col!r}:", [repr(u) for u in uniques])

# 6) Now apply your filter and see how many rows match
mask = df[col].astype(str).str.strip() == "Gray"
print("Number of rows where Primary Fur Color == 'Gray':", mask.sum())
print("Sample matching rows:\n", df[mask].head())