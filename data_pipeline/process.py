from pathlib import Path
import json
from datetime import datetime

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")

def process_market_data(raw_file):
    with open(raw_file, "r") as f:
        data = json.load(f)

    print(f"🔍 Loaded {len(data)} entries from {raw_file.name}")

    cleaned_data = []
    for item in data:
        # Add the entire dict (all keys/values) to cleaned_data
        cleaned_data.append(item)
    
    # Save cleaned data to processed folder with timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    out_file = PROCESSED_DIR / f"market_data_cleaned_{timestamp}.json"

    # Ensure processed directory exists
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    with open(out_file, "w") as f:
        json.dump(cleaned_data, f, indent=2)

    print(f"✅ Saved cleaned data to {out_file.name}")

    return cleaned_data  # return after saving

if __name__ == "__main__":
    market_files = list(RAW_DIR.glob("market_data_*.json"))
    if not market_files:
        print("No market data files found to process.")
    else:
        for f in market_files:
            print(f"🚀 Processing file: {f.name}")
            process_market_data(f)
