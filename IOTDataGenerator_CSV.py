'''
IOT Data Format:
StationID: int, 1000000-10099, 10% send message every seconds
Date: text, format 'yyyymmdd'
DateTime: timestamp, UTC milliseconds, format: 'YYYY-MMM-DDTHH:MI:SS.SSS'
Speed: float, xxx.xx
Volume: int, xxxxx
'''

import csv
import datetime
import random


with open('c:\\test.csv', 'w') as csvfile:
    header = ['StationID', 'Date', 'DateTime', 'Day', 'Speed', 'Volume']
    writer = csv.DictWriter(csvfile, fieldnames=header, delimiter=',', lineterminator='\n') # Windows default terminator is "\r\n"
    writer.writeheader()
    counter = 0
    start_time=datetime.datetime(2016,1,1)

    while (counter <= 86400) : # 24*60*6*10 = 8640, 10 days
        Date = start_time.strftime('%Y%m%d')
        DateTime = start_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:23]
        Day = start_time.strftime('%w')

        for i in range(10): # Every 10 stations generate IOT message from 100 stations
            StationID=random.randint(100000,100099)
            Speed = '{0:.2f}'.format(random.uniform(1,160))
            Volume = random.randint(1,9999)
            writer.writerow({'StationID':StationID, 'Date':Date,
                            'DateTime':DateTime, 'Day':Day, 'Speed':Speed, 'Volume':Volume})

        start_time += datetime.timedelta(seconds=10) # changed from milliseconds=1 to seconds
        counter += 1

