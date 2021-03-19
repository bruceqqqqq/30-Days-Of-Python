def calculated_mean(*nums):
    tot = sum(nums)
    mean = tot / len(nums)
    return mean

print(calculated_mean(6, 11, 7))

def calculated_median(nums):
    nums.sort()
    if len(nums) % 2 != 0:
        median = nums[len(nums)//2]
        print('Median:', median)
    else:
        median = (nums[len(nums)//2] + nums[len(nums)//2-1]) / 2
        print('Median:', median)

calculated_median([3, 3, 6, 7, 8, 9, 1])
calculated_median([9, 8, 6, 5, 4, 3, 2, 1])

def calculated_mode(nums):
    most = 0
    for i in nums:
        if nums.count(i) > most:
            most = nums.count(i)
            modeCalc = i
    return modeCalc

print(calculated_mode([1, 1, 3, 3, 3, 4, 4, 6, 6, 9, 9]))

def calculated_range(lst: list):
    maior = max(lst)
    menor = min(lst)
    rangeC = maior - menor
    return rangeC

print(calculated_range([4, 6, 9, 3, 7]))


def calculated_variance(lst: list):
    mean = sum(lst) / len(lst)
    diff = []
    for i in lst:
        r = (i - mean) ** 2
        diff.append(r)
    variance = (sum(diff) / len(diff))
    return int(variance)

print(calculated_variance([600, 470, 170, 430, 300]))

def calculated_desvio(lst: list):
    mean = sum(lst) / len(lst)
    diff = []
    for i in lst:
        r = (i - mean) ** 2
        diff.append(r)
    variance = (sum(diff) / len(diff))
    std = variance ** 0.5
    return int(std)

print(calculated_desvio([600, 470, 170, 430, 300]))
