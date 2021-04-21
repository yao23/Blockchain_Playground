import httplib2
import os
import gspread
import datetime

# from apiclient import discovery
# from google.oauth2 import service_account
from google.oauth2.service_account import Credentials

from binance.client import Client

# bian info
api_key = 'YOUR_KEY'
api_secret = 'YOUR_SECRET'
client = Client(api_key, api_secret)

spot = client.get_account_snapshot(type='SPOT')
print('spot info: ')
for k, v in spot.items():
    print(k, v)
s_balance = spot.get('snapshotVos')[-1].get('data').get('totalAssetOfBtc')

print('------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

future = client.get_account_snapshot(type='FUTURES')
print('future info: ')
for k, v in future.items():
    print(k, v)
f_balance = future.get('snapshotVos')[-1].get('data').get('assets')[-1].get('walletBalance')

try:
    # https://denisluiz.medium.com/python-with-google-sheets-service-account-step-by-step-8f74c26ed28e
    # https://developers.google.com/sheets/api/guides/batchupdate
    # scopes = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/spreadsheets"]
    # secret_file = os.path.join(os.getcwd(), 'client_secret.json')

    # spreadsheet_id = 'YOUR_SHEET_ID'
    # range_name = 'Sheet1!A1:D2'

    # credentials = service_account.Credentials.from_service_account_file(secret_file, scopes=scopes)
    # service = discovery.build('sheets', 'v4', credentials=credentials)
    
    # values = [
    #     ['a1', 'b1', 'c1', 123],
    #     ['a2', 'b2', 'c2', 456],
    # ]

    # data = {
    #     'values' : values 
    # }

    # service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, body=data, range=range_name, valueInputOption='USER_ENTERED').execute()

    # https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account
    # https://stackoverflow.com/questions/62351484/insert-values-into-first-empty-row-in-google-sheets
    scopes = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    # creds = ServiceAccountCredentials.from_json_keyfile_name("client_secret.json", scope)
    creds = Credentials.from_service_account_file(os.path.join(os.getcwd(), 'client_secret.json'), scopes=scopes)
    client = gspread.authorize(creds)
    sheet = client.open('Balance').sheet1
    data = sheet.get_all_records()
    # today = datetime.today().strftime('%m-%d-%Y')
    # today = datetime.datetime.strptime(date, "%m/%d/%Y")
    today = datetime.date.today().strftime('%m/%d/%Y')
    # insertRow = [today, 'Person', '1000', 'Bank']
    insertRow = [today, s_balance, f_balance]
    
    # row = sheet.row_values(4)
    sheet.append_row(insertRow, value_input_option='USER_ENTERED')
    # sheet.insert_row(row, 2)

    # data = sheet.get_all_values()
    # row = 0
    # for i, r in enumerate(data):
    #     if all([c == '' for c in r]) is True:
    #         row = i + 1
    #         break
    # today = datetime.today().strftime('%m-%d-%Y')
    # insertRow = ['Person', '1000', today, 'Bank']
    # spreadsheet.values_update('A' + str(row), params={'value_input_option': 'USER_ENTERED'}, body={'values': [insertRow]})

except OSError as e:
    print(e)



# # get market depth
# depth = client.get_order_book(symbol='BNBBTC')
# print('depth: ')
# for k, v in depth.items():
#     print(k, v)

# # get all symbol prices
# prices = client.get_all_tickers()
# print('prices: ' + str(prices)[1:-1] )