
from pathlib import Path
import pandas as pd
import re

# 1. Locate project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Locate WinoBias folder
winobias_folder = BASE_DIR / "data" / "winobias"

# 3. Output folder
processed_folder = BASE_DIR / "data" / "processed"
processed_folder.mkdir(parents=True, exist_ok=True)

records = []

# 4. Read all WinoBias files
for file in sorted(winobias_folder.glob("*.txt.*")):

    # Extract information from filename
    match = re.match(
        r"^(pro|anti)_stereotyped_(type1|type2)\.txt\.(dev|test)$",
        file.name
    )

    if not match:
        print("Skipping unexpected filename:", file.name)
        continue

    stereotype_label = match.group(1)
    construction_type = match.group(2)
    data_split = match.group(3)

    # Read examples
    with open(file, "r", encoding="utf-8") as f:

        for line in f:

            line = line.strip()

            if not line:
                continue

            # Separate example ID and sentence
            example_match = re.match(r"^(\d+)\s+(.*)$", line)

            if not example_match:
                print("Skipping unexpected line:", line)
                continue

            example_id = int(example_match.group(1))
            sentence = example_match.group(2)

            records.append({
                "example_id": example_id,
                "sentence": sentence,
                "stereotype_label": stereotype_label,
                "construction_type": construction_type,
                "data_split": data_split,
                "source_file": file.name
            })

# 5. Create DataFrame
winobias_data = pd.DataFrame(records)

# 6. Display results
print("\n========== WINOBIAS PREPROCESSING ==========")

print("\nDataset dimensions:")
print(winobias_data.shape)

print("\nStereotype distribution:")
print(winobias_data["stereotype_label"].value_counts())

print("\nConstruction type distribution:")
print(winobias_data["construction_type"].value_counts())

print("\nData split distribution:")
print(winobias_data["data_split"].value_counts())

print("\nFirst five examples:")
print(winobias_data.head())

# 7. Save processed dataset
output_file = processed_folder / "winobias_processed.csv"

winobias_data.to_csv(output_file, index=False)

print("\nProcessed WinoBias dataset saved!")
print("Location:", output_file)
