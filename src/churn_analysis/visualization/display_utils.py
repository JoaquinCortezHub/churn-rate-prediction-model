# src/churn_analysis/visualization/display_utils.py
"""
Display utilities for beautiful table formatting and data presentation.
"""

import pandas as pd
import polars as pl
from rich.console import Console
from rich.table import Table
from rich import box
from typing import Optional, List, Union


def create_rich_table(
    df: Union[pl.DataFrame, pd.DataFrame], 
    title: str = "Analysis Results", 
    money_columns: Optional[List[str]] = None,
    percentage_columns: Optional[List[str]] = None,
    integer_columns: Optional[List[str]] = None
) -> None:
    """
    Create a beautiful table using Rich library.
    
    Args:
        df: Polars or Pandas DataFrame to display
        title: Table title
        money_columns: List of column names to format as currency
        percentage_columns: List of column names to format as percentages
        integer_columns: List of column names to format as integers
    """
    
    console = Console()
    
    # Create table with styling
    table = Table(
        title=f"📊 {title}",
        box=box.ROUNDED,
        show_header=True,
        header_style="white",
        title_style="bold green",
        show_lines=True,
        expand=False
    )
    
    # Convert to pandas if it's a Polars DataFrame
    if isinstance(df, pl.DataFrame):
        df_pandas = df.to_pandas()
    else:
        df_pandas = df.copy()
    
    # Initialize column lists if None
    money_columns = money_columns or []
    percentage_columns = percentage_columns or []
    integer_columns = integer_columns or []
    
    # Auto-detect percentage columns if not specified
    if not percentage_columns:
        percentage_columns = [col for col in df_pandas.columns 
                            if 'rate' in col.lower() or 'percentage' in col.lower()]
    
    # Add columns with appropriate justification
    for col in df_pandas.columns:
        if col in money_columns or col in percentage_columns or col in integer_columns:
            justify = "right"
        elif df_pandas[col].dtype in ['object', 'string']:
            justify = "left"
        else:
            justify = "center"
            
        table.add_column(
            col.replace("_", " ").title(), 
            justify=justify,
            style="dim" if col in integer_columns else None
        )
    
    # Add rows with formatting
    for _, row in df_pandas.iterrows():
        formatted_row = []
        for col in df_pandas.columns:
            value = row[col]
            
            # Format based on column type
            if pd.isna(value):
                formatted_value = "[dim]N/A[/dim]"
            elif col in money_columns:
                formatted_value = f"[green]${value:,.0f}[/green]" if isinstance(value, (int, float)) else str(value)
            elif col in percentage_columns:
                if isinstance(value, (int, float)):
                    color = "red" if value > 30 else "yellow" if value > 20 else "green"
                    formatted_value = f"[{color}]{value:.1f}%[/{color}]"
                else:
                    formatted_value = str(value)
            elif col in integer_columns:
                formatted_value = f"{int(value):,}" if isinstance(value, (int, float)) else str(value)
            elif isinstance(value, float):
                formatted_value = f"{value:,.2f}"
            elif isinstance(value, int):
                formatted_value = f"{value:,}"
            else:
                formatted_value = str(value)
                
            formatted_row.append(formatted_value)
        
        table.add_row(*formatted_row)
    
    console.print(table)
    print()  # Add spacing after table


def display_insights_summary(insights: List[str], title: str = "Key Insights") -> None:
    """
    Display a list of insights in a formatted way.
    
    Args:
        insights: List of insight strings
        title: Title for the insights section
    """
    console = Console()
    
    # Create insights panel
    from rich.panel import Panel
    from rich.text import Text
    
    insight_text = Text()
    for i, insight in enumerate(insights, 1):
        insight_text.append(f"{i}. {insight}\n", style="bold white")
    
    panel = Panel(
        insight_text,
        title=f"💡 {title}",
        border_style="blue",
        padding=(1, 2)
    )
    
    console.print(panel)
    print()


def display_business_alert(
    message: str, 
    alert_type: str = "warning", 
    details: Optional[List[str]] = None
) -> None:
    """
    Display business alerts with appropriate styling.
    
    Args:
        message: Main alert message
        alert_type: Type of alert ('warning', 'critical', 'success', 'info')
        details: Optional list of additional details
    """
    console = Console()
    
    # Style mapping
    styles = {
        "warning": {"border": "yellow", "title": "⚠️ Warning", "text": "yellow"},
        "critical": {"border": "red", "title": "🚨 Critical Alert", "text": "red"},
        "success": {"border": "green", "title": "✅ Success", "text": "green"},
        "info": {"border": "blue", "title": "ℹ️ Information", "text": "blue"}
    }
    
    style = styles.get(alert_type, styles["info"])
    
    # Create alert content
    from rich.panel import Panel
    from rich.text import Text
    
    alert_text = Text()
    alert_text.append(f"{message}\n", style=f"bold {style['text']}")
    
    if details:
        alert_text.append("\nDetails:\n", style="bold")
        for detail in details:
            alert_text.append(f"• {detail}\n", style=style['text'])
    
    panel = Panel(
        alert_text,
        title=style['title'],
        border_style=style['border'],
        padding=(1, 2)
    )
    
    console.print(panel)
    print()