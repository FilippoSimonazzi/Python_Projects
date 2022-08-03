import re
from datetime import datetime
from dateutil import parser

#_start = '2022-07-06 16:02:54'
#_end = '2022-07-06 16:03:00'

print('# I will compute how many times you have clicked!\n# Tell me which period you want me to analyze.')

full_history = input('# Do you want the statistics since you started recording? ([y]/n): ')
while full_history not in ['Yes', 'Y', 'y', 'yes', 'No', 'no', 'n']:
    print('# I could not understand your input.')
    full_history = input('# Do you want the statistics since you started recording? ([y]/n): ')
full_history = True if full_history in ['Yes', 'Y', 'y'] else False
    
if not full_history:
    print('# First, enter which the initial day. Then, if required, enter the final day of the requested period.')
    dt_start = parser.parse(input('# Enter initial date: '), dayfirst=True)
    same_date = input(f'# Do you want the statistics only for this day? ([y]/n): ')

    while same_date not in ['Yes', 'Y', 'y', 'yes', 'No', 'no', 'n']:
        print('I could not understand your input.')
        same_date = input(f'# Do you want the statistics only for this day? ([y]/n): ')
    if same_date in ['Yes', 'Y', 'y']:
        dt_end = dt_start.replace(hour=23, minute=59, second=59)
    else:
        parser.parse(input('# Enter final date:'), dayfirst=True)
else:
    with open('log_mouse.txt', 'r') as f:
        lines = f.readlines()
        dt_start = parser.parse(lines[0].strip().split(' ')[0])
        dt_end = parser.parse(lines[-1].strip().split(' ')[0])
        dt_end = dt_end.replace(hour=23, minute=59, second=59)

dt_fmt = '%Y-%m-%d %H:%M:%S'
dt_reg = r'\d{4}-\d{2}-\d{2}'

str_time_len = len(str(dt_start))
clicks_dict = {'left': 0, 'right': 0}

with open('log_mouse.txt', 'r') as f:
    started = False
    for line in f:
        if re.match(dt_reg, line):
            datetime_str = line[:str_time_len]
            dt = datetime.strptime(datetime_str, dt_fmt)
            if not started and dt >= dt_start and dt < dt_end:
                started = True
            elif started and dt > dt_end:
                break
        
        if not started:
            continue
        
        button = line.strip().split(' ')[-1].split('.')[-1]
        clicks_dict[button] += 1

if full_history:
    print(f'\n ------------------------------------------ \n Analyzed from {dt_start.strftime("%d-%m-%Y")} to {dt_end.strftime("%d-%m-%Y")}. \n \n Left clicks: {clicks_dict["left"]}.\n\n Right clicks: {clicks_dict["right"]}.\n ------------------------------------------ \n')
else:
    print(f'\n ------------------------------------------ \n Analyzed only {dt_start.strftime("%d-%m-%Y")}. \n \nLeft clicks: {clicks_dict["left"]}.\n\n Right clicks: {clicks_dict["right"]}.\n ------------------------------------------ \n')
