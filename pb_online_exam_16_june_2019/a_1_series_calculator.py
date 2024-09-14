serial_name = input()
br_seasons = int(input())
br_episode = int(input())
time_for_ep = int(input())
ep_with_adds = time_for_ep * 1.2
season_ep = br_seasons * 10
total_ep = ep_with_adds * br_episode
total_sesonses = total_ep * br_seasons + season_ep
print(f"Total time needed to watch the {serial_name} series is {int(total_sesonses)} minutes.")

