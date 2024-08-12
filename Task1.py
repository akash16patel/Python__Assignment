import yfinance as yf
import pandas as pd
from flask import Flask, jsonify, render_template_string
import os

# Define the tickers and corresponding file names
tickers = {
    '^NSEI': {'csv': 'nifty_historical_data.csv'},
    '^NSEBANK': {'csv': 'banknifty_historical_data.csv'},
    'NIFTY_FIN_SERVICE.NS': {'csv': 'finnifty_historical_data.csv'}
}

# Create 'data' directory if it does not exist
if not os.path.exists('data'):
    os.makedirs('data')


def fetch_and_save_data():
    """
    Fetches historical data for defined tickers and saves it as CSV files.
    """
    today = pd.Timestamp.now().strftime('%Y-%m-%d')

    for ticker, files in tickers.items():
        try:
            print(f"Fetching data for {ticker}")
            df = yf.download(ticker, start='1900-01-01', end=today)

            if df.empty:
                print(f"No data found for {ticker}")
                continue

            df.reset_index(inplace=True)
            csv_file_path = os.path.join('data', files['csv'])

            # Save data as CSV with margins (extra blank rows for readability)
            df.to_csv(csv_file_path, index=False, float_format='%.2f')

            # Add margins to the CSV file
            with open(csv_file_path, 'r') as file:
                lines = file.readlines()

            # Insert a blank line after the header
            lines.insert(1, '\n')

            with open(csv_file_path, 'w') as file:
                file.writelines(lines)

            print(f"Data for {ticker} saved as CSV successfully.")
        except Exception as e:
            print(f"Failed to fetch data for {ticker}: {e}")


# Create Flask app
app = Flask(__name__)


@app.route('/')
def home():
    """
    Provides a home page with links to API endpoints for data access.
    """
    return render_template_string('''
        <h1>Welcome to the NSE HISTORICAL DATA API</h1>
        <p>Use the following endpoints to access the data:</p>
        <ul>
            <li><a href="/data/^NSEI">Nifty Index Data (^NSEI)</a></li>
            <li><a href="/data/^NSEBANK">Bank Nifty Data (^NSEBANK)</a></li>
            <li><a href="/data/NIFTY_FIN_SERVICE.NS">Fin Nifty Data (NIFTY_FIN_SERVICE.NS)</a></li>
        </ul>
    ''')


@app.route('/data/<ticker>', methods=['GET'])
def get_data(ticker):
    """
    Returns historical data for the specified ticker in CSV format.

    :param ticker: The ticker symbol for which data is requested.
    :return: JSON representation of the historical data or error message.
    """
    # Sanitize ticker input
    ticker = ticker.strip()

    # Map ticker to file names
    files = tickers.get(ticker)

    if not files:
        return jsonify({'error': 'Invalid ticker specified'}), 404

    csv_file_path = os.path.join('data', files['csv'])

    if not os.path.isfile(csv_file_path):
        return jsonify({'error': 'Data file not found for the specified ticker'}), 404

    try:
        # Read the data from CSV file
        df = pd.read_csv(csv_file_path)

        if df.empty:
            return jsonify({'error': 'No data found in file'}), 404

        # Convert DataFrame to dictionary
        data = df.to_dict(orient='records')

        # Format the data into a more suitable view as a table
        formatted_data = [{"Date": record['Date'],
                           "Open": f"{record['Open']:.2f}",
                           "High": f"{record['High']:.2f}",
                           "Low": f"{record['Low']:.2f}",
                           "Close": f"{record['Close']:.2f}",
                           "Volume": int(record['Volume'])} for record in data]

        return jsonify(formatted_data)
    except Exception as e:
        return jsonify({'error': f"An error occurred: {str(e)}"}), 500


if __name__ == '__main__':
    # Data fetching and saving is to be performed before starting the Flask server
    fetch_and_save_data()
    # The Flask server is to be run
    print("Server is running. Access the API endpoints to view the data.")
    app.run(debug=True)
