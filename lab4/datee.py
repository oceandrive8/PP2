#Exercise 1
import datetime
x=datetime.datetime.now()
print("Current time:",x)
fiveda=x - datetime.timedelta(days=5)
print("Five days ago:",fiveda)


#Exercise 2
import datetime
today=datetime.datetime.now()
yesterday=today-datetime.timedelta(days=1)
tomorrow=today+datetime.timedelta(days=1)
print( "Yesterday:", yesterday, "\nToday:", today, "\nTomorrow:", tomorrow)


#Exercise 3
import datetime
x=datetime.datetime.now()
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#creating new format of datetime with strftime methiod


#Exercise 4
import datetime
date1 = datetime.datetime(2020, 12, 23, 0, 45)
date2 = datetime.datetime(2020, 7, 24, 0, 23)
differ = date1 - date2
diffsec= differ.total_seconds()
print("Difference in seconds:", diffsec)
#we give dates as an example so we get new date its their difference 