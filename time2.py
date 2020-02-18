import time

starting_point = time.time()
time.sleep(9)
elapsed_time = time.time () - starting_point
elapsed_time_int = int(elapsed_time)

elapsed_time_minutes = elapsed_time_int / 60 
elapsed_time_seconds = elapsed_time_int % 60

print(elapsed_time_minutes)
print(elapsed_time_seconds)