"""
Tests to make sure that the webpage being scraped and the APIs being 
used to fetch data maintain the structure that is expected. A successful test
involves printing the following: 'Webpage verification successful.' and 
'API verifcation successful.', each on their own line.  
"""
import requests
import sys
import json
from bs4 import BeautifulSoup

"""
Tests that https://en.wikipedia.org/wiki/List_of_S%26P_500_companies has the 
structure needed for the program. This includes making sure that there is 
a constituents table with the required rows. 
"""
try:
  url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
  r = requests.get(url)
  html = r.text
  soup = BeautifulSoup(html, 'lxml')
  company_table = soup.find_all(id='constituents')[0]
  company_table_cols = company_table.tbody.tr.find_all('th')
  ticker = company_table_cols[0].text[:-1] #Ignore ending newline
  gics_sub_industry = company_table_cols[4].text
  #Wiki page calls it symbol instead of ticker
  if 'Symbol' != ticker or 'GICS Sub-Industry' != gics_sub_industry:
    print('Columns have been modified.')
    print(f'Symbol = {ticker}')
    print(f'GICS Sub-Industry = {gics_sub_industry}')
  else:
    print('Webpage verification successful.')
except Exception as e:
  print('There was an error scraping the webpage.')
  print(e)
      
################################################################################

"""
Tests that AlphaVantage's APIs maintains the structure expected.
""" 
try: 
  ticker = "MMM" #Example ticker
  api_key = sys.argv[1]
  income_statement_url = 'https://www.alphavantage.co/query?'\
  f'function=INCOME_STATEMENT&symbol={ticker}&apikey={api_key}'
  balance_sheet_url = 'https://www.alphavantage.co/query?'\
  f'function=BALANCE_SHEET&symbol={ticker}&apikey={api_key}'
  income_statement = requests.get(income_statement_url).json()
  balance_sheet = requests.get(balance_sheet_url).json()

  #Get current versions
  curr_income_statment = income_statement['annualReports'][0]
  curr_balance_sheet = balance_sheet['annualReports'][0]
  
  #Check that the fields needed are accessible
  latest_earnings = curr_income_statment['fiscalDateEnding']
  shares_outstanding = curr_balance_sheet['commonStockSharesOutstanding']
  st_debt = curr_balance_sheet['shortTermDebt']
  lt_debt = curr_balance_sheet['longTermDebt']
  cash = curr_balance_sheet['cashAndCashEquivalentsAtCarryingValue']
  revenue = curr_income_statment['totalRevenue']
  ebitda = curr_income_statment['ebitda']
  net_income = curr_income_statment['netIncome']

  #All good
  print('API verifcation successful.')
except Exception as e:
  print('There was an error using the APIs.')
  print(e)
