# Abby Lloyd population-dispersion.py

import statistics

die_rolls = [1, 3, 4, 2, 6, 5, 3, 4, 5, 2]

print('population variance:', statistics.pvariance(die_rolls))
print('population std:', statistics.pstdev(die_rolls))