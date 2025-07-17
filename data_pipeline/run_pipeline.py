import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from pipeline.process import process_market_data
from db.save_to_db import save_data_to_db

def main():
    # Automatically pick the latest file in data/raw
    raw_dir = Path("data/raw")
    files = sorted(raw_dir.glob("market_data_*.json"), reverse=True)
    
    if not files:
        print("❌ No raw market data files found.")
        return
    
    latest_file = files[0]
    print(f"🚀 Using latest market file: {latest_file.name}")

    cleaned_data = process_market_data(latest_file)
    save_data_to_db(cleaned_data)

if __name__ == "__main__":
    main()
