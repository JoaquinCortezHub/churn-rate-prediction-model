# src/churn_analysis/config/settings.py
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUTS_DIR = PROJECT_ROOT / "outputs"
FIGURES_DIR = OUTPUTS_DIR / "figures"

# Data files
TELCO_RAW_FILE = RAW_DATA_DIR / "WA_Fn-UseC_-Telco-Customer-Churn.csv"

# Kaggle credentials (from environment)
KAGGLE_USERNAME = os.getenv('KAGGLE_USERNAME')
KAGGLE_KEY = os.getenv('KAGGLE_KEY')

# Visualization settings
PLOT_STYLE = "seaborn-v0_8"
FIGURE_SIZE = (12, 8)
COLOR_PALETTE = "husl"

# Analysis parameters
RANDOM_STATE = 42