time_first = int(input())
time_second = int(input())
time_third = int(input())
total_time = time_first+time_second+time_third
minutes = 0
seconds = 0
if total_time >= 60:
    minutes = total_time//60
seconds = total_time%60

print(f"{minutes}:{seconds:02d}")