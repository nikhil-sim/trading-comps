"""
Integration tests for util.py
"""
import sys
sys.path.append('..')
import util

#Test 1: Call fetch_webpage w/ 200 response (using own endpoint).
try: 
  url = 'https://pgc34s2jd1.execute-api.us-west-1.amazonaws.com/default/'\
  'testing?404=False'
  fetched_html = util.fetch_webpage(url)
  correct_html = '<html><head><title>Hello, World!</title></head><body>'\
    '<h1>Hello, World!</h1></body></html>'
  if fetched_html != correct_html:
    print('Test 1 failed.')
  else:
    print('Test 1 passed.')
except Exception as e:
  print('Test 1: There was an error fetching the webpage.')
  print(e)

print()
#Test 2: Call fetch_webpage w/ 404 response (using own endpoint).
try: 
  url = 'https://pgc34s2jd1.execute-api.us-west-1.amazonaws.com/default/'\
  'testing?404=True'
  fetched_html = util.fetch_webpage(url)
  if fetched_html != None:
    print('Test 2 failed.')
  else:
    print('Test 2 passed.')
except Exception as e:
  print('Test 2: There was an error fetching the webpage.')
  print(e)

print()
#Test 3: Call fetch_api w/ with VNO (test valid until 2022-12-31)
try:
  ticker = 'VNO'
  wrong = False

  latest_earnings = util.fetch_api_data(ticker, 'latestEarnings')
  lates_earnings_actual = '2021-12-31'
  if latest_earnings != lates_earnings_actual:
    print('Test 3 failed. Incorrect latest earnings.')
    wrong = True

  shares_outstanding = util.fetch_api_data(ticker, 'sharesOutstanding')
  shares_outstanding_actual = '191723608'
  if shares_outstanding != shares_outstanding_actual:
    print('Test 3 failed. Incorrect shares outstanding.')
    wrong = True

  net_debt = util.fetch_api_data(ticker, 'netDebt')
  net_debt_actual = '1377379000'
  if net_debt != net_debt_actual:
    print('Test 3 failed. Incorrect net debt.')
    wrong = True

  revenue = util.fetch_api_data(ticker, 'totalRevenue')
  revenue_actual = '1589210000'
  if revenue != revenue_actual:
    print('Test 3 failed. Incorrect total revenue.')
    wrong = True

  ebitda = util.fetch_api_data(ticker, 'ebitda')
  ebitda_actual = '827019000'
  if ebitda != ebitda_actual:
    print('Test 3 failed. Incorrect ebitda.')
    wrong = True  

  net_income = util.fetch_api_data(ticker, 'netIncome')
  net_income_actual = '175999000'
  if net_income != net_income_actual:
    print('Test 3 failed. Incorrect net income.')
    wrong = True  

  if not wrong:
    print("Test 3 passed.")
except Exception as e:
  print('Test 3: There was an error fetching data from AlphVantage APIs.')
  print(e)
  
print()
#Test 4: Call fetch_api w/ bad parameters (should gracefully handle errors).
#Note that AlphaVantage will return an empty dictionary w/ no data.
try:
  ticker = 'ABCDEFG' #bad ticker
  latest_earnings = util.fetch_api_data(ticker, 'latestEarnings')
  if latest_earnings != None:
    print('Test 4 failed.')
  else:
    print('Test 4 passed.')
except Exception as e:
  print('Test 4: There was an error fetching data from AlphVantage APIs.')
  print(e)
 
print()     
#Test 5: db_write/db_read by writing to and deleting from the (test) database.
try:
  insert_data = [
    ('2021-01-01', 'LUV', 'Airlines', 123, 123, 123, 123, 123),
    ('2021-01-01', 'UAL', 'Airlines', 456, 456, 456, 456, 456)
  ]
  insert_query = """
  INSERT INTO 
  trading_comps.test (latest_earnings, ticker, gics_sub_industry, 
    shares_outstanding, net_debt, revenue, ebitda, net_income)
  VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
  """
  util.db_write(insert_query, insert_data)

  read_query = """
  SELECT ticker FROM trading_comps.test WHERE gics_sub_industry = %s;
  """
  read_param = ['Airlines']
  airline_ticker_data = util.db_read(read_query, read_param)
  airlines_tickers = {row[0] for row in airline_ticker_data}
  correct_airline_tickers = {'ALK', 'AAL', 'DAL', 'LUV', 'UAL'}

  wrong = False
  if airlines_tickers != correct_airline_tickers:
    print('Test 5 failed. Incorrect airline tickers.')
    wrong = True
        
  #cleanup
  delete_query = """
  DELETE FROM trading_comps.test WHERE ticker IN %s;
  """
  delete_tickers = ['LUV', 'UAL']
  util.db_write(delete_query, delete_tickers)

  check_cleanup_query = """
  SELECT ticker FROM trading_comps.test WHERE gics_sub_industry = 'Airlines';
  """
  cleaned_up_data = util.db_read(read_query, read_param)
  cleaned_up_tickers = {row[0] for row in cleaned_up_data}
  correct_cleaned_up_tickers = {'ALK', 'AAL', 'DAL'}
  if cleaned_up_tickers != correct_cleaned_up_tickers:
    print('Test 5 failed. Incorrect cleanup.')
    wrong = True
  
  if not wrong:
    print('Test 5 passed.')
except Exception as e:
  print('Test 5: There were issues working with the database.')