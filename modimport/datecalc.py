import time
from time import perf_counter as my_timer
import random

# print(time.gmtime(0))
#
# print(time.localtime())
#
# print(time.time())

time_here = time.localtime()
print(time_here)
print("Year:", time_here[0], time_here.tm_year)
print("Month:", time_here[1], time_here.tm_mon)
print("Day:", time_here[2], time_here.tm_mday)

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()
print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds".format(end_time - start_time))

# Write a small program to display information on the
# four clocks whose functions we have just looked at:
# i.e. time(), perf_counter, monotonic() and process_time().
#
# Use the documentation for the get_clock_info() function
# to work out how to call it for each of the clocks.

print("time() \t\t\t", time.get_clock_info('time'))
print("perf_counter()\t", time.get_clock_info('perf_counter'))
print("monotonic()\t\t", time.get_clock_info('monotonic'))
print("process_time()\t", time.get_clock_info('process_time'))
