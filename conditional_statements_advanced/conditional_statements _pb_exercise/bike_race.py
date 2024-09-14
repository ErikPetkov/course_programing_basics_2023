yong_bikers = int(input())
old_bikers = int(input())
tipe_rase = input()
juniors = 0
seniors = 0
discount = 1
if tipe_rase == "trail":
    juniors = 5.5
    seniors = 7
elif tipe_rase == "cross-country":
    juniors = 8
    seniors = 9.5
    if yong_bikers+old_bikers >= 50:
        juniors *= 0.75
        seniors *= 0.75
elif tipe_rase == "downhill":
    juniors = 12.25
    seniors = 13.75
elif tipe_rase == "road":
    juniors = 20
    seniors = 21.5
yong = yong_bikers * juniors
old = old_bikers * seniors
total_sum = yong + old
total_sum *= 0.95
print(f"{total_sum:.2f}")
