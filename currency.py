import requests
from APIKEYS import *

# Base URL for the Free Currency API
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY_CURRENCY}"

# List of currencies to convert to
CURRENCIES = ["USD", "EUR", "AUD"]

def convert_currency(base):
    """
    Converts the base currency to the currencies listed in CURRENCIES.
    """
    # Constructs the request URL with the specified parameters
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)  # Sends the GET request to the API
        data = response.json()  # Parses the JSON response
        return data["data"]
    except Exception as e:
        print("Failed to retrieve currency data:", e)
        return None

# Main loop for currency conversion input/output
while True:
    base = input("Enter the base currency (q to quit): ").upper()
    
    if base == "Q":
        break
    if base not in CURRENCIES:
        print("Please enter a valid currency from the list:", ", ".join(CURRENCIES))
        continue
    try:
        amount = int(input("How much: "))
    except ValueError:
        print("Please enter a valid number for the amount.")
        continue
        
    data = convert_currency(base)
    if not data:
        continue
    del data[base]  # Removes the base currency from the results to prevent self-conversion display
    
    # Displays the conversion results
    for ticker, value in data.items():
        print(f"{ticker}: {value * amount}")
