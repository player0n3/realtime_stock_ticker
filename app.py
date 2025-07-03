import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
from collections import deque

# Page configuration
st.set_page_config(
    page_title="Realtime Stock Ticker",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .stock-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    .positive-change {
        color: #00ff88;
        font-weight: bold;
    }
    .negative-change {
        color: #ff4444;
        font-weight: bold;
    }
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'stock_ticker' not in st.session_state:
    st.session_state.stock_ticker = None

class StockTicker:
    def __init__(self):
        self.symbols = []
        self.price_history = {}
        
    def add_symbol(self, symbol):
        """Add a stock symbol to track"""
        if symbol.upper() not in [s.upper() for s in self.symbols]:
            self.symbols.append(symbol.upper())
            self.price_history[symbol.upper()] = deque(maxlen=100)
            return True
        return False
    
    def remove_symbol(self, symbol):
        """Remove a stock symbol from tracking"""
        if symbol.upper() in [s.upper() for s in self.symbols]:
            self.symbols.remove(symbol.upper())
            if symbol.upper() in self.price_history:
                del self.price_history[symbol.upper()]
            return True
        return False
    
    def get_stock_data(self, symbol):
        """Get real-time stock data for a symbol"""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            
            # Get current price
            hist = ticker.history(period="1d", interval="1m")
            if not hist.empty:
                current_price = hist['Close'].iloc[-1]
                previous_close = info.get('previousClose', current_price)
                change = current_price - previous_close
                change_percent = (change / previous_close) * 100 if previous_close else 0
                
                # Store price history
                self.price_history[symbol].append({
                    'timestamp': datetime.now(),
                    'price': current_price
                })
                
                return {
                    'symbol': symbol,
                    'current_price': current_price,
                    'previous_close': previous_close,
                    'change': change,
                    'change_percent': change_percent,
                    'volume': info.get('volume', 0),
                    'market_cap': info.get('marketCap', 0),
                    'pe_ratio': info.get('trailingPE', 0),
                    'company_name': info.get('longName', symbol),
                    'sector': info.get('sector', 'N/A'),
                    'industry': info.get('industry', 'N/A'),
                    'timestamp': datetime.now()
                }
        except Exception as e:
            error_msg = str(e)
            if '429' in error_msg or 'Too Many Requests' in error_msg:
                st.warning(f"Rate limit reached for {symbol}. Skipping this symbol temporarily.")
            elif '404' in error_msg or 'Not Found' in error_msg or 'No data found' in error_msg:
                st.warning(f"Symbol {symbol} not found or is invalid. Please remove it from tracking.")
            else:
                st.warning(f"Error fetching data for {symbol}: {error_msg}")
            return None
    
    def get_all_data(self):
        """Get data for all tracked symbols"""
        data = {}
        for symbol in self.symbols:
            stock_data = self.get_stock_data(symbol)
            if stock_data:
                data[symbol] = stock_data
        return data

# Initialize stock ticker
if st.session_state.stock_ticker is None:
    st.session_state.stock_ticker = StockTicker()

ticker = st.session_state.stock_ticker

# Main header
st.markdown('<h1 class="main-header">📈 Realtime Stock Ticker</h1>', unsafe_allow_html=True)

# Sidebar for symbol management
with st.sidebar:
    st.header("🔧 Stock Management")
    
    # Add new symbol
    new_symbol = st.text_input("Add Stock Symbol", placeholder="e.g., AAPL, GOOGL, MSFT")
    if st.button("Add Stock"):
        if new_symbol:
            if ticker.add_symbol(new_symbol):
                st.success(f"Added {new_symbol.upper()} to tracking")
                st.rerun()
            else:
                st.error("Symbol already exists or failed to add")
    
    # Remove symbol
    if ticker.symbols:
        st.subheader("Tracked Stocks")
        for symbol in ticker.symbols:
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(symbol)
            with col2:
                if st.button("Remove", key=f"remove_{symbol}"):
                    ticker.remove_symbol(symbol)
                    st.rerun()
    
    # Auto-refresh settings
    st.subheader("⚙️ Settings")
    auto_refresh = st.checkbox("Auto-refresh (every 30 seconds)", value=False)
    refresh_interval = st.slider("Refresh interval (seconds)", 10, 60, 30)

# Main content area
if not ticker.symbols:
    st.info("👆 Add some stock symbols in the sidebar to get started!")
    st.markdown("""
    ### Popular Stock Symbols to Try:
    - **AAPL** - Apple Inc.
    - **GOOGL** - Alphabet Inc. (Google)
    - **MSFT** - Microsoft Corporation
    - **TSLA** - Tesla, Inc.
    - **AMZN** - Amazon.com, Inc.
    - **META** - Meta Platforms, Inc.
    - **NVDA** - NVIDIA Corporation
    - **NFLX** - Netflix, Inc.
    """)
else:
    # Get current data
    current_data = ticker.get_all_data()
    
    if len(current_data) == 0:
        st.warning("No valid stock data available. Please check your tracked symbols or try again later.")
    else:
        # Display stock cards
        cols = st.columns(min(3, len(current_data)))
        
        for i, (symbol, data) in enumerate(current_data.items()):
            col_idx = i % len(cols)
            
            with cols[col_idx]:
                change_color = "positive-change" if data['change'] >= 0 else "negative-change"
                change_icon = "📈" if data['change'] >= 0 else "📉"
                
                st.markdown(f"""
                <div class="stock-card">
                    <h3>{change_icon} {data['symbol']}</h3>
                    <h2>${data['current_price']:.2f}</h2>
                    <p class="{change_color}">
                        {data['change']:+.2f} ({data['change_percent']:+.2f}%)
                    </p>
                    <small>{data['company_name']}</small>
                </div>
                """, unsafe_allow_html=True)
        
        # Detailed metrics
        st.subheader("📊 Detailed Metrics")
        
        for symbol, data in current_data.items():
            with st.expander(f"{symbol} - {data['company_name']}"):
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Current Price", f"${data['current_price']:.2f}")
                    st.metric("Previous Close", f"${data['previous_close']:.2f}")
                
                with col2:
                    st.metric("Change", f"{data['change']:+.2f}")
                    st.metric("Change %", f"{data['change_percent']:+.2f}%")
                
                with col3:
                    st.metric("Volume", f"{data['volume']:,}")
                    st.metric("Market Cap", f"${data['market_cap']/1e9:.2f}B" if data['market_cap'] else "N/A")
                
                with col4:
                    st.metric("P/E Ratio", f"{data['pe_ratio']:.2f}" if data['pe_ratio'] else "N/A")
                    st.metric("Sector", data['sector'])
        
        # Price charts
        st.subheader("📈 Price Charts")
        
        for symbol, data in current_data.items():
            if symbol in ticker.price_history and len(ticker.price_history[symbol]) > 1:
                # Create price history chart
                history_df = pd.DataFrame(list(ticker.price_history[symbol]))
                
                fig = go.Figure()
                fig.add_trace(go.Scatter(
                    x=history_df['timestamp'],
                    y=history_df['price'],
                    mode='lines+markers',
                    name=symbol,
                    line=dict(color='#1f77b4', width=2),
                    marker=dict(size=6)
                ))
                
                fig.update_layout(
                    title=f"{symbol} Price Movement",
                    xaxis_title="Time",
                    yaxis_title="Price ($)",
                    height=400,
                    showlegend=False,
                    template="plotly_white"
                )
                
                st.plotly_chart(fig, use_container_width=True)
        
        # Market overview
        st.subheader("🌍 Market Overview")
        
        # Create a summary table
        summary_data = []
        for symbol, data in current_data.items():
            summary_data.append({
                'Symbol': symbol,
                'Price': f"${data['current_price']:.2f}",
                'Change': f"{data['change']:+.2f}",
                'Change %': f"{data['change_percent']:+.2f}%",
                'Volume': f"{data['volume']:,}",
                'Market Cap': f"${data['market_cap']/1e9:.2f}B" if data['market_cap'] else "N/A"
            })
        
        summary_df = pd.DataFrame(summary_data)
        st.dataframe(summary_df, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>📈 Realtime Stock Ticker | Powered by Yahoo Finance API</p>
    <p>Last updated: {}</p>
</div>
""".format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), unsafe_allow_html=True)
