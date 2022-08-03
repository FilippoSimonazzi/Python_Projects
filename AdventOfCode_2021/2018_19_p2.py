from utils import read_file, timer
import numpy as np
from scipy.spatial import distance

def coords_to_dist_map(scan_coords):
    dist_map = distance.cdist(scan_coords, scan_coords, metric='euclidean')
    return dist_map

def process(data):
    raw_scans = data.split('\n\n')
    scans, scans_distance_map = [], []
    scan_positions = {0: (0, 0, 0)}
    for scan in raw_scans:
        scan_coords = np.array([[int(x) for x in coord.split(',')] for coord in scan.splitlines()[1:]])
        scans.append(scan_coords)
        dist_map = coords_to_dist_map(scan_coords)
        scans_distance_map.append(dist_map)

    beacons = scans[0]
    while len(scan_positions) < len(scans):
        for i in scan_positions.keys():
            for j in list(set(list(range(len(scans))))) - set(scan_positions.keys()):
                m1, m2 = scans_distance_map[i], scans_distance_map[j]
                match, m1_points, m2_points = match_scan_distance(m1, m2)

@timer
def solve():
    with open('files/input19', 'r') as f:
        data = f.read()
    data = process(data)
result = solve()
print(f'Solution: ')