import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

st.title("Stock Dashboard")
ticker = st.sidebar.text_input("Ticker")
start_date = st.sidebar.date_input("Start Date")
end_date = st.sidebar.date_input("End Date")

if ticker == "":
    st.subheader("Please select a stock and name it properly as per the NYSE")
data = yf.download(ticker, start=start_date, end=end_date)
fig = px.line(data, x = data.index, y=data['Adj Close'], title=ticker)
st.plotly_chart(fig)

pricing_data, Prediction, fundamental_data, news= st.tabs(["Pricing Data", "Prediction", "Fundamental Data", "Top 10 news"])


###############################################################
# THE PRICING DATA CODE
###############################################################
with pricing_data:
    st.header("Pricing Movements")
    data2 = data
    data2['% Change'] = data['Adj Close'] / data['Adj Close'].shift(1) - 1
    data2.dropna(inplace = True)
    ##################################### MULTIPLE BUTTON PRESS
    show_content = st.session_state.get('show_content', False)
    if st.button('Data table'):
      show_content = not show_content
      st.session_state['show_content'] = show_content

    if show_content:
      st.table(data2)
    #############################################################
    annual_return = data2['% Change'].mean()*252*100
    st.write('Annual Return is', annual_return, '%')
    stdev = np.std(data2['% Change'])*np.sqrt(252)
    st.write('Standard Deviation is ', stdev*100, "%")
    st.write("Risk Adj. Return is ", annual_return/(stdev*100))

###############################################################
# FUNDAMENATAL DATA CODE
###############################################################
from alpha_vantage.fundamentaldata import FundamentalData 
with fundamental_data:
    st.subheader("Select any one of these")
    bsn, is1n, cfn = st.columns(3)
    key = 'ADXU8JR8RRDFXMMR'
    fd = FundamentalData(key, output_format = 'pandas')
    if bsn.button("Balance Sheet"):
      st.subheader('Balance Sheet')
      balance_sheet = fd.get_balance_sheet_annual(ticker)[0]
      bs = balance_sheet.T[2:]#
      bs.columns = list(balance_sheet.T.iloc[0])
      st.write(bs)
    if is1n.button("Income Statement"):
      st.subheader('Income Statement')
      income_statement = fd.get_income_statement_annual(ticker)[0]
      is1 = income_statement.T[2:]
      is1.columns = list(income_statement.T.iloc[0])
      st.write(is1)
    if cfn.button("Cash Flow"):
      st.subheader("Cash Flow Statement")
      cash_flow = fd.get_cash_flow_annual(ticker)[0]
      cf = cash_flow.T[2:]
      cf.columns = list(cash_flow.T.iloc[0])
      st.write(cf)
      

###############################################################
# THE LATEST NEWS CODE
###############################################################
from stocknews import StockNews
with news:
   st.header(f'News of {ticker}')
   sn = StockNews(ticker, save_news=False)
   df_news = sn.read_rss()
   for i in range(10):
      st.subheader(f'News {i+1}')
      st.write(df_news['published'][i])
      st.write(df_news['title'][i])
      st.write(df_news['summary'][i])
      title_sentiment = df_news['sentiment_title'][i]
      st.write(f'Title Sentiment {title_sentiment}')
      news_sentiment =df_news['sentiment_summary'][i]
      st.write(f'News Sentiment {news_sentiment}')

###############################################################
# THE PREDICTION OF STOCK PRICE (TESTING PHASE....)
###############################################################
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# Taking the input from user
stock = yf.Ticker(ticker)
user_data = stock.history(start=start_date, end=end_date)
# Prepare the dataset
X = user_data[['Open', 'High', 'Low', 'Volume']]  # Feature columns
y = user_data['Close']  # Target column

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

train_score = model.score(X_train, y_train)
test_score = model.score(X_test, y_test)

with Prediction:
   new_data = X_test.iloc[:1]  # Use the first row of the test set as new data
   predictions = model.predict(new_data)
   st.write(f"Predictions : {predictions}")
   #st.write(f"Training score: {train_score:.2f}")
   #st.write(f"Testing score: {test_score:.2f}")

   st.subheader("Enter custom data for prediction:")
   op, cl = st.columns(2)
   lv, vv = st.columns(2)
   open_value = op.number_input("Open:", min_value=0.0, step=0.01)
   high_value = cl.number_input("High:", min_value=0.0, step=0.01)
   low_value = lv.number_input("Low:", min_value=0.0, step=0.01)
   volume_value = vv.number_input("Volume:", min_value=0, step=1)

   custom_data = [open_value, high_value, low_value, volume_value]
   prediction = model.predict([custom_data])
   st.write(f"Prediction : {prediction[0]:.2f}")
