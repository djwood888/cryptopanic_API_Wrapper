import webbrowser
import config

# Access the API key
api_key = config.API_KEY

webbrowser.open('https://cryptopanic.com/developers/api/')

f = open("config.py", "w+")
f.write("API_KEY = api_key")
