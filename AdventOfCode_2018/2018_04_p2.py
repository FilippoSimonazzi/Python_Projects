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

    sleep_per_minute = {}
    for guard, days in guard_days.items():
        if guard not in sleep_per_minute:
            sleep_per_minute[guard] = [0] * 60
        
        for day in days:
            for minute in range(60):
                if calender[day][minute]:
                    sleep_per_minute[guard][minute] += 1
    
    max_minute = 0
    for guard, minutes in sleep_per_minute.items():
        if max(minutes) > max_minute:
            max_guard  = guard
            max_minute = max(minutes)
            max_index  = minutes.index(max_minute)
    
    return max_index * int(max_guard[1:])


result = solve()
print(f'Solution: {result}')