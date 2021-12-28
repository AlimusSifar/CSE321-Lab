import numpy as np


def bankers_algorithm(data):
    process_no = data["process_no"]
    available_resource = data["available_resource"]
    needed_resource = data["needed_resource"]
    resource_is_complete = [False] * process_no
    safe_sequence: list[str] = []
    changed_list = []

    idx = 0
    while False in resource_is_complete:
        idx %= process_no

        if not resource_is_complete[idx]:

            ready = np.all(available_resource >= needed_resource[idx])
            if ready:
                resource_is_complete[idx] = True
                safe_sequence.append(data["process_names"][idx])
                available_resource += data["allocated_resource"][idx]
                changed_list.append(list(available_resource))

        idx += 1

    return safe_sequence, np.array(changed_list)


def read_file():
    data = {}
    with open("input.txt", "r", encoding="utf-8") as file:
        data["process_no"] = int(file.readline())
        data["resource_no"] = int(file.readline())

        data["process_names"] = [chr(i + 65) for i in range(data["process_no"])]
        data["max_resource"] = np.array(
            [file.readline().split() for _ in range(data["process_no"])], dtype=np.int32
        )
        data["allocated_resource"] = np.array(
            [file.readline().split() for _ in range(data["process_no"])], dtype=np.int32
        )
        data["available_resource"] = np.array(file.readline().split(), dtype=np.int32)

    return data


def format_matrix(data) -> str:
    return "\n".join([" ".join(map(str, row)) for row in data])


# *** # MAIN STARTS HERE # *** #
data = read_file()

data["needed_resource"] = data["max_resource"] - data["allocated_resource"]
safe_sequence, changed_list = bankers_algorithm(data)


print(f">>> Need Matrix :\n{format_matrix(data['needed_resource'])}")
print(f">>> Safe sequence is :\n{' '.join(safe_sequence)}")
print(f">>> Change in available resource matrix :\n{format_matrix(changed_list)}")
