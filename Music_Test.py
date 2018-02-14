import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)


spreadsheet = client.open('GMusic Playlist Backup 2017.01.15')
sheet = spreadsheet.get_worksheet(1)

#sheet.update_cell(3,3,'updated from google')
#sheet.delete_row(3)
#result = sheet.col_values(1)
#result = sheet.get_all_records()
cells = sheet.col_values(1)
#cell = sheet.acell('A2').value

print(sheet)

print(cells[0])
del cells[0]

for cell in cells:
    if cell != '':
        sep1 = ','
        data = cell.split(sep1)
        artist = data[0]
        title = data[2].replace('"', "")

        print(cell)
        print(artist)
        print(title)
        print()
