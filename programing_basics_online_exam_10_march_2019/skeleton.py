min_control = int(input())
sec_control = int(input())
long_place = float(input())
seconds_per_100m = int(input())
control_in_sec = min_control * 60 + sec_control
time_lose = long_place / 120
total_lose_time = time_lose * 2.5
time_martin = (long_place / 100) * seconds_per_100m - total_lose_time
if control_in_sec >= time_martin:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {time_martin:.3f}.")
else:
    print(f"No, Marin failed! He was {(time_martin - control_in_sec):.3f} second slower.")
