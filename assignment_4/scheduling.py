from queue import PriorityQueue, Queue


def get_average(iterable):
    return sum(iterable) / len(iterable)


# Base Scheduling Class
class BaseScheduling:
    def __init__(self, no_of_process: str, arrival_times: list, burst_times: list) -> None:
        self.no_of_process = int(no_of_process)
        self.arrival_times = list(map(int, arrival_times))
        self.burst_times = list(map(int, burst_times))

        self.cpu_time = 0
        self.waiting_queue = Queue()

        self.gantt_list: dict = {}
        self.completion_time: list[tuple] = list()
        self.turnaround_time: list = list()
        self.waiting_time: list = list()

    def check_arrival(self, priorities) -> None:
        for process, (arrival_t, priority) in enumerate(zip(self.arrival_times, priorities)):
            if arrival_t == self.cpu_time:
                self.waiting_queue.put_nowait((priority, process))

    def set_turnaround_time(self) -> None:
        for (_, completion), arrival in zip(self.completion_time, self.arrival_times):
            self.turnaround_time.append(completion - arrival)

    def set_waiting_time(self) -> None:
        for tat, burst in zip(self.turnaround_time, self.burst_times):
            self.waiting_time.append(tat - burst)

    def get_completion_time(self) -> list:
        return self.completion_time

    def get_turnaround_time(self) -> list:
        return self.turnaround_time

    def get_waiting_time(self) -> list:
        return self.waiting_time

    def get_average_turnaround_time(self) -> float:
        return get_average(self.turnaround_time)

    def get_average_waiting_time(self) -> float:
        return get_average(self.waiting_time)


# Shortest Job First Scheduling
class SJF_Scheduling(BaseScheduling):
    def __init__(self, no_of_process: str, arrival_times: list, burst_times: list) -> None:
        super().__init__(no_of_process, arrival_times, burst_times)

        self.waiting_queue = PriorityQueue()

    def start(self) -> None:
        while self.no_of_process > 0:
            # initial waiting queue
            self.check_arrival(self.burst_times)

            # starting process
            while not self.waiting_queue.empty():
                process_is_complete = False
                burst_t, process = self.waiting_queue.get()
                # print(f"process {process}, burst {burst_t}")  # TEST LINE

                self.gantt_list[self.cpu_time] = f"P{process + 1}"
                # print(f"{self.gantt_list=}")  # TEST LINE

                # if current process is not complete
                while not process_is_complete:
                    self.cpu_time += 1
                    burst_t -= 1

                    # if more than 1 process is available
                    if self.no_of_process > 1:
                        self.check_arrival(self.burst_times)

                    # if current process is complete
                    if burst_t == 0:
                        process_is_complete = True
                        self.no_of_process -= 1
                        self.completion_time.append((process, self.cpu_time))
                        self.completion_time = sorted(self.completion_time)
                        continue

                    # checking the queue for new process
                    if not self.waiting_queue.empty():
                        dequed = self.waiting_queue.get()

                        # if new process has lower burst time
                        if burst_t > dequed[0]:
                            self.waiting_queue.put_nowait(
                                (burst_t, process))
                            burst_t, process = dequed
                            self.gantt_list[self.cpu_time] = f"P{process + 1}"
                            continue

                        self.waiting_queue.put_nowait(dequed)

            # if there is no process in the queue, then cpu is idle.
            if self.waiting_queue.empty():
                self.cpu_time += 1

        # print(f"{self.gantt_list=}")  # TEST LINE
        # print(f"{self.completion_time=}")  # TEST LINE

        self.set_turnaround_time()
        self.set_waiting_time()


# Priority Scheduling
class Priority_Scheduling(BaseScheduling):
    def __init__(self, no_of_process: str, arrival_times: list, burst_times: list, priorities: list) -> None:
        super().__init__(no_of_process, arrival_times, burst_times)

        self.priorities = list(map(int, priorities))
        self.waiting_queue = PriorityQueue()

    def start(self) -> None:
        while self.no_of_process > 0:
            # initial waiting queue
            self.check_arrival(self.priorities)

            # starting process
            while not self.waiting_queue.empty():
                process_is_complete = False
                priority, process = self.waiting_queue.get()
                # print(f"{priority=} {process=}")  # TEST LINE
                burst_t = self.burst_times[process]
                # print(f"{burst_t=}")  # TEST LINE

                self.gantt_list[self.cpu_time] = f"P{process + 1}"
                # print(f"{self.gantt_list=}")  # TEST LINE

                # if current process is not complete
                while not process_is_complete:
                    self.cpu_time += 1
                    burst_t -= 1

                    # if more than 1 process is available
                    if self.no_of_process > 1:
                        self.check_arrival(self.priorities)

                    # if current process is complete
                    if burst_t == 0:
                        process_is_complete = True
                        self.no_of_process -= 1
                        self.completion_time.append((process, self.cpu_time))
                        self.completion_time = sorted(self.completion_time)
                        continue

                    # checking the queue for new process
                    if not self.waiting_queue.empty():
                        dequed = self.waiting_queue.get()

                        # if new process has higher priority
                        if priority > dequed[0]:
                            self.waiting_queue.put_nowait((priority, process))
                            priority, process = dequed
                            self.gantt_list[self.cpu_time] = f"P{process + 1}"
                            continue

                        self.waiting_queue.put_nowait(dequed)

            # if there is no process in the queue, then cpu is idle.
            if self.waiting_queue.empty():
                self.cpu_time += 1

        # print(f"{self.gantt_list=}")  # TEST LINE
        # print(f"{self.completion_time=}")  # TEST LINE

        self.set_turnaround_time()
        self.set_waiting_time()


# Round Robin Scheduling
class RR_Scheduling(BaseScheduling):
    def __init__(self, no_of_process: str, arrival_times: list, burst_times: list, time_quantum: str) -> None:
        super().__init__(no_of_process, arrival_times, burst_times)
        self.TIME_QUANTUM = int(time_quantum)

    def start(self) -> None:
        while self.no_of_process > 0:
            # initial waiting queue
            self.check_arrival(self.burst_times)

            # starting process
            while not self.waiting_queue.empty():
                process_is_complete = False
                burst_t, process = self.waiting_queue.get()
                # print(f"{process=} {burst_t=}")  # TEST LINE

                self.gantt_list[self.cpu_time] = f"P{process + 1}"
                # print(f"{self.gantt_list=}")  # TEST LINE

                # use time quantum for a process
                for _ in range(self.TIME_QUANTUM):
                    self.cpu_time += 1
                    burst_t -= 1

                    # if more than 1 process is available
                    if self.no_of_process > 1:
                        self.check_arrival(self.burst_times)

                    # if current process is complete
                    if burst_t == 0:
                        process_is_complete = True
                        self.no_of_process -= 1
                        self.completion_time.append(
                            (process + 1, self.cpu_time))
                        self.completion_time = sorted(self.completion_time)
                        break

                # if current process is not complete
                if not process_is_complete:
                    self.waiting_queue.put_nowait((burst_t, process))

            # if there is no process in the queue, then cpu is idle.
            if self.waiting_queue.empty():
                self.cpu_time += 1

        # print(f"{self.gantt_list=}")  # TEST LINE
        # print(f"{self.completion_time=}")  # TEST LINE

        self.set_turnaround_time()
        self.set_waiting_time()
