import json
import yfinance as yf
#@param user: String the users name (must have associated stock_data/ file)
#@param load_data: boolean whether to download data immediately
#post: returns a dictionary containing all of the users tickers, with dictionaries 
def get_user_ticker_data(user, load_data=False):
	print(user)
	filepath = "./stock_data/"+user+".txt"
	f = open(filepath)
	tickers = {}
	for line in f:
		tickers[line[:-1]] = yf.Ticker(line[:-1])#getting rid of newline character
	if load_data:
		for key in tickers:
			x = tickers[key].info
			tickers[key] = x
	return tickers
def get_relevant_info(user = 'sammy'):
	stocks = get_user_ticker_data(user)
	#print(stocks['TSLA'].info)
	output = ''
	for stock in stocks.values():
		try:
			output += 'Info For Company: '+str(stock.info['shortName']) + '\n'
			output += '\tRegular Market Price : ' +str(stock.info['regularMarketPrice']) + '\n'
			output += '\tYesterdays Close : '+str(stock.info['previousClose']) + '\n'
			output += '\tOpening Price : ' +str(stock.info['regularMarketOpen']) +'\n'
			output += '\tProfit Margins: '+ str(stock.info['profitMargins']) + '\n'
			output += '\n'
		except KeyError:
			break
	return output
def get_stock_by_ticker(ticker):
	stock = yf.Ticker(ticker)
	return stock.info