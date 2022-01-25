# Abby Lloyd, bonus.py
import random
import statistics

list = []
for x in range(101):
    random_number = random.randrange(1, 101)
    list.append(random_number)
    
results_std = statistics.pstdev(list)
results_variance = statistics.pvariance(list)

print("Random numbers: ", list)
print("The standard deviation of the generated list is ", results_std)
print("The variance of the generated list is ", results_variance)

