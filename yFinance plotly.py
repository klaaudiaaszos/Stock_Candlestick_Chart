import yfinance as yf
import plotly.graph_objects as go

ticker = "TSLA"
userTicker = input ("Write ticker name: ").strip().upper()
if userTicker:
    ticker = userTicker

data = yf.download (tickers = ticker, period = "6mo", interval = "1d", rounding = True)

if data.empty:
    print("No data found for ticker:", ticker)
    exit()

print ("Data from server for ticker: ", ticker)
data.columns = data.columns.droplevel(1)
print (data)


chart = go.Figure ()
chart.add_trace ( go.Candlestick (x = data.index, open = data ["Open"], high = data ["High"], low = data ["Low"], close = data ["Close"], name = "Price Chart" ))
chart.update_layout (title = "Ticker" + " share price", yaxis_title = "Stock price (USD)")

chart.show (renderer= "browser") # sposób renderowania - browser
