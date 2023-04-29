# Google Sheets as a Data Warehouse: Extracting and Storing Facebook Ads Data
This project provides a step-by-step guide to extract data from Facebook Ads API using Python and store it in Google Sheets. By using Google Sheets as a data warehouse, you can easily manage and analyze your data from different sources in a single location.

### Prerequisites
* A Facebook Ads account with API access
* A Google Cloud Platform account with the Google Drive API and Google Sheets API enabled
* Python 3.6 or higher
* pip package manager

### Installation
1. Clone the repository: `git clone https://github.com/leonardohss0/google-sheets-as-a-data-warehouse.git`
2. Install the required Python libraries: `pip install -r requirements.txt`
3. Follow the steps in MEDIUM to set up your Google Cloud and Facebook Ads API credentials.

### Usage
1. Run the script app.py to extract data from Facebook Ads API and store it in Google Sheets: `python -u -m facebook_flow`
2. The script will prompt you to authenticate with Google using your Google Cloud credentials.
3. Once authenticated, the script will extract data from Facebook Ads API and insert it into the 4. Google Sheet specified in the SPREADSHEET_ID variable in config.py.
5. You can schedule the script to run at regular intervals using a cron job or other scheduling tool.

### Troubleshooting
* If you encounter any errors during installation or usage, please refer to the documentation for the libraries used in this project.
* If you encounter any issues with the Facebook Ads API or Google Sheets API, please refer to the official documentation or seek help from the respective support channels.

### Contributing
If you have any suggestions or improvements for this project, please feel free to create a pull request or open an issue. We welcome contributions from the community!

License
This project is licensed under the MIT License. See the LICENSE file for details.
