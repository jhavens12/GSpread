import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open('Python_Test_Sheet').sheet1


#sheet.update_cell(3,3,'updated from google')
#sheet.delete_row(3)
#result = sheet.col_values(1)
#result = sheet.get_all_records()
val = sheet.acell('B1').value
pprint(val)
