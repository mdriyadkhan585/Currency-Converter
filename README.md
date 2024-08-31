# Currency-Converter
---
![Currency Converter Logo](logo.svg)

---
## Overview

The Currency Converter is a Python script that allows you to convert amounts between different currencies using live exchange rates. The script fetches real-time exchange rates from an API and provides a user-friendly command-line interface to perform currency conversions.

## Features

- **Live Exchange Rates**: Fetches real-time exchange rates for a wide range of currencies.
- **User-Friendly Interface**: Interactive command-line interface with clear instructions.
- **Dynamic Currency List**: Displays a comprehensive list of supported currencies.
- **Error Handling**: Handles invalid inputs and API errors gracefully.
- **Continuous Operation**: Allows users to perform multiple conversions in a single session.

## Requirements

- Python 3.x
- `requests` library
- `tabulate` library
- `colorama` library

You can install the required libraries using pip:

```bash
pip install requests tabulate colorama
```

## Usage

1. **Clone the Repository**

   Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/mdriyadkhan585/Currency-Converter.git
   ```

2. **Run the Script**

   Navigate to the directory containing the script and run it using Python:

   ```bash
   cd Currency-Converter
   python currency_converter.py
   ```

3. **Interact with the Script**

   - The script will display a list of supported currencies.
   - Enter the base currency code (e.g., USD) when prompted.
   - Enter the target currency code (e.g., EUR).
   - Enter the amount to convert.
   - The script will display the converted amount.

   To exit the program, type `exit` at any prompt.

## Example

```plaintext
Supported Currencies
+--------------+--------------------------+
| Currency Code| Currency Name            |
+--------------+--------------------------+
| USD          | United States Dollar     |
| EUR          | Euro                     |
| ...          | ...                      |
+--------------+--------------------------+

Enter 'exit' to quit the program at any time.
Enter base currency code (e.g., USD): USD
Enter target currency code (e.g., EUR): EUR
Enter amount to convert: 100

100.00 USD is equal to 85.00 EUR
```

## Contributing

Contributions are welcome! If you find a bug or have suggestions for improvements, please open an issue or submit a pull request.

## Acknowledgements

- **Exchange Rate API**: [ExchangeRate-API](https://www.exchangerate-api.com/)
- **Tabulate Library**: [Tabulate](https://pypi.org/project/tabulate/)
- **Colorama Library**: [Colorama](https://pypi.org/project/colorama/)


### Notes:

- Replace `https://github.com/mdriyadkhan585/Currency-Converter.git` with the actual URL of your repository.
- Adjust any additional details as necessary based on your project's specific features or instructions.

