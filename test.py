from datetime import datetime

date = datetime(2023,12,17)
date1 = datetime.now()
print(datetime.timestamp(date))
print(datetime.timestamp(date1),'now')