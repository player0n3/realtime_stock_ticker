"""
Configuration file for the Realtime Stock Ticker application.
Contains default settings, constants, and configuration options.
"""

# Application Settings
APP_NAME = "Realtime Stock Ticker"
APP_VERSION = "1.0.0"
APP_DESCRIPTION = "A modern real-time stock ticker application"

# Default Stock Symbols (popular stocks to start with)
DEFAULT_STOCKS = [
    "AAPL",  # Apple Inc.
    "GOOGL", # Alphabet Inc. (Google)
    "MSFT",  # Microsoft Corporation
    "TSLA",  # Tesla, Inc.
    "AMZN",  # Amazon.com, Inc.
    "META",  # Meta Platforms, Inc.
    "NVDA",  # NVIDIA Corporation
    "NFLX",  # Netflix, Inc.
    "JPM",   # JPMorgan Chase & Co.
    "V"      # Visa Inc.
]

# Refresh Settings
DEFAULT_REFRESH_INTERVAL = 30  # seconds
MIN_REFRESH_INTERVAL = 10      # seconds
MAX_REFRESH_INTERVAL = 60      # seconds

# Data Settings
MAX_PRICE_HISTORY = 100        # Maximum number of price points to store
MAX_STOCKS_TO_TRACK = 20       # Maximum number of stocks to track simultaneously

# API Settings
YAHOO_FINANCE_TIMEOUT = 10     # seconds
MAX_RETRIES = 3                # Maximum number of API retry attempts

# UI Settings
CARDS_PER_ROW = 3              # Number of stock cards per row
CHART_HEIGHT = 400             # Height of price charts in pixels
SIDEBAR_WIDTH = 300            # Width of sidebar in pixels

# Color Schemes
COLORS = {
    'primary': '#1f77b4',
    'secondary': '#667eea',
    'accent': '#764ba2',
    'positive': '#00ff88',
    'negative': '#ff4444',
    'neutral': '#666666',
    'background': '#ffffff',
    'card_background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'
}

# Error Messages
ERROR_MESSAGES = {
    'invalid_symbol': 'Invalid stock symbol. Please check the symbol and try again.',
    'api_error': 'Error fetching data from Yahoo Finance API.',
    'network_error': 'Network connection error. Please check your internet connection.',
    'rate_limit': 'API rate limit exceeded. Please wait before making more requests.',
    'symbol_not_found': 'Stock symbol not found. Please verify the symbol is correct.',
    'max_stocks': f'Maximum number of stocks ({MAX_STOCKS_TO_TRACK}) reached. Please remove some stocks first.'
}

# Success Messages
SUCCESS_MESSAGES = {
    'stock_added': 'Stock added successfully to tracking list.',
    'stock_removed': 'Stock removed from tracking list.',
    'data_updated': 'Stock data updated successfully.',
    'settings_saved': 'Settings saved successfully.'
}

# Chart Configuration
CHART_CONFIG = {
    'template': 'plotly_white',
    'line_color': '#1f77b4',
    'line_width': 2,
    'marker_size': 6,
    'show_legend': False,
    'responsive': True
}

# Data Validation
VALID_SYMBOL_PATTERN = r'^[A-Z]{1,5}$'  # Basic pattern for stock symbols

# Performance Settings
ENABLE_CACHING = True
CACHE_TTL = 300  # seconds (5 minutes)
MAX_CONCURRENT_REQUESTS = 5

# Logging Configuration
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FILE = 'stock_ticker.log'

# Feature Flags
FEATURES = {
    'auto_refresh': True,
    'price_alerts': False,  # Future feature
    'technical_indicators': False,  # Future feature
    'portfolio_tracking': False,  # Future feature
    'export_data': False,  # Future feature
} 