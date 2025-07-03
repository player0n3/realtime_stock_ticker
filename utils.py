"""
Utility functions for the Realtime Stock Ticker application.
Contains helper functions for data formatting, validation, and common operations.
"""

import re
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union
import pandas as pd
from config import VALID_SYMBOL_PATTERN, ERROR_MESSAGES, SUCCESS_MESSAGES

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def validate_stock_symbol(symbol: str) -> bool:
    """
    Validate if a stock symbol is in the correct format.
    
    Args:
        symbol (str): Stock symbol to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not symbol or not isinstance(symbol, str):
        return False
    
    # Convert to uppercase and remove whitespace
    symbol = symbol.strip().upper()
    
    # Check if symbol matches the pattern
    if not re.match(VALID_SYMBOL_PATTERN, symbol):
        return False
    
    return True

def format_currency(amount: Union[float, int], currency: str = "USD") -> str:
    """
    Format a number as currency.
    
    Args:
        amount (float/int): Amount to format
        currency (str): Currency code (default: USD)
        
    Returns:
        str: Formatted currency string
    """
    if amount is None:
        return "N/A"
    
    try:
        if currency == "USD":
            return f"${amount:,.2f}"
        else:
            return f"{amount:,.2f} {currency}"
    except (ValueError, TypeError):
        return "N/A"

def format_percentage(value: float, decimal_places: int = 2) -> str:
    """
    Format a number as a percentage.
    
    Args:
        value (float): Value to format as percentage
        decimal_places (int): Number of decimal places
        
    Returns:
        str: Formatted percentage string
    """
    if value is None:
        return "N/A"
    
    try:
        return f"{value:+.{decimal_places}f}%"
    except (ValueError, TypeError):
        return "N/A"

def format_large_number(value: Union[float, int]) -> str:
    """
    Format large numbers with appropriate suffixes (K, M, B, T).
    
    Args:
        value (float/int): Number to format
        
    Returns:
        str: Formatted number string
    """
    if value is None or value == 0:
        return "0"
    
    try:
        value = float(value)
        if abs(value) >= 1e12:
            return f"{value/1e12:.2f}T"
        elif abs(value) >= 1e9:
            return f"{value/1e9:.2f}B"
        elif abs(value) >= 1e6:
            return f"{value/1e6:.2f}M"
        elif abs(value) >= 1e3:
            return f"{value/1e3:.2f}K"
        else:
            return f"{value:,.0f}"
    except (ValueError, TypeError):
        return "N/A"

def format_market_cap(market_cap: Union[float, int]) -> str:
    """
    Format market capitalization with appropriate suffix.
    
    Args:
        market_cap (float/int): Market capitalization value
        
    Returns:
        str: Formatted market cap string
    """
    if market_cap is None or market_cap == 0:
        return "N/A"
    
    return f"${format_large_number(market_cap)}"

def format_volume(volume: Union[float, int]) -> str:
    """
    Format trading volume with appropriate suffix.
    
    Args:
        volume (float/int): Trading volume
        
    Returns:
        str: Formatted volume string
    """
    if volume is None or volume == 0:
        return "0"
    
    return format_large_number(volume)

def format_pe_ratio(pe_ratio: Union[float, int]) -> str:
    """
    Format P/E ratio.
    
    Args:
        pe_ratio (float/int): P/E ratio value
        
    Returns:
        str: Formatted P/E ratio string
    """
    if pe_ratio is None or pe_ratio <= 0:
        return "N/A"
    
    try:
        return f"{pe_ratio:.2f}"
    except (ValueError, TypeError):
        return "N/A"

def get_change_color(change: float) -> str:
    """
    Get CSS class name for change color based on value.
    
    Args:
        change (float): Price change value
        
    Returns:
        str: CSS class name for color
    """
    if change > 0:
        return "positive-change"
    elif change < 0:
        return "negative-change"
    else:
        return "neutral-change"

def get_change_icon(change: float) -> str:
    """
    Get emoji icon for price change.
    
    Args:
        change (float): Price change value
        
    Returns:
        str: Emoji icon
    """
    if change > 0:
        return "📈"
    elif change < 0:
        return "📉"
    else:
        return "➡️"

def calculate_percentage_change(current: float, previous: float) -> float:
    """
    Calculate percentage change between two values.
    
    Args:
        current (float): Current value
        previous (float): Previous value
        
    Returns:
        float: Percentage change
    """
    if previous == 0:
        return 0.0
    
    try:
        return ((current - previous) / previous) * 100
    except (ValueError, TypeError, ZeroDivisionError):
        return 0.0

def is_market_open() -> bool:
    """
    Check if the stock market is currently open.
    Note: This is a simplified check based on US market hours.
    
    Returns:
        bool: True if market is open, False otherwise
    """
    now = datetime.now()
    
    # Check if it's a weekday (Monday = 0, Sunday = 6)
    if now.weekday() >= 5:  # Saturday or Sunday
        return False
    
    # US market hours: 9:30 AM - 4:00 PM EST (simplified)
    market_open = now.replace(hour=9, minute=30, second=0, microsecond=0)
    market_close = now.replace(hour=16, minute=0, second=0, microsecond=0)
    
    return market_open <= now <= market_close

def get_time_until_market_open() -> str:
    """
    Get time until market opens (if currently closed).
    
    Returns:
        str: Time until market opens
    """
    now = datetime.now()
    
    # Calculate next market open time
    if now.weekday() >= 5:  # Weekend
        days_until_monday = (7 - now.weekday()) % 7
        next_market_day = now + timedelta(days=days_until_monday)
        next_market_day = next_market_day.replace(hour=9, minute=30, second=0, microsecond=0)
    else:  # Weekday
        today_market_open = now.replace(hour=9, minute=30, second=0, microsecond=0)
        if now < today_market_open:
            next_market_day = today_market_open
        else:
            # Next business day
            next_market_day = now + timedelta(days=1)
            while next_market_day.weekday() >= 5:  # Skip weekends
                next_market_day += timedelta(days=1)
            next_market_day = next_market_day.replace(hour=9, minute=30, second=0, microsecond=0)
    
    time_diff = next_market_day - now
    days = time_diff.days
    hours = time_diff.seconds // 3600
    minutes = (time_diff.seconds % 3600) // 60
    
    if days > 0:
        return f"{days}d {hours}h {minutes}m"
    else:
        return f"{hours}h {minutes}m"

def clean_stock_data(data: Dict) -> Dict:
    """
    Clean and validate stock data from API.
    
    Args:
        data (Dict): Raw stock data from API
        
    Returns:
        Dict: Cleaned stock data
    """
    if not data:
        return {}
    
    cleaned_data = {}
    
    # Clean and format each field
    for key, value in data.items():
        if key == 'current_price' or key == 'previous_close':
            cleaned_data[key] = float(value) if value is not None else 0.0
        elif key == 'change' or key == 'change_percent':
            cleaned_data[key] = float(value) if value is not None else 0.0
        elif key == 'volume':
            cleaned_data[key] = int(value) if value is not None else 0
        elif key == 'market_cap':
            cleaned_data[key] = float(value) if value is not None else 0.0
        elif key == 'pe_ratio':
            cleaned_data[key] = float(value) if value is not None else None
        elif key == 'symbol' or key == 'company_name' or key == 'sector' or key == 'industry':
            cleaned_data[key] = str(value) if value is not None else 'N/A'
        else:
            cleaned_data[key] = value
    
    return cleaned_data

def create_summary_data(stock_data: Dict[str, Dict]) -> List[Dict]:
    """
    Create summary data for the market overview table.
    
    Args:
        stock_data (Dict): Dictionary of stock data
        
    Returns:
        List[Dict]: List of summary data for each stock
    """
    summary_data = []
    
    for symbol, data in stock_data.items():
        summary_data.append({
            'Symbol': symbol,
            'Price': format_currency(data.get('current_price', 0)),
            'Change': format_currency(data.get('change', 0)),
            'Change %': format_percentage(data.get('change_percent', 0)),
            'Volume': format_volume(data.get('volume', 0)),
            'Market Cap': format_market_cap(data.get('market_cap', 0))
        })
    
    return summary_data

def log_error(error: Exception, context: str = "") -> None:
    """
    Log an error with context.
    
    Args:
        error (Exception): The error to log
        context (str): Additional context about the error
    """
    error_msg = f"{context}: {str(error)}" if context else str(error)
    logger.error(error_msg)

def log_info(message: str) -> None:
    """
    Log an info message.
    
    Args:
        message (str): Message to log
    """
    logger.info(message) 