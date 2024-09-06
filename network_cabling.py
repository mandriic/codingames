import sys
import math
MAX = 1073741824
def prDebug(lst):
    for ii in lst:
        print(ii, file=sys.stderr)
def min_fiber_length(buildings):
    n = len(buildings)
    # Step 1: Find the horizontal distance (difference between max and min x-coordinates)
    x_coords = [b[1] for b in buildings]
    horizontal_distance = max(x_coords) - min(x_coords)
    y_coords = sorted([b[0] for b in buildings])
    if n % 2 == 1:
        median_y = y_coords[n // 2]
    else:
        median_y = ((y_coords[(n // 2) - 1] + y_coords[round(n // 2)]) // 2)
    vertical_distance = sum(abs(b[0] - median_y) for b in buildings)
    total_length = horizontal_distance + vertical_distance
    return(total_length)
n = int(input())
map = []
Dbgmap = [[2,1],[0,0],[2,2],[3,5]]
maxdis = 0
mapsize = 10
for i in range(n):
    x, y = [int(j) for j in input().split()]
    map.append([y,x])
print(min_fiber_length(map))
