import streamlit as st
st.set_page_config(
    page_title="Stock Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)
import pandas as pd
import yfinance as yf
from datetime import date, datetime
import time 
import os
from src import save_text_to_file, plot_stock_price_comparison

st.logo(image="assets/Full_Logo.png", size='large', icon_image="assets/Small_Logo.png")
st.markdown(
    """
    <style>
    img[data-testid="stLogo"]{
    height:50px;
    width:800;
    }   
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>Stock Price Comparison</h1>", unsafe_allow_html=True)
stock_ticker_file = 'Tickers/Stock_Tickers'
stock_list = pd.read_csv(stock_ticker_file).squeeze().tolist()

if 'submitted' not in st.session_state:
    st.session_state.submitted = False

with st.form(key='stock_form'):
    stock_tickers = st.multiselect('Select stocks to analyze', stock_list,  default=['GOOGL', 'AMZN'])
    today = date.today()
    col1,col2 = st.columns(2)
    with col1:
        start = st.date_input("Start date", date(2021, 1, 1), max_value=today)
    with col2:
        end = st.date_input("End date", date(2022, 12, 31), max_value=today)
    submit_button = st.form_submit_button(label="Submit", icon=":material/stacked_bar_chart:")

if submit_button and not st.session_state.submitted:
    st.session_state.submitted = True 

if st.session_state.submitted:
    st.markdown(f"#### Stock Comparision for ({', '.join(stock_tickers)})")
    stock_data = yf.download(stock_tickers, start=start, end=end, group_by='ticker')

    @st.dialog(f"Stock Data for ({', '.join(stock_tickers)})", width="large")
    def show_data():
        st.dataframe(stock_data)
    view_data = st.button("Show Data", icon=":material/table:")
    if view_data:
        show_data()

    st.write("**Stock Price Comparison with Significant Changes**")
    with st.container(border=True):
        with st.container(border=True):
            threshold = st.slider('Select threshold for significant price change', min_value=0.01, max_value=0.2, value=0.07, step=0.01)
        if stock_tickers: 
            plot_stock_price_comparison(stock_data=stock_data, stock_tickers=stock_tickers, threshold=threshold)
        else:
            st.error("Please select at least one stock to analyze.")

with st.sidebar:
    st.subheader("Add Insights")
    insights_text = st.text_area("Type your insights here", height=200)
    current_time = datetime.now().strftime("%H:%M - %d/%m/%Y")
    insights_text_with_datetime = f"{current_time}\n{insights_text}\n\n"

    if st.button("Save Insights", icon=":material/save:", use_container_width=True):
        save_text_to_file(insights_text_with_datetime)
        st.markdown('<style>div[data-baseweb="toast"] div {color: green;}</style>', unsafe_allow_html=True)
        st.toast('Insights saved successfully!')
        time.sleep(.5)

    if not os.path.exists("Insights.txt"):
        with open("Insights.txt", "w") as file:
            file.write("Stock Comparison(Insights): \n\n")

    insights = st.button("Show Insights", icon=":material/description:", use_container_width= True)
    
if insights:
    @st.dialog("Insights", width="large")
    def insights():
        if os.path.exists("Insights.txt"):
            with open("Insights.txt", "r") as file:
                insights = file.read()
            st.text_area("Saved Insights", insights, height=300)
        else:
            st.warning("No insights saved yet.")
    insights()
                