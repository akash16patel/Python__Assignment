# NSE Historical Data API

## Problem Statement
TASK 1:

1.fetch historical data for BANKNIFTY,NIFTY and FINNIFTY from NSE 
2. Process the data and save it in suitable format
3. create API using Flask to get this fetched data for single scrip


1. **Historical data for specific indices is to be fetched from Yahoo Finance.** The indices include:
   - Nifty Index (^NSEI)
   - Bank Nifty (^NSEBANK)
   - Fin Nifty (NIFTY_FIN_SERVICE.NS)

2. **The fetched data is to be saved as CSV files.** The files are to be named as follows:
   - `nifty_historical_data.csv` for ^NSEI
   - `banknifty_historical_data.csv` for ^NSEBANK
   - `finnifty_historical_data.csv` for NIFTY_FIN_SERVICE.NS

3. **A Flask web server is to be created.** The server is to provide endpoints to access the saved historical data.

## Project Setup

1. **Dependencies are to be installed.** Required packages are:
   - `yfinance`
   - `pandas`
   - `Flask`

2. **A `data` directory is to be created.** If this directory does not exist, it is to be created automatically.

3. **Historical data is to be fetched and saved.** The data is fetched from Yahoo Finance using the `yfinance` library and saved in the `data` directory as CSV files.

4. **The Flask server is to be started.** The server will provide the following endpoints:
   - `/data/^NSEI` - Access historical data for Nifty Index (^NSEI)
   - `/data/^NSEBANK` - Access historical data for Bank Nifty (^NSEBANK)
   - `/data/NIFTY_FIN_SERVICE.NS` - Access historical data for Fin Nifty (NIFTY_FIN_SERVICE.NS)

## Running the Project

1. **Ensure that all dependencies are installed.**

2. **Run the `task1` script.** This script will fetch and save the data, and then start the Flask server.
  python task1.py

3. ** After the server starts, access the API endpoints through a web browser or use tools like curl or Postman to request data from the provided endpoints.
  

What to Do After Server Start
Verify Data Retrieval:

Check that the CSV files (nifty_historical_data.csv, banknifty_historical_data.csv, finnifty_historical_data.csv) have been created in the data directory.
Access API Endpoints:

Open your web browser and navigate to the following URLs to access the data:
For Nifty Index data: http://127.0.0.1:5000/data/^NSEI
For Bank Nifty data: http://127.0.0.1:5000/data/^NSEBANK
For Fin Nifty data: http://127.0.0.1:5000/data/NIFTY_FIN_SERVICE.NS
some snippets to understand better 
![image](https://github.com/user-attachments/assets/1c4d7681-c2ce-4e04-a670-363e32f5d5fd)
![image](https://github.com/user-attachments/assets/387a0210-72c0-430b-b576-dd321974348f)
![image](https://github.com/user-attachments/assets/a204bc57-7597-4c1f-b59b-da52e7d6b1ea)
![image](https://github.com/user-attachments/assets/05a39b70-7171-498d-977d-100c092cbbf7)

## Problem Statement
TASK 2:
1.create a small python algo to keep running and stops after 10 mins. 
2. Implement the algorithm using Object-Oriented Programming (OOP) concepts.
3. Create a flask api to start this algo


A web server is needed to manage and execute a timer-based algorithm. The server should provide an interface for starting the algorithm and display instructions for usage. The following features are required:

1. An algorithm that runs for a specified duration of 10 minutes.
2. A web interface to start the algorithm via a `POST` request.
3. A welcome page with instructions on how to trigger the algorithm.

## Components

1. **BaseAlgorithm Class**
   - Common functionality and interface are provided.
   - `__init__(self, run_duration=600)`: Parameters are initialized.
   - `run(self)`: Abstract method is defined for subclass implementation.
   - `start(self)`: Algorithm is started in a separate thread if not already running.

2. **TimerAlgorithm Class**
   - Concrete implementation of the algorithm is provided to run for 10 minutes.
   - `run(self)`: Execution of the algorithm and status updates are handled.

3. **Flask Web Server**
   - **Routes:**
     - `/`: A welcome page with instructions is rendered.
     - `/start_algo`: Algorithm start is triggered via a `POST` request.
4. Run the Script:
   python Task2.py
 

# NIFTY Option Chain Data Filtering

## Problem Statement
TASK 3:
1.Given a JSON dataset, filter the data to include only the last trading date's information.
2. save the data in same format 


A script is needed to filter a JSON dataset of NIFTY option chain data to retain only the information corresponding to the most recent trading date. The dataset is structured with multiple records, each containing time series data. The task involves extracting and saving data for the latest trading date from this dataset.

## Dependencies

This script requires the following Python packages:

- `json` (standard library)
- `datetime` (standard library)

No additional installation is required for these libraries as they are part of the Python standard library.

## Functionality

1. **Data Loading:** JSON data is loaded from the specified input file.
2. **Data Filtering:** Data for each record is filtered to include only the information for the most recent trading date.
3. **Data Saving:** The filtered data is saved to an output JSON file.

## Components

1. **Input and Output Files:**
   - **Input File Path:** `data/NIFTYoption_chain.json` (Path to the input JSON file)
   - **Output File Path:** `data/NIFTYoption_chain_filtered.json` (Path to the output JSON file)

2. **Data Processing:**
   - **Data Extraction:** The most recent trading date is determined for each record.
   - **Data Filtering:** Data is filtered to retain only the records for the last trading date.
   - **Data Saving:** The filtered data is written to the output JSON file.

## Usage

1. **Prepare the Input File:**
   Ensure the input JSON file (`NIFTYoption_chain.json`) is located in the `data` directory.

2. **Run the Script:**
   Execute the script to process the data and generate the filtered output.


   python Task3.py
      
Task Summaries
Task 1: Fetch Historical Data
Summary:
Historical data for NIFTY, BANKNIFTY, and FINNIFTY indices is fetched from the NSE using Python. The data is saved in CSV format and served via a Flask API.

Requirements:

yfinance
pandas
flask
Task 2: Start Algorithm via Flask API
Summary:
A Flask API is created to start a timer-based algorithm running for 10 minutes. The algorithm is implemented using object-oriented programming (OOP) concepts and is run in a separate thread.

Requirements:

flask
logging
Task 3: Filter JSON Data by Last Trading Date
Summary:
A JSON dataset is filtered to include only the data corresponding to the most recent trading date. The filtered data is saved to a new JSON file.

Requirements:

Python standard libraries (json, datetime)

##Setup project
1. **Dependencies:**
   - `yfinance`
   - `pandas`
   - `flask`
   - Python standard libraries (`json`, `datetime`)

2. **Setup Instructions:**

   **1. Clone the Repository:**
   ```bash
   git clone <repository_url>
   cd <repository_directory>
3. ##Set Up a Virtual Environment (Optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

4.##Install Dependencies:
Ensure the requirements.txt file is in the project root directory
pip install -r requirements.txt

##Development Environment
IDE: PyCharm is used for developing and running the Python scripts.
   






