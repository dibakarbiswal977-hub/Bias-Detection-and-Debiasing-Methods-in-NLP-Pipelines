
import requests
from pathlib import Path

# Find the main project directory
BASE_DIR = Path(__file__).resolve().parent

# Create dataset folders
WINOBIAS_DIR = BASE_DIR / "data" / "winobias"
CROWS_DIR = BASE_DIR / "data" / "crows_pairs"

WINOBIAS_DIR.mkdir(parents=True, exist_ok=True)
CROWS_DIR.mkdir(parents=True, exist_ok=True)


def download_file(url, destination):

    print(f"\nDownloading: {destination.name}")

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        destination.write_bytes(response.content)

        print(f"Successfully downloaded: {destination.name}")

    except requests.RequestException as error:
        print(f"Download failed: {error}")


# WinoBias dataset files
winobias_files = [
    "anti_stereotyped_type1.txt.dev",
    "anti_stereotyped_type1.txt.test",
    "anti_stereotyped_type2.txt.dev",
    "anti_stereotyped_type2.txt.test",
    "pro_stereotyped_type1.txt.dev",
    "pro_stereotyped_type1.txt.test",
    "pro_stereotyped_type2.txt.dev",
    "pro_stereotyped_type2.txt.test"
]

WINOBIAS_URL = (
    "https://raw.githubusercontent.com/"
    "uclanlp/corefBias/master/WinoBias/wino/data/"
)

print("\n========== WINOBIAS DATASET ==========")

for filename in winobias_files:

    url = WINOBIAS_URL + filename
    destination = WINOBIAS_DIR / filename

    download_file(url, destination)


# CrowS-Pairs dataset
crows_url = (
    "https://raw.githubusercontent.com/"
    "nyu-mll/crows-pairs/master/data/"
    "crows_pairs_anonymized.csv"
)

crows_destination = CROWS_DIR / "crows_pairs_anonymized.csv"

print("\n========== CROWS-PAIRS DATASET ==========")

download_file(crows_url, crows_destination)


# Final message
print("\n========== DOWNLOAD SUMMARY ==========")

print("WinoBias folder:", WINOBIAS_DIR)
print("CrowS-Pairs folder:", CROWS_DIR)

print("\nDataset downloading process completed!")
