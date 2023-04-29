import gspread
import pandas as pd

from facebook_flow.scripts.facebook_scripts import getCampaignData
from facebook_flow.resources.config import ACCOUNT_ID, ACCESS_TOKEN, UNTIL, SINCE
from oauth2client.service_account import ServiceAccountCredentials

# Set the name of the Google Sheets file
file_name = "leonardohss-gsheets"

# Set the name of the worksheet within the Google Sheets file
worksheet_name = "facebook-data"

# Load the service account key
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("facebook_flow/secrets/leonardohss-gsheets-6d95497aa31d.json", scope)

# Authorize the client
client = gspread.authorize(creds)

# Open the worksheet
worksheet = client.open(file_name).worksheet(worksheet_name)

# Clear the existing contents of the worksheet
worksheet.clear()

# Load your dataframe into the worksheet
df =  getCampaignData(account_id=ACCOUNT_ID, access_token=ACCESS_TOKEN, until=UNTIL, since=SINCE) 
# df = pd.read_csv("facebook_flow/data/example_data.csv") # Try this to only pull the example data to the Google Sheets
df = df.astype(str)  # Convert all values to strings
worksheet.update([df.columns.values.tolist()] + df.values.tolist())