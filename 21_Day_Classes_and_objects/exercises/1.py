class Statistics:
    def __init__(self, lst):
        self.ages = []
        for n in lst:
            self.ages.append(n)

    def add_list(self, data):
        self.ages.append(data)

    def count(self):
        return len(self.ages)

    def sum(self):
        return sum(ages)

    def max(self):
        return max(ages)

    def min(self):
        return min(ages)

    def range(self):
        return data.max() - data.min()

    def mean(self):
        return data.sum() / data.count()

    def median(self):
        self.ages = sorted(self.ages)
        return self.ages[len(self.ages)//2]

    def mode(self):
        mode = 0
        modedict = {}
        for n in self.ages:
            if self.ages.count(n) > mode:
                mode = self.ages.count(n)
                modedict['mode'] = n
                modedict['count'] = self.ages.count(n)
        return modedict

    def std(self):
        median = data.mean()
        tot = 0
        for n in self.ages:
            s = (n - median) ** 2
            tot += s
        stdr = (tot / len(self.ages)) ** 0.5
        return f'{stdr:.1f}'

    def variance(self):
        each = 0
        media = data.mean()
        for n in self.ages:
            each += (n - media) ** 2
        var = each / len(self.ages)
        return f'{var:.1f}'

    def frequency_distributions(self):
        d = {}
        for n in self.ages:
            if d.get(n):
                d[n] += 1
            else:
                d[n] = 1
        fq = []
        for k, v in d.items():
            fq.append((v, k))
        return fq

    def describe(self):
        print('Count:', data.count())
        print('Sum:', data.sum())
        print('Max:', data.max())
        print('Min:', data.min())
        print('Range:', data.range())
        print('Mean:', data.mean())
        print('Median:', data.median())
        print('Mode:', data.mode())
        print('Standard Deviation:', data.std())
        print('Variance:', data.variance())
        print('Frequency Distribution:', data.frequency_distributions())

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
print(type(data))