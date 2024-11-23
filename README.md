# Stock Price Comparison

**Stock Price Comparison** is a Streamlit application that allows users to compare stock prices of multiple companies over a specified time period. The app utilizes the **yfinance** library to dynamically fetch stock data and provides insightful visualizations and analysis based on user inputs.

## Features

- **Multiple Stock Tickers**: Enter multiple stock tickers to compare their performance.
- **Date Range Selection**: Choose a start and end date to filter the stock data.
- **Stock Comparison**: View detailed comparisons of stock prices, including significant price changes.
- **Threshold Customization**: Set a threshold for significant changes to filter the most relevant data.
- **Insights Section**: Add, save, and view insights based on the stock graphs for further analysis.
- **Stock Data View**: View raw stock data in a user-friendly format.

## How It Works

1. **Input Stock Tickers**: Enter the stock symbols (e.g., `AAPL`, `GOOGL`, `AMZN`) that you wish to compare.
2. **Select Date Range**: Choose the start and end dates for the comparison.
3. **Submit**: After clicking the submit button, the application fetches the stock data and displays:
   - **Price Comparison**: A comparison graph showing the performance of each stock.
   - **Significant Price Changes**: A table highlighting significant changes in stock prices, with customizable thresholds.
4. **Add Insights**: You can add your insights based on the graphs and save them for later reference.
5. **View Stock Data**: The app also allows you to view detailed stock data in a tabular format.

## Installation

To run the **Stock Price Comparison** app locally, follow these steps:

### 1. Clone the repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Install Dependencies
Ensure that Python 3.10.8 is installed. Then, install the necessary libraries by running:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App
```bash
streamlit run app.py
```
This will launch the app locally at http://localhost:8501.