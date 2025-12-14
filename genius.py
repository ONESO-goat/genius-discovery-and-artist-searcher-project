import requests
import api_key
import pandas as pd
from IPython.core.display import HTML



client_access_token = api_key.your_client_access_token
search_term = "Missy-Elliott"
genius_search_url = f"http://api.genius.com/search?q={search_term}&access_token={client_access_token}"

response = requests.get(genius_search_url)
print(response)

 