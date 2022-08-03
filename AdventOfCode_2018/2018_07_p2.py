from utils import read_file, timer
from collections import defaultdict

@timer
def solve():
    input     = read_file("07")
    built     = []
    workers   = []
    steps     = defaultdict(list)
    all_steps = set()
    timer     = 0

    for line in input:
        first = line.split(" ")[1]
        after = line.split(" ")[7]
        steps[after].append(first)
        all_steps.update(first, after)

    all_steps = sorted(list(all_steps))
    amount_of_steps = len(all_steps)
    
    while len(built) < amount_of_steps:
        if len(workers) < 5:
            for after in all_steps:
                if all(first_steps in built for first_steps in steps[after]):
                    workers.append({"step": after, "duration": ord(after) - 4})
                    all_steps.remove(after)

        worker_id = 0
        while worker_id < len(workers):
            if workers[worker_id]["duration"] > 1:
                workers[worker_id]["duration"] -= 1
                worker_id += 1
            else:
                built.append(workers[worker_id]["step"])
                del workers[worker_id]

        timer += 1
    return timer
    
result = solve()
print(f"Solution: {result}")