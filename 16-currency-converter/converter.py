"""
API Integration: You will need to fetch real-time financial data by sending HTTP requests to an external service, 
such as the Free Currency Converter API. This is a fundamental skill for building dynamic applications.
JSON Handling: The data you receive from the API will be in JSON format. You'll learn how to parse this data to 
extract the specific exchange rate information you need.
Mathematical Operations: Once the exchange rate is retrieved, you'll perform standard arithmetic to calculate 
the final converted amount based on the user's input.
Data Formatting: Implementing logic to handle input currencies and target currencies, ensuring the output is
formatted correctly as a currency value.
Error Handling: It is good practice to include checks for potential issues, such as invalid API responses, 
network connectivity problems, or unsupported currency codes.
"""
import json, requests

API_KEY="92f1bfcb5769f089595493c4"
BASE_URL="https://v6.exchangerate-api.com/v6/92f1bfcb5769f089595493c4/latest/USD"
response=requests.get(BASE_URL)
api_data=response.json()
currency_1=input("Currency 1: ")
currency_2=input("Currency 2: ")
rates = api_data["conversion_rates"]
currency_1_rate = api_data["conversion_rates"][currency_1]
currency_2_rate = api_data["conversion_rates"][currency_2]
if currency_1 in api_data["conversion_rates"] and currency_2 in api_data["conversion_rates"]:
    if currency_1_rate>currency_2_rate:
        x=currency_1_rate/currency_2_rate
        print(f"1 {currency_2} = {x} {currency_1}")
    else:
        x=currency_2_rate/currency_1_rate
        print(f"1 {currency_1} = {x} {currency_2}")




