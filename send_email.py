"""
A script to scan over the set of S&P 500 companies, create an up-to-date model 
on each, and send an email featuring the tickers of companies found to be 
undervalued. 
"""

def find_undervalued_companies(testing=False):
  """
  Finds undervalued companies by creating an up-to-date model on each company 
  tracked.
  
  args: 
    testing (bool): Whether or not we are testing, determing whether or not to 
    use the testing database.
    
  returns: 
    undervalued_companies (set): The tickers of undervalued companies.
  """

def send_email(undervalued_companies):
  """
  Sends an email featuring listing the 'undervalued_companies.'
  
  args; 
    undervalued_companies (set): The tickers of undervalued companies.
  """

if __name__ == "__main__":
  undervalued_companies = find_undervalued_companies()  
  send_email(undervalued_companies)






