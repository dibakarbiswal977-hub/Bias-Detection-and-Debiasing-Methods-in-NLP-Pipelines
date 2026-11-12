
from pathlib import Path
import pandas as pd

# Find the project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Dataset paths
crows_file = BASE_DIR / "data" / "crows_pairs" / "crows_pairs_anonymized.csv"
winobias_folder = BASE_DIR / "data" / "winobias"

# ==================================
# 1. LOAD CROWS-PAIRS
# ==================================

print("\n========== CROWS-PAIRS ==========")

crows_data = pd.read_csv(crows_file)

print("\nDataset dimensions:")
print(crows_data.shape)

print("\nColumn names:")
print(crows_data.columns.tolist())

print("\nBias categories:")
print(crows_data["bias_type"].value_counts())

print("\nFirst five records:")
print(crows_data.head())


# ==================================
# 2. LOAD WINOBIAS
# ==================================

print("\n========== WINOBIAS ==========")

for file in sorted(winobias_folder.glob("*.txt.*")):

    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print("\nFile:", file.name)
    print("Number of examples:", len(lines))

    print("First two examples:")
    for line in lines[:2]:
        print(line.strip())
