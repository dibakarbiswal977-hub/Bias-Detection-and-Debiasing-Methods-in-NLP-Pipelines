
from pathlib import Path
import pandas as pd

# Find the project directory
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "processed"

# Load the three processed datasets
crows = pd.read_csv(DATA_DIR / "crows_pairs_cleaned.csv")
gender = pd.read_csv(DATA_DIR / "crows_pairs_gender.csv")
wino = pd.read_csv(DATA_DIR / "winobias_processed.csv")


# =====================================
# 1. INSPECT CROWS-PAIRS
# =====================================

print("\n========== CROWS-PAIRS TEXT ==========")

print("\nFirst 3 sentence pairs:")

for index, row in crows.head(3).iterrows():
    print(f"\nExample {index + 1}")
    print("More stereotypical sentence:", row["sent_more"])
    print("Less stereotypical sentence:", row["sent_less"])
    print("Bias category:", row["bias_type"])
    print("Label:", row["stereo_antistereo"])


# =====================================
# 2. INSPECT GENDER SUBSET
# =====================================

print("\n========== GENDER SUBSET ==========")

print("Total gender examples:", len(gender))

for index, row in gender.head(3).iterrows():
    print(f"\nExample {index + 1}")
    print("Sentence A:", row["sent_more"])
    print("Sentence B:", row["sent_less"])


# =====================================
# 3. INSPECT WINOBIAS
# =====================================

print("\n========== WINOBIAS TEXT ==========")

for index, row in wino.head(5).iterrows():
    print(f"\nExample {index + 1}")
    print("Sentence:", row["sentence"])
    print("Stereotype label:", row["stereotype_label"])
    print("Construction type:", row["construction_type"])
    print("Data split:", row["data_split"])


print("\n========== INSPECTION FINISHED ==========")
