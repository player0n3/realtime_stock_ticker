#!/usr/bin/env python3
"""
Launcher script for the Realtime Stock Ticker application.
Handles setup, dependency checking, and application startup.
"""

import sys
import subprocess
import importlib.util
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible."""
    if sys.version_info < (3, 8):
        print("❌ Error: Python 3.8 or higher is required.")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✅ Python version: {sys.version.split()[0]}")

def check_dependencies():
    """Check if required dependencies are installed."""
    required_packages = [
        'streamlit',
        'yfinance',
        'pandas',
        'plotly',
        'websocket-client',
        'requests'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        if importlib.util.find_spec(package) is None:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"❌ Missing dependencies: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'
            ])
            print("✅ Dependencies installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install dependencies.")
            print("Please run: pip install -r requirements.txt")
            sys.exit(1)
    else:
        print("✅ All dependencies are installed.")

def check_files():
    """Check if required files exist."""
    required_files = ['app.py', 'requirements.txt', 'config.py', 'utils.py']
    missing_files = []
    
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        sys.exit(1)
    
    print("✅ All required files found.")

def main():
    """Main launcher function."""
    print("🚀 Starting Realtime Stock Ticker...")
    print("=" * 50)
    
    # Check Python version
    check_python_version()
    
    # Check dependencies
    check_dependencies()
    
    # Check files
    check_files()
    
    print("=" * 50)
    print("🎯 Launching application...")
    print("📱 The app will open in your default browser.")
    print("🔗 URL: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the application.")
    print("=" * 50)
    
    try:
        # Launch Streamlit app
        subprocess.run([
            sys.executable, '-m', 'streamlit', 'run', 'app.py',
            '--server.port', '8501',
            '--server.address', 'localhost',
            '--browser.gatherUsageStats', 'false'
        ])
    except KeyboardInterrupt:
        print("\n👋 Application stopped by user.")
    except Exception as e:
        print(f"❌ Error launching application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 