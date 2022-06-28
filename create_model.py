"""
A module to create a trading comparison model for a given company. 
"""

def get_base_data(ticker, testing=False):
  """
  Gets from the database the base data needed to value 'ticker.' Base data is 
  defined below under returns. 
  
  args: 
    ticker (str): The ticker for the company being modeled.
    testing (bool): Whether or not we are testing, determining whether or not to 
    use the testing database.
  
  returns:
    base_data (list): A list of tuples featuring the ticker, shares 
    outstanding, net debt, revenue, ebitda, and net income of all companies that 
    are a part of the same GICS sub-industry as 'ticker.'
  """

def get_price_data(tickers):
  """
  Gets the current share price of all companies in 'tickers.'
  
  args:
    tickers (set): The tickers of all companies that are a part of this model. 
  
  returns:
    price_data (dict): A dict mapping ticker to share price. 
  """
  
def calculate_model_data(base_data, price_data):
  """
  Calculates core model data points from the 'base_data' on these companies and 
  real-time 'price_data.' 
  
  args: 
    base_data (list): A list of tuples featuring the ticker, shares outstanding, 
    net debt, revenue, ebitda, and net income of all companies that are a part 
    of this model.
    price_data (dict): A dict mapping ticker to share price. 
    
  returns:
    model_data (list): A list of tuples featuring the ev/revenue, ev/ebitda, and 
    p/e values of the companies in this model.
  """

def calculate_statistics(model_data):
  """
  Calculates the high, 75th percentile, average, median, 25th percentile, and 
  low of each valuation metric for the companies in 'model_data.'
  
  args:
    model_data (list): A list of tuples featuring the ev/revenue, ev/ebitda, and 
    p/e values of the companies in this model.
  
  returns:
    statistics (list): A list of tuples featuring the statistics mentioned in 
    the docstring for ev/revenue, ev/ebitda, and p/e values.
  """

def calculate_ivps(ticker, model_data, statistics):
  """
  Calculates the implied value per share for the company being modeled. 
  
  args:
    ticker (str): The ticker for the company being modeled.
    model_data (list): A list of tuples featuring the ev/revenue, ev/ebitda, and 
    p/e values of the companies in this model.
    statistics (list): A list of tuples featuring the statistics for ev/revenue, 
    ev/ebitda, and p/e values.     

  returns: 
    ivps (float): The implied value per share of the company being modeled.
  """

def model(ticker, complete=False):
  """
  Creates a trading comparison model for the company associated with 'ticker.' 
  If 'complete,' then all the data for the model is returned. Otherwise, just 
  the central point on whether the company is undervalued is returned.
  
  args:
    ticker (str): The ticker for the company being modeled.
  
  returns (complete=True):
    base_data (list): A list of tuples featuring the ticker, shares 
    outstanding, net debt, revenue, ebitda, and net income of all companies that 
    are a part of the same GICS sub-industry as 'ticker.'
    price_data (dict): A dict mapping ticker to share price. 
    model_data (list): A list of tuples featuring the ev/revenue, ev/ebitda, and 
    p/e values of the companies in this model.
    statistics (list): A list of tuples featuring the statistics mentioned in 
    the docstring for ev/revenue, ev/ebitda, and p/e values.
    ivps (float): The implied value per share of the company being modeled.
    
  returns (complete=False)
    undervalued (bool): Whether or not the company being modeled is undervalued 
    per the model generated.
  """








