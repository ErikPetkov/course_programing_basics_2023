record_in_secunds = float(input())
record_in_meters = float(input())
time_in_wich_he_swims_meter = float(input())
time = record_in_meters*time_in_wich_he_swims_meter
time_added = (record_in_meters // 15)*12.5
total_time = time+time_added
if record_in_secunds > total_time:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(total_time-record_in_secunds):.2f} seconds slower.")
