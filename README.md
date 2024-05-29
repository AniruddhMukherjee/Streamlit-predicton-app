# Stock Dashboard and Predicition using Streamlit

### *Overview*
This project provides a comprehensive dashboard for analyzing and visualizing stock market data. It leverages the Yahoo Finance API to fetch real-time stock prices, historical data, and the latest news related to a specified stock. The dashboard displays the current stock price, a line chart of historical performance, and the latest news articles. Additionally, the project implements a machine learning model to predict future stock prices based on historical data, presenting the forecasts alongside the actual prices. The user-friendly interface allows investors and traders to easily navigate and interact with the dashboard, making it a valuable tool for informed decision-making in the stock market.

## *Technologies Used :*

### *Streamlit*
Streamlit simplifies the development of interactive web applications for data science and machine learning projects. With its intuitive interface and easy-to-use functionalities, Streamlit enables developers to build powerful web apps with minimal effort.

### *yfinance*
Plotly Express is a high-level data visualization library for Python that provides a simple and intuitive interface for creating a variety of interactive and customizable plots, including scatter plots, line charts, bar charts, histograms, and more. It is built on top of the Plotly.js library and offers a wide range of features for data exploration and presentation.

### *PLotly.express*
The alpha_vantage Python library is a comprehensive API for retrieving real-time and historical financial data from the Alpha Vantage platform. It supports a wide range of financial instruments, including stocks, currencies, cryptocurrencies, and more, and provides a user-friendly interface for accessing and analyzing this data.

### *alpha_vantage*
PyPDF is a Python library designed for processing PDF files. It offers functionalities for extracting text, images, and metadata from PDF documents, making it a valuable tool for tasks such as text extraction, content analysis, and document processing.

### *stocknews*
The stocknews Python library is a tool for retrieving and analyzing news articles related to specific stocks or companies. It allows users to search for news articles, filter them by date or relevance, and extract key information such as sentiment, topics, and entities mentioned in the articles. This can be useful for investors and analysts looking to stay informed about the latest developments in the stock market.

## *Highlights of the Project :*
### *Stock Price Display*
Fetch and display the current stock price, including the opening, closing, high, and low prices.
Provide historical stock price data and display it in a line chart, allowing users to analyze the stock's performance over time.

### *Stock News*
Retrieve the latest news articles related to the specified stock from various sources.
Display the news articles with their titles, summaries, and links to the original sources.
Allow users to filter and sort the news based on relevance, date, or other criteria.

### *Stock Prediction*
Implement a machine learning model to predict future stock prices based on historical data.
Train the model using techniques like linear regression, time series analysis, or neural networks.
Display the predicted stock prices in the dashboard, along with visualizations to help users understand the forecasts.

### *Usage:*
Install dependencies: pip install -r requirements.txt
Run the Streamlit app: streamlit run app.py
