import os
from pathlib import Path
import kaggle
from dotenv import load_dotenv

def setup_kaggle_auth():
    """Setup Kaggle authentication from environment variables."""
    load_dotenv()
    
    username = os.getenv('KAGGLE_USERNAME')
    key = os.getenv('KAGGLE_KEY')
    
    if username and key:
        os.environ['KAGGLE_USERNAME'] = username
        os.environ['KAGGLE_KEY'] = key
        print("✅ Kaggle credentials loaded from environment")
    else:
        print("⚠️ No Kaggle credentials in environment, checking for kaggle.json...")

def download_telco_data():
    """Download and extract Telco customer churn dataset."""
    setup_kaggle_auth()
    
    data_dir = Path("src/data/raw")
    data_dir.mkdir(parents=True, exist_ok=True)
    
    dataset_file = data_dir / "WA_Fn-UseC_-Telco-Customer-Churn.csv"
    
    if dataset_file.exists():
        print(f"✅ Dataset already exists at {dataset_file}")
        return
    
    try:
        print("📥 Downloading Telco dataset from Kaggle...")
        kaggle.api.dataset_download_files(
            'blastchar/telco-customer-churn',
            path=data_dir,
            unzip=True
        )
        print(f"✅ Dataset downloaded to {data_dir}")
    except Exception as e:
        print(f"❌ Error downloading dataset: {e}")
        print("Please check your Kaggle credentials and try again.")

if __name__ == "__main__":
    download_telco_data()