import yfinance as yf

# Get the list of tickers from user input
tickers = input("Enter the tickers separated by a space: ").split()

# Get the live stock data for each ticker
live_data = yf.download(tickers, period="1d")  # By default, group_by='column'

# Display the live stock data including volume, percent change, opening price, high, and low
for ticker in tickers:
    print(f"Ticker: {ticker}")
    print("Volume:")
    print(live_data['Volume'][ticker].to_string(index=False, header=False))  # Display volume
    print("Percent Change:")
    print(live_data['Close'][ticker].pct_change().to_string(index=False, header=False))  # Display percent change
    print("Opening Price:")
    print(live_data['Open'][ticker].to_string(index=False, header=False))  # Display opening price
    print("High:")
    print(live_data['High'][ticker].to_string(index=False, header=False))  # Display high
    print("Low:")
    print(live_data['Low'][ticker].to_string(index=False, header=False))  # Display low

# Save the live stock data to a new CSV file
live_data.to_csv('live_stock_quotes.csv')
