# Morse Code Converter

This is a Python script that can encode and decode text to and from Morse code. It takes a string of text as input and outputs the equivalent Morse code signal or takes a Morse code signal as input and outputs the equivalent text.

## Usage

To use the script:

1. Import the `morse` dictionary from the script.
2. Call the `encode(text)` function to encode a string of text to Morse code. Replace `text` with the string of text to encode.
3. Call the `decode(code)` function to decode a Morse code signal to text. Replace `code` with the Morse code signal to decode.

## Example

Here's an example usage of the script:

```python
from morsecode import morse, encode, decode

# Encode a string of text to Morse code
text = "SOS"
code = encode(text, morse)
print(code)

# Decode a Morse code signal to text
code = "... --- ..."
text = decode(code, morse)
print(text)
```

## Author and license

This script was made by Karim Amr Elsayed Khater. It is not licensed and is free to use and modify.

## Future work

This script is a simple Morse code converter that can be improved in several ways:

- The script could be made more user-friendly by adding a command-line interface for easier input and output.
- The script could be extended to support additional encoding and decoding techniques for different types of signals.
- The script could be modified to handle errors and invalid input more gracefully.

# Leopard CSV Data Analyzer

This is a Python script that can read a CSV file and analyze the data within. The script can analyze numeric data columns to provide counts, means, minimums, and maximums for each column and generate an HTML report. It can also count the number of instances of a particular value in a specified column.

## Requirements

This script requires Python 3 and the `csv` module.

## Usage

To use the script:

1. Import the `Leopard` class from the script.
2. Create a `Leopard` object with the path to the CSV file as an argument.
3. Call the `get_header()` method to get the column headers.
4. Call the `get_data()` method to get the data rows.
5. Call the `stats()` method to get statistics for the numeric columns.
6. Call the `html_stats(stats, filepath)` method to generate an HTML report for the statistics. Replace `stats` with the statistics dictionary and `filepath` with the desired output file path.
7. Call the `count_instances(colhead, criteria)` method to count the number of instances of a particular value in a specified column. Replace `colhead` with the column header and `criteria` with the value to count.

## Example

Here's an example usage of the script:

```python
from leopard import Leopard

# Create a Leopard object with the path to the CSV file
test = Leopard("diabetes_data.csv")

# Get the column headers
print(test.get_header())

# Get the data rows
print(test.get_data())

# Get statistics for the numeric columns
stats = test.stats()
print(stats)

# Generate an HTML report for the statistics
test.html_stats(stats, "diabetes.html")

# Count the number of instances of a particular value in a specified column
count = test.count_instances("Glucose", "200")
print(count)
```

## Author and license

This script is not licensed and is free to use and modify.

## Future work

This script is a simple data analyzer that can be improved in several ways:

- The script could be made more user-friendly by adding command-line arguments for easier input and output file specification.
- The script could be made more robust by adding error handling for invalid input and unexpected errors.
- The script could be extended to support additional data analysis techniques and output formats.
