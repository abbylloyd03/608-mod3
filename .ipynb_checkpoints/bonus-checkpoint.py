# Abby Lloyd, bonus.py
import random
import statistics

for number in range(251):
    list = random.randrange(1, 101)
    
std = statistics.pstdev(list)
variance = statistics.pvariance(list)

print("The standard deviation of the generated list is ", std)
print("The variance of the generated list is ", variance)
