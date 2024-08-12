import json
from datetime import datetime

# File paths for input and output are defined
input_file_path = 'data/NIFTYoption_chain.json'  # Path to the input JSON file
output_file_path = 'data/NIFTYoption_chain_filtered.json'  # Path for the output JSON file

# JSON data is loaded from the input file
with open(input_file_path, 'r') as file:
    data = json.load(file)

def extract_last_trading_date(data):
    """
    Data corresponding to the last trading date is extracted for each record.

    Parameters:
        data (dict): The input JSON data with trading information.

    Returns:
        dict: Filtered data with records for the last trading date.
    """
    filtered_data = {}  # A dictionary is initialized to hold filtered data

    # Each record in the dataset is iterated over
    for key, value in data.items():
        # Existence of 'data' key in the record is checked
        if 'data' in value:
            # Date values are extracted and converted to datetime objects
            dates = list(value['data']['date'].values())
            if not dates:
                continue
            dates = [datetime.fromisoformat(date.replace('Z', '+00:00')) for date in dates]

            # The most recent (last) trading date is found
            last_date = max(dates)
            last_date_str = last_date.isoformat()  # Datetime is converted to ISO format string

            # The filtered record for this key is initialized
            filtered_data[key] = {
                'strike_price': value['strike_price'],
                'ot': value['ot'],
                'data': {
                    'date': {},
                    'open': {},
                    'high': {},
                    'low': {},
                    'close': {},
                    'volume': {},
                    'oi': {},
                    'vwap': {},
                    'supertrend': {},
                    'trend': {},
                    'sma': {}
                }
            }

            # Information for the last trading date is included
            for i, date in enumerate(dates):
                if date == last_date:
                    for field in filtered_data[key]['data']:
                        filtered_data[key]['data'][field][str(i)] = value['data'][field][str(i)]

    return filtered_data  # The filtered data dictionary is returned

# Function is called to filter data based on the last trading date
filtered_data = extract_last_trading_date(data)

# Filtered data is saved to the output JSON file
with open(output_file_path, 'w') as file:
    json.dump(filtered_data, file, indent=4)  # JSON data is written with indentation

print(f"Filtered data has been saved to {output_file_path}")  # Confirmation message is printed
