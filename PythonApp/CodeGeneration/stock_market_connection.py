import yfinance as yf

def get_stock_data(ticker, start_date, end_date):
    """
    Fetches historical stock data for the given ticker symbol between the start and end dates.
    
    Args:
    ticker (str): The ticker symbol of the stock.
    start_date (str): The start date in the format 'YYYY-MM-DD'.
    end_date (str): The end date in the format 'YYYY-MM-DD'.
    
    Returns:
    DataFrame: A DataFrame containing the historical stock data.
    """
    stock = yf.Ticker(ticker)
    hist = stock.history(start=start_date, end=end_date)
    return hist

if __name__ == "__main__":
    # Example usage
    ticker_symbol = 'AAPL'  # Apple Inc.
    start_date = '2022-01-01'
    end_date = '2022-12-31'
    
    stock_data = get_stock_data(ticker_symbol, start_date, end_date)
    print(f"Historical stock data for {ticker_symbol} from {start_date} to {end_date}:")
    print(stock_data)