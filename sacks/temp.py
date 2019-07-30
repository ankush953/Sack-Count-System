import datetime as dt
import pytz

date_time_str = '07/04/2019'
date_time_obj = dt.datetime.strptime(date_time_str, '%m/%d/%Y')

timezone = pytz.timezone('Asia/Kolkata')
timezone_date_time_obj = timezone.localize(date_time_obj)

print(timezone_date_time_obj)
print(timezone_date_time_obj.tzinfo)