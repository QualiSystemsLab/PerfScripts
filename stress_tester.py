from Agents.BenchmarkAgent import BenchmarkAgent
import this
from executor import main

NUMBER_OF_BUILDS_MULTIPLE_EXECUTIONS = [10, 15, 30, 50, 100]

# create reservation, then have a loop that checks if status has changed every two seconds
for itera in NUMBER_OF_BUILDS_MULTIPLE_EXECUTIONS:
     reserve_benchmark_flow = {BenchmarkAgent: 5000}
     main(reserve_benchmark_flow,
          number_of_action_groups=1, number_of_actions_per_group=itera, sleep_between_groups=0,
          main_loop_iterations=5)