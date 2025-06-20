import polars as pl
from pathlib import Path
from churn_analysis.config.settings import TELCO_RAW_FILE

def load_telco_data() -> pl.DataFrame:
    """
    Load the Telco customer churn dataset.
    
    Returns:
        pl.DataFrame: Raw Telco dataset
    """
    if not TELCO_RAW_FILE.exists():
        raise FileNotFoundError(
            f"Dataset not found at {TELCO_RAW_FILE}. "
            "Please run the download script first: "
            "uv run python scripts/download_data.py"
        )
    
    df = pl.read_csv(TELCO_RAW_FILE)
    print(f"✅ Dataset loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    return df

def get_dataset_info(df: pl.DataFrame) -> dict:
    """Get basic dataset information."""
    return {
        'shape': df.shape,
        'columns': df.columns,
        'null_count': df.null_count().sum_horizontal()[0],
        'dtypes': dict(zip(df.columns, [str(dtype) for dtype in df.dtypes]))
    }