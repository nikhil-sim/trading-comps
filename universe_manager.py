"""
A module/script to help manage the system's tracking of the S&P 500. This 
includes methods to help process additions/deletion to the index and process 
data updates after a company releases earnings.
"""
      
def fetch_current_companies():  
  """
  Fetches the ticker and GICS sub-industry of the current companies that make up
  the S&P 500 by scraping the following url:
  https://en.wikipedia.org/wiki/List_of_S%26P_500_companies. Tickers are used 
  for ID and the GICS sub-industries are used to group together companies.
    
  returns:
    company_data (set): A set of tuples featuring the ticker and GICS 
    sub-industry of the current companies that make the S&P 500.
  """    
  company_data = set()
  return company_data

def fetch_tracked_tickers(testing=False):
  """
  Fetches from the database the tickers of the companies currently tracked by 
  the system as forming the S&P 500.

  args:
    testing (bool): Whether or not we are testing, determing whether or not to 
    use the testing database.
    
  returns: 
    tickers (set): The tickers of companies in the database.
  """
  tickers = set()
  return tickers

def calculate_changes(current_companies, tracked_companies):
  """
  Calculates additions and deletions to the S&P 500. 
    
  args:
    current_companies (set): The tickers of current S&P 500 companies. 
    tracked_companies (set): The tickers of companies currently tracked in the 
    database.
      
  returns:  
    additions (set): Tickers that represent additions to the index since the 
    system's last update.
    deletions (set): Tickers that represent deletions to the index since the 
    system's last update.
  """
  additions = set()
  deletions = set()
  return additions, deletions

def add_companies(additions, testing=False):
  """
  Adds the companies in additions to the database. The fields stored in the 
  database include the following (the ones not scraped are fetched via 
  AlphaVantange's API): latest earnings, ticker, GICS sub-industry, shares 
  outstanding, net debt, revenue, ebitda, and net income. Note that this is 
  not all the data required for a trading comps model. Data not included is 
  either complex data made up with what is stored or it is data that is needed
  in real-time. 
    
  args: 
    additions (set): The tickers and GICS sub-sector of companies recently 
    added to the S&P 500. 
    testing (bool): Whether or not we are testing, determing whether or not to 
    use the testing database.
  """
        
def delete_companies(deletions, testing=False):
  """
  Deletes the companies in deletions from the database. 
    
  args:
    deletions (set): The tickers of companies recently removed from the S&P 
    500. 
    testing (bool): Whether or not we are testing, determing whether or not to 
    use the testing database.
  """
              
def update_data(testing=False):
  """
  Updates the data of companies that have recently released earnings. 
  
  args: 
    testing (bool): Whether or not we are testing, determing whether or not to 
    use the testing database.
  """
  
if __name__ == "__main__":
  current_companies = fetch_current_companies()
  current_tickers = {c[0] for c in current_companies}
  
  tracked_tickers = fetch_tracked_tickers()
  
  additions_tickers, deletions_tickers = calculate_changes(current_tickers, 
                                                           tracked_tickers)
  additions = {c for c in current_companies if c[0] in additions_tickers}
  
  delete_companies(deletions_tickers)
  update_data()
  add_companies(additions)