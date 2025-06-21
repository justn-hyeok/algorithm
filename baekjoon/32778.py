import sys

station_info = sys.stdin.readline().strip()

open_idx = station_info.find('(')
close_idx = station_info.rfind(')')

if open_idx != -1 and close_idx != -1 and open_idx < close_idx:
    station_name = station_info[:open_idx].strip()
    sub_station_name = station_info[open_idx + 1:close_idx]
else:
    station_name = station_info
    sub_station_name = '-'

print(station_name)
print(sub_station_name)
