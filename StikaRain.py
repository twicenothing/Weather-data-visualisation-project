import csv
from datetime import datetime
import matplotlib.pyplot as plt

filee = 'data/sitka_weather_2018_simple.csv'

with open(filee) as f:
    reader = csv.reader(f)
    header = next(reader)
    prcp = []
    dates = []
    
    for row in reader:
        daily_prcp = float(row[3])
        date = datetime.strptime(row[2],'%Y-%m-%d')
        prcp.append(daily_prcp)
        dates.append(date)
    
    print(prcp)

# visualisation

fig, ax = plt.subplots()
ax.plot(dates,prcp, c='red')
plt.title('Daily precipitation in Sitka, Alaska',fontsize = 24)
plt.xlabel('Dates',fontsize = 12)
plt.ylabel('Precipitation', fontsize = 12)

plt.show()


