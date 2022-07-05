"""
Utility functions to help with networked logic. 
"""

def fetch_webpage(url, ret_none=False):
  """
  Fetches the HTML of the webpage located at the passed in 'url.' Errors and 
  failures are logged. 
   
  args: 
    url (str): The URL of some webpage. 
    ret_none (bool): Whether or not to return None for testing purposes. 
  
  returns:
    html (str): The HTML of that webpage. None if there are errors or failures. 
  """  
  html = ''
  return html

def fetch_api_data(ticker, data_point, ret_none=False):
  """
  Fetches the latest measure (on a trailing 12-month basis for financial 
  statement line item data or the last quote for price data) of 'data_point' for 
  'ticker.' Errors and failures are logged.
  
  args:
    ticker (str): The ticker of some company. 
    data_point (str): The data point wanted.
    ret_none (bool): Whether or not to return None for testing purposes. 
  
  returns:
    data (str): The data wanted. Conversion, if needed, is handled by the 
    caller. None if there are errors or failures.
  """
  data = ''
  return data

def db_write(query, parameters=None):
  """
  Facilitates the execution of 'query' with, if relevant, 'parameters,' 
  resulting in a write to the database. Errors and failures are logged.
  
  args:
    query (str): The SQL query facilitating the write. 
    parameters (list): A list of parameters that the query is executed 
    against.
  """

def db_read(query, parameters=None, ret_none=False):
  """
  Facilitates the execution of 'query' with, if relevant, 'parameters,' 
  resulting in reading records from the database. Errors and failures are 
  logged.
  
  args:
    query (str): The SQL query facilitating the read. 
    parameters (list): A list of parameters that the query is executed 
    against. 
    ret_none (bool): Whether or not to return None for testing purposes. 
    
  returns: 
    data (list): A list of tuples where the tuples correspond to the rows 
    returned by the passed in SQL query. None if there are errors or failures.
  """
  data = []
  return data