from utils import read_file, timer
from collections import defaultdict


def analyse_schedule(schedule):
    calender = {}
    guard_days = defaultdict(list)

    for line in sorted(schedule):
        if "Guard" in line:
            guard = line.split()[3]
            continue
            
        if "asleep" in line:
            day = line[6:11]
            if day not in calender:
                calender[day] = [0] * 60
                guard_days[guard].append(day)
            sleep_start = int(line.split()[1][3:5])
            continue
    
        if "wakes" in line:
            sleep_end = int(line.split()[1][3:5])
            for i in range(sleep_start, sleep_end):
                calender[day][i] = 1
    
    return calender, guard_days


@timer
def solve():
    input = read_file('04')
    calender, guard_days = analyse_schedule(input)
    
    guard_hours = {}
    for guard, days in guard_days.items():
        guard_hours[guard] = sum(sum(calender[day]) for day in days)

    max_hours = 0

    for guard, hours in guard_hours.items():
        if hours > max_hours:
            max_hours = hours
            sleepiest_guard = guard
    
    minutes = [0] * 60

    for day in guard_days[sleepiest_guard]:
        for i in range(60):
            if calender[day][i]:
                minutes[i] += 1
    
    return minutes.index(max(minutes)) * int(sleepiest_guard[1:])


result = solve()
print(f'Solution: {result}')