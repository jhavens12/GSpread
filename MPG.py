import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import datetime

import matplotlib.pyplot as plt
import pylab
import matplotlib.dates as mdates
from pprint import pprint
import numpy as np

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
client = gspread.authorize(creds)

sheet = client.open('2015 Mazda 3 Gas Mileage').sheet1

sheet_data = sheet.get_all_values()

def convert_TS(i):
    return datetime.datetime.strptime(i, "%m/%d/%Y")

del sheet_data[0]
odo_dict = {}
mpg_dict = {}

for fuelup in sheet_data:
    odo_dict[convert_TS(fuelup[0])] = int(fuelup[1])
    mpg_dict[convert_TS(fuelup[0])] = float(fuelup[4])

pprint(mpg_dict)

fig, ax1 = plt.subplots()

ax1.plot(list(odo_dict.keys()),list(odo_dict.values()),'b')
ax1.set_xlabel('date')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('ODO Reading', color='b')
ax1.tick_params('y', colors='b')

ax2 = ax1.twinx()
ax2.plot(list(mpg_dict.keys()),list(mpg_dict.values()),'r')
ax2.set_ylabel('MPG', color='r')
ax2.tick_params('y', colors='r')

fig.tight_layout()
plt.show()






# plt.plot(list(odo_dict.keys()),list(odo_dict.values()),label=('ODO Reading'))
# #plt.plot(list(yearly_dict2.keys()),list(yearly_dict2.values()),label=('Last Year'))
#
# plt.style.use('dark_background')
# plt.rcParams['lines.linewidth'] = 1
# plt.ylim(ymin=0)
# plt.title('Odometer')
# plt.legend()
# plt.show()
