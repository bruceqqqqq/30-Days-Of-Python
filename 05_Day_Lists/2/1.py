ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(max(ages)) # or ages[-1]
print(min(ages)) # or ages[0]
ages.append(max(ages))
ages.append(min(ages))
print(ages)
median = ((ages[len(ages)//2] + ages[len(ages)//2 - 1]) / 2)
print(median)
average = sum(ages) / len(ages)
print(average)
range = max(ages) - min(ages)
print(range)
compare = abs(min(ages) - average), abs(max(ages) - average)
print(compare)