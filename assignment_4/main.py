from scheduling import BaseScheduling, SJF_Scheduling, Priority_Scheduling, RR_Scheduling


def common_input():
    no_of_process = input("Enter total number of processes: ")
    arrival_time = input("Enter arrival times (space separated): ").split()
    burst_time = input("Enter burst times (space separated): ").split()

    return no_of_process, arrival_time, burst_time


def print_output(schedule: BaseScheduling) -> None:
    completion_time = [time for _, time in schedule.get_completion_time()]
    turnaround_time = schedule.get_turnaround_time()
    waiting_time = schedule.get_waiting_time()
    average_turnaround_time = schedule.get_average_turnaround_time()
    average_waiting_time = schedule.get_average_waiting_time()

    print(f"Completion time         : {completion_time}")
    print(f"Turnaround time         : {turnaround_time}")
    print(f"Waiting time            : {waiting_time}")
    print(f"Average turnaround time : {average_turnaround_time}")
    print(f"Average waiting time    : {average_waiting_time}")


def main():
    # ~~~~~ TEST VALUES : SJF_Scheduling ~~~~~ #
    print("~~~~~ SJF_Scheduling ~~~~~")
    no_of_process, arrival_time_1, burst_time_1 = common_input()

    process_sjf = SJF_Scheduling(no_of_process, arrival_time_1, burst_time_1)
    process_sjf.start()
    print_output(process_sjf)

    # ~~~~~ TEST VALUES : Priority_Scheduling ~~~~~ #
    print("\n~~~~~ Priority_Scheduling ~~~~~")
    no_of_process, arrival_time_2, burst_time_2 = common_input()
    priorities = input("Enter priority values (space separated): ").split()

    process_priority = Priority_Scheduling(
        no_of_process, arrival_time_2, burst_time_2, priorities)
    process_priority.start()
    print_output(process_priority)

    # ~~~~~ TEST VALUES : Round_Robin ~~~~~ #
    print("\n~~~~~ Round_Robin ~~~~~")
    no_of_process, arrival_time_3, burst_time_3 = common_input()
    time_quantum = input("Enter time quantum value: ")

    process_rr = RR_Scheduling(
        no_of_process, arrival_time_3, burst_time_3, time_quantum)
    process_rr.start()
    print_output(process_rr)


if __name__ == "__main__":
    main()
