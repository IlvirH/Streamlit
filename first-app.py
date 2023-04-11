import streamlit as st
import yfinance as yf
import pandas as pd

st.title("""
Котировки стоимости акций компании 'APPLE' за период с 11.02.2006 по 22.09.2022

""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2006-2-11', end='2022-9-22')

st.write("""
### Стоимость при закрытии торгов
""")

st.line_chart(tickerDf['Close'])

st.write("""
### Объемы торгов
""")
st.line_chart(tickerDf['Volume'])