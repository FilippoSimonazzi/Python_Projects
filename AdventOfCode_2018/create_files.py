import os

n_days = 25
for day in range(6, n_days + 1):
    # create input file
    f = open(f'./files/input{str(day).zfill(2)}', mode='a').close()
    
    # create task one file
    with open(f'2018_{str(day).zfill(2)}_p1.py', 'w') as f:
        f.write('from utils import read_file, timer')
        f.write('\n\n')
        f.write(f'@timer\ndef solve():\n    input = read_file("{str(day).zfill(2)}")\n    pass')
        f.write('\n\n')
        f.write(f'result = solve()\n')
        f.write(f"print(f'Solution: ')")
    
    # create task two file
    with open(f'2018_{str(day).zfill(2)}_p2.py', 'w') as f:
        f.write('from utils import read_file, timer')
        f.write('\n\n')
        f.write('@timer\ndef solve():\n    pass')
        f.write('\n\n')
        f.write(f'result = solve()\n')
        f.write(f"print(f'Solution: ')")
