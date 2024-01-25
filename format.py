"""

CryptoPanic API Formatter.

Use Wrapper to make calls and get data.
Format data for streaming input and monitoring.
Historical Data seems to be limited to 12/24/2018 but there is no Documentation.

"""
import api_gather

# main_script.py
import config

# Access the API key
api_key = config.API_KEY

from importlib import reload
reload(api_gather)

# Assuming 'make_url' returns a URL string
url_everything = api_gather.make_url(filter='important')

# Append the BTC currency filter to the URL query string
url_everything += '&currencies=BTC'  

everything_pages_last_200 = api_gather.get_pages_list_json(9, url_everything)

everything_pages_last_200_results = []
for page in everything_pages_last_200:
    everything_pages_last_200_results.append(page['results'])
df_results = api_gather.concatenate_pages(everything_pages_last_200_results)
