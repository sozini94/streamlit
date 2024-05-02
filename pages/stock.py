from pykrx import stock
from pykrx import bond
from datetime import datetime
import streamlit as st
import time


today = datetime.today()  
today = today.strftime("%Y%m%d")
tickers = stock.get_market_ticker_list(today)
stocks = []

for ticker in stock.get_market_ticker_list():
    stocks.append(ticker+f"/"+stock.get_market_ticker_name(ticker))

def get_stock_info(stock_code, start_date, end_date):
    df = stock.get_market_ohlcv(start_date, end_date, stock_code)
    time.sleep(1)
    return df

st.title("주식 정보 조회 앱")

stock_select = st.selectbox('주식을 선택해주세요.', stocks)
stock_code = stock_select.split("/")

# stock_code = st.text_input("주식 코드를 입력하세요. (예)005930 삼성전자","005930")
start_date = st.date_input("조회 시작 날짜를 입력하세요.", value=None)
end_date = st.date_input("조회 종료 날짜를 입력하세요.", value=None)


if st.button("주식 정보 조회"):
    start_date_str = start_date.strftime("%Y%m%d")
    end_date_str = end_date.strftime("%Y%m%d")
    stock_data = get_stock_info(stock_code[0], start_date_str, end_date_str)

    st.write(stock_data)
    
    stock_data2 = stock.get_stock_major_changes(stock_code[0])
    st.write(stock_data2)
    print(stock_data2)