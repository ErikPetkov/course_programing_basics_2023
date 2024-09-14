wanted_jump = int(input())
done = False
jumps = 0
jump_now = wanted_jump - 30
while not done:
    fails = 0
    while fails < 3:
        jumps += 1
        his_jump = int(input())
        if his_jump > jump_now:
            jump_now += 5
            fails = 0
            if jump_now >= wanted_jump:
                done = True
                jumps += 1
                break
        else:
            fails += 1
            if fails == 3:
                break
    if fails == 3 or done:
        break

if not done:
    print(f"Tihomir failed at {jump_now}cm after {jumps} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {jump_now}cm after {jumps} jumps.")
