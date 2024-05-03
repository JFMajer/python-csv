from pathlib import Path
import csv
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

matplotlib.use('TkAgg')

for index, column in enumerate(header_row):
    print(index, column)

# Initialize lists
highs = []
lows = []
dates = []

# Process each row once
for row in reader:
    high = int(row[4])
    low = int(row[5])
    date = datetime.strptime(row[2], '%Y-%m-%d')

    highs.append(high)
    lows.append(low)
    dates.append(date)

# plot temperatures
plt.style.use('seaborn-v0_8-deep')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red')
ax.plot(dates, lows, color='blue')

ax.set_title("Daily high and low temperatures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
