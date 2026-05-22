# README 💱 Currency Exchange Rate Checker

## Overview

This Python script fetches real-time currency exchange data from the ExchangeRate API and compares two currencies entered by the user. It calculates the exchange ratio between them using live conversion rates.

Tiny forex robot. Big spreadsheet energy. 📈🤖

---

## Features

* Fetches live exchange rates using an external API
* Accepts two currency codes from the user
* Parses JSON response data
* Performs exchange rate calculations
* Displays conversion information in a readable format

---

## Requirements

Install the required package before running the script:

```bash
pip install requests
```

---

## Technologies Used

* Python 3
* `requests` library
* JSON API handling
* ExchangeRate API

API Provider:

[ExchangeRate API](https://www.exchangerate-api.com/?utm_source=chatgpt.com)

---

## How It Works

1. The program sends an HTTP GET request to the ExchangeRate API.
2. The API returns currency conversion data in JSON format.
3. The user enters two currency codes.
4. The script retrieves their exchange rates relative to USD.
5. It compares the rates and prints the conversion relationship.

Example:

```text
Currency 1: INR
Currency 2: USD

1 USD = 83.12 INR
```

---

## Supported Currency Codes

Examples:

| Currency      | Code |
| ------------- | ---- |
| US Dollar     | USD  |
| Indian Rupee  | INR  |
| Euro          | EUR  |
| Japanese Yen  | JPY  |
| British Pound | GBP  |

---

## Running the Program

```bash
python currency_converter.py
```

---

## Example Code Structure

```python
response = requests.get(BASE_URL)
api_data = response.json()

currency_1 = input("Currency 1: ")
currency_2 = input("Currency 2: ")
```

---

# What I Would Improve 🔧

Your project already demonstrates:

* API integration
* JSON parsing
* User input handling
* Basic arithmetic operations

Now for the upgrade pack ⚙️

## 1. Fix Currency Conversion Logic

Current logic compares rates instead of directly converting between currencies.

Better formula:

```python
converted_rate = currency_2_rate / currency_1_rate
```

Then:

```python
print(f"1 {currency_1} = {converted_rate:.2f} {currency_2}")
```

---

## 2. Add Error Handling

Right now the program crashes if:

* Internet connection fails
* Currency code is invalid
* API is unavailable

Example improvement:

```python
try:
    response = requests.get(BASE_URL)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
```

---

## 3. Validate Currency Codes

Currently:

```python
currency_1_rate = api_data["conversion_rates"][currency_1]
```

This throws a `KeyError` for invalid codes.

Safer version:

```python
if currency_1 not in rates:
    print("Invalid currency code")
```

---

## 4. Use Uppercase Automatically

Users may type `inr` instead of `INR`.

Improvement:

```python
currency_1 = input("Currency 1: ").upper()
currency_2 = input("Currency 2: ").upper()
```

---

## 5. Allow Amount Conversion

Currently it only compares currencies.

Much more useful:

```python
amount = float(input("Amount: "))
converted = amount * (currency_2_rate / currency_1_rate)
```

Example:

```text
100 USD = 8312 INR
```

---

## 6. Hide API Key

The API key should not be hardcoded directly into the script.

Better:

```python
import os
API_KEY = os.getenv("API_KEY")
```

This keeps secrets safer 🔐

---

## 7. Improve Output Formatting

Current output can contain long decimals.

Cleaner:

```python
print(f"{amount} {currency_1} = {converted:.2f} {currency_2}")
```

---

## 8. Make the Code Modular

Functions make the project easier to maintain.

Example:

```python
def fetch_rates():
    pass

def convert_currency():
    pass
```

---

# Suggested Final Version Structure 🧠

```text
currency_converter/
│
├── currency_converter.py
├── requirements.txt
├── README.md
└── .env
```

---