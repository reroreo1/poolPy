from datetime import datetime , date

dt = datetime(2018, 10, 22, 0, 0)
# epoch time
epoch_time = datetime(1970, 1, 1)

# subtract Datetime from epoch datetime
delta = (dt - epoch_time)
delta = delta.total_seconds()
# check precision later for datetime
print('Seconds since January 1, 1970:',f"{ delta:,.2f}" , "or " ,"{:.2e}".format(delta))
today = date.today().strftime("%b-%d-%Y").split("-")
print(*today)