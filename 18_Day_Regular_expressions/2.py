import re

points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
print(f'points = {points}')
points = [int(n) for n in points]
sorted_points = sorted(points)
print(f'sorted_points = {sorted_points}')
difference = max(sorted_points) - min(sorted_points)
print(f'distance = {difference}')
