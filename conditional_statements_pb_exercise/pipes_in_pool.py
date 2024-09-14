v_in_pool_liters = int(input())
p1_debit_on_first_pipe_per_hour = int(input())
p2_debit_on_first_pipe_per_hour = int(input())
n_hours_worker_misses = float(input())

pipes_per_hour = p1_debit_on_first_pipe_per_hour+p2_debit_on_first_pipe_per_hour
pool_water = pipes_per_hour*n_hours_worker_misses
pool_water_percent = (pool_water/v_in_pool_liters*100)
p1_persent = p1_debit_on_first_pipe_per_hour * n_hours_worker_misses/pool_water*100
p2_persent = p2_debit_on_first_pipe_per_hour * n_hours_worker_misses/pool_water*100

if pool_water <= v_in_pool_liters:
    print(f"The pool is {pool_water_percent:.2f}% full. Pipe 1:"
          f" {p1_persent}%. Pipe 2: {p2_persent:.2f}%.")
else:
    print(f"For {n_hours_worker_misses:.2f} hours "
          f"the pool overflows with {pool_water-v_in_pool_liters:.2f} liters.")
