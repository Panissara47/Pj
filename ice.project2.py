import requests
import tkinter as tk
from tkinter import ttk

# Replace with your API key
api_key = 'd112c20c01e9ec348c2298da4a49e130'

def convert_currency():
    # API URL
    api_url = f'http://api.exchangeratesapi.io/v1/latest?access_key={api_key}'
    # Make a request to the API
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to access data. Status code: {response.status_code}")

def currency_converter(amount, from_currency, to_currency):
    data = convert_currency()
    # Check if the provided currencies exist in the data
    if from_currency not in data['rates'] or to_currency not in data['rates']:
        print("Invalid currency codes.")
        return None
    # Get the exchange rates
    from_rate = data['rates'][from_currency]
    to_rate = data['rates'][to_currency]
    # Perform the conversion
    converted_amount = (amount / from_rate) * to_rate
    return converted_amount

def on_convert():
    amount = float(amount_entry.get())
    from_currency = from_currency_combobox.get().upper()
    to_currency = to_currency_combobox.get().upper()

    converted_amount = currency_converter(amount, from_currency, to_currency)
    if converted_amount is not None:
        result_label.config(text=f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}")

# GUI setup
root = tk.Tk()
root.title("Currency Converter")

# Amount entry
amount_label = tk.Label(root, text="Enter the amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

# Source currency combobox
from_currency_label = tk.Label(root, text="Enter the source currency:")
from_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
from_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "AUD"])
from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)

# Target currency combobox
to_currency_label = tk.Label(root, text="Enter the target currency:")
to_currency_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
to_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "AUD"])
to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=on_convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()