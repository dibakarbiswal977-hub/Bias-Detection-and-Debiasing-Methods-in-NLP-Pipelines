
from pathlib import Path
import pandas as pd

# 1. Locate the main project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Locate the original dataset
crows_file = (
    BASE_DIR / "data" / "crows_pairs"
    / "crows_pairs_anonymized.csv"
)

# 3. Create a folder for processed data
processed_folder = BASE_DIR / "data" / "processed"
processed_folder.mkdir(parents=True, exist_ok=True)

# 4. Load the original dataset
data = pd.read_csv(crows_file)

print("========== ORIGINAL DATASET ==========")
print("Dataset dimensions:", data.shape)

# 5. Remove the unnecessary CSV index column
data = data.drop(columns=["Unnamed: 0"], errors="ignore")

# 6. Display all bias categories
print("\n========== BIAS CATEGORY DISTRIBUTION ==========")

category_counts = data["bias_type"].value_counts()

print(category_counts)

# 7. Display category percentages
print("\n========== CATEGORY PERCENTAGES ==========")

category_percentages = (
    data["bias_type"].value_counts(normalize=True) * 100
)

print(category_percentages.round(2))

# 8. Compare stereotype and anti-stereotype counts
print("\n========== STEREOTYPE DISTRIBUTION ==========")

stereotype_counts = pd.crosstab(
    data["bias_type"],
    data["stereo_antistereo"]
)

print(stereotype_counts)

# 9. Check missing values
print("\n========== MISSING VALUES ==========")

print(data.isnull().sum())

# 10. Extract gender records for detailed analysis
gender_data = data[data["bias_type"] == "gender"].copy()

print("\n========== GENDER SUBSET ==========")
print("Gender records:", len(gender_data))

# 11. Save the complete cleaned dataset
all_output = processed_folder / "crows_pairs_cleaned.csv"

data.to_csv(all_output, index=False)

# 12. Save the gender subset separately
gender_output = processed_folder / "crows_pairs_gender.csv"

gender_data.to_csv(gender_output, index=False)

print("\n========== SAVING RESULTS ==========")

print("All categories saved to:", all_output)
print("Gender subset saved to:", gender_output)

print("\nCrowS-Pairs inspection completed!")
