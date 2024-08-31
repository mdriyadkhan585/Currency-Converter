import requests
from tabulate import tabulate
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# Define a dictionary of currency codes and names
CURRENCY_CODES = {
    'USD': 'United States Dollar',
    'EUR': 'Euro',
    'JPY': 'Japanese Yen',
    'GBP': 'British Pound Sterling',
    'AUD': 'Australian Dollar',
    'CAD': 'Canadian Dollar',
    'CHF': 'Swiss Franc',
    'CNY': 'Chinese Yuan',
    'SEK': 'Swedish Krona',
    'NZD': 'New Zealand Dollar',
    'MXN': 'Mexican Peso',
    'SGD': 'Singapore Dollar',
    'HKD': 'Hong Kong Dollar',
    'NOK': 'Norwegian Krone',
    'KRW': 'South Korean Won',
    'TRY': 'Turkish Lira',
    'RUB': 'Russian Ruble',
    'INR': 'Indian Rupee',
    'BRL': 'Brazilian Real',
    'ZAR': 'South African Rand',
    'BDT': 'Bangladeshi Taka',
    'PKR': 'Pakistani Rupee',
    'THB': 'Thai Baht',
    'MYR': 'Malaysian Ringgit',
    'IDR': 'Indonesian Rupiah',
    'SAR': 'Saudi Riyal',
    'AED': 'United Arab Emirates Dirham',
    'CLP': 'Chilean Peso',
    'COP': 'Colombian Peso',
    'PEN': 'Peruvian Nuevo Sol',
    'DZD': 'Algerian Dinar',
    'EGP': 'Egyptian Pound',
    'MAD': 'Moroccan Dirham',
    'KWD': 'Kuwaiti Dinar',
    'BHD': 'Bahraini Dinar',
    'JOD': 'Jordanian Dinar',
    'OMR': 'Omani Rial',
    'LKR': 'Sri Lankan Rupee',
    'VND': 'Vietnamese Dong',
    'HUF': 'Hungarian Forint',
    'CZK': 'Czech Koruna',
    'PLN': 'Polish Zloty',
    'RON': 'Romanian Leu',
    'HRK': 'Croatian Kuna',
    'ISK': 'Icelandic Króna',
    'DOP': 'Dominican Peso',
    'NAD': 'Namibian Dollar',
    'MUR': 'Mauritian Rupee',
    'BMD': 'Bermudian Dollar'
}

def get_exchange_rate(base_currency, target_currency):
    url = f'https://api.exchangerate-api.com/v4/latest/{base_currency}'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200 and target_currency in data['rates']:
        return data['rates'][target_currency]
    else:
        raise ValueError('Invalid currency code or API request failed.')

def convert_currency(amount, base_currency, target_currency):
    try:
        rate = get_exchange_rate(base_currency, target_currency)
        return amount * rate
    except ValueError as e:
        print(Fore.RED + Style.BRIGHT + str(e) + Style.RESET_ALL)
        return None

def display_currency_list():
    headers = [Fore.YELLOW + "Currency Code" + Style.RESET_ALL, Fore.YELLOW + "Currency Name" + Style.RESET_ALL]
    table = [[code, name] for code, name in CURRENCY_CODES.items()]
    print(Fore.CYAN + Back.WHITE + " Supported Currencies " + Style.RESET_ALL)
    print(tabulate(table, headers=headers, tablefmt='grid', stralign='center', numalign='center'))

def format_currency(amount, currency_code):
    return f"{amount:,.2f} {currency_code}"

def main():
    display_currency_list()
    while True:
        print(Fore.CYAN + "\nEnter 'exit' to quit the program at any time." + Style.RESET_ALL)
        base_currency = input(Fore.GREEN + "Enter base currency code (e.g., USD): " + Style.RESET_ALL).upper()
        if base_currency == 'EXIT':
            break
        target_currency = input(Fore.GREEN + "Enter target currency code (e.g., EUR): " + Style.RESET_ALL).upper()
        if target_currency == 'EXIT':
            break
        try:
            amount = float(input(Fore.GREEN + "Enter amount to convert: " + Style.RESET_ALL))
            if amount < 0:
                print(Fore.RED + Style.BRIGHT + "Amount must be a positive number." + Style.RESET_ALL)
                continue
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "Invalid amount. Please enter a numeric value." + Style.RESET_ALL)
            continue
        
        converted_amount = convert_currency(amount, base_currency, target_currency)
        
        if converted_amount is not None:
            print(f"\n{Fore.CYAN + Style.BRIGHT + format_currency(amount, base_currency) + Style.RESET_ALL} is equal to {Fore.CYAN + Style.BRIGHT + format_currency(converted_amount, target_currency) + Style.RESET_ALL}")

if __name__ == "__main__":
    main()
