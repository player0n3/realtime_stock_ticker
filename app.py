import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Stock Ticker", page_icon="📈", layout="wide")

st.title("🚀 Railway Test App")
st.write("If you can see this, Railway deployment is working!")
st.write(f"App loaded at: {datetime.now()}")
