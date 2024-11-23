import plotly.graph_objs as go
import yfinance as yf
import pandas as pd
import streamlit as st

def plot_stock_price_comparison(stock_data, stock_tickers, threshold=0.07):
    fig_line = go.Figure()
    for ticker in stock_tickers:
        ticker_data = stock_data[ticker].reset_index()
        ticker_data['Price_Change'] = ticker_data['Close'].pct_change()
        fig_line.add_trace(go.Scatter(
            x=ticker_data['Date'],
            y=ticker_data['Close'],
            mode='lines',
            name=ticker,
            line=dict(width=2)
        ))
        major_up = ticker_data[ticker_data['Price_Change'] > threshold]
        major_down = ticker_data[ticker_data['Price_Change'] < -threshold]
        for _, row in major_up.iterrows():
            fig_line.add_annotation(
                x=row['Date'], y=row['Close'],
                text=f'Significant Rise<br>+{row["Price_Change"]:.1%}',
                showarrow=True, arrowhead=3, ax=0, ay=-40,
                font=dict(color='green', size=12),
                bgcolor='white', bordercolor='green', borderwidth=1
            )
        for _, row in major_down.iterrows():
            fig_line.add_annotation(
                x=row['Date'], y=row['Close'],
                text=f'Significant Drop<br>{row["Price_Change"]:.1%}',
                showarrow=True, arrowhead=3, ax=0, ay=40,
                font=dict(color='red', size=12),
                bgcolor='white', bordercolor='red', borderwidth=1
            )
    fig_line.update_layout(
        title='Line Chart of Stock Prices Comparison with Significant Changes',
        xaxis_title='Date',
        yaxis_title='Price',
        margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig_line)