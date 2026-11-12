
from pathlib import Path
import pandas as pd

# Locate project directory
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"

# Load processed datasets
crows = pd.read_csv(DATA_DIR / "crows_pairs_cleaned.csv")
gender = pd.read_csv(DATA_DIR / "crows_pairs_gender.csv")
wino = pd.read_csv(DATA_DIR / "winobias_processed.csv")


# ==================================
# 1. CROWS-PAIRS VALIDATION
# ==================================

print("\n========== CROWS-PAIRS VALIDATION ==========")

print("Total records:", len(crows))

print("\nMissing values:")
print(crows.isnull().sum())

print("\nDuplicate rows:", crows.duplicated().sum())

print("\nUnique bias categories:")
print(sorted(crows["bias_type"].unique()))

print("\nGender subset records:", len(gender))

print("Incorrect categories in gender subset:",
      (gender["bias_type"] != "gender").sum())


# ==================================
# 2. WINOBIAS VALIDATION
# ==================================

print("\n========== WINOBIAS VALIDATION ==========")

print("Total examples:", len(wino))

print("\nMissing values:")
print(wino.isnull().sum())

print("\nDuplicate rows:", wino.duplicated().sum())

print("\nStereotype labels:")
print(wino["stereotype_label"].value_counts())

print("\nConstruction types:")
print(wino["construction_type"].value_counts())

print("\nData splits:")
print(wino["data_split"].value_counts())

print("\nEmpty sentences:",
      wino["sentence"].isnull().sum() +
      (wino["sentence"].str.strip() == "").sum())


print("\n========== VALIDATION FINISHED ==========")
