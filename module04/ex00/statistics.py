import math

def find_quartile(data, percentile):
    """a function that calculates the quartile"""
    size = len(data)
    if size == 0:
        return None
    sorted_data = sorted(data)
    k = (size - 1) * (percentile / 100.0)
    f = int(k)
    if f == k:
        return sorted_data[f]
    return sorted_data[f] + (sorted_data[f + 1] - sorted_data[f]) * (k - f)


def ft_statistics(*args: any, **kwargs: any) -> None:
    """a function that calculate statistic value if asked"""
    mean = sum(int(i) for i in args) / len(args)
    values = kwargs.values()
    if ('mean' in values):
        print("mean: ",mean)
    if ('median' in values):
        if (len(args) % 2== 1):
            print("median: ",sorted(args)[len(args) // 2])
        else:
            print("median: ",sum(int(i) for i in args) / 2)
    if ('quartile' in values):
        k = sorted(args)
        print("quartile: ",[find_quartile(k,25) , find_quartile(k,75)])
    if ('std' in values):
        std = sum((int(i) - mean)**2 for i in args)
        print("std :",math.sqrt(std/len(args)))
    if ("var" in values):
        var = sum((int(i) - mean)**2 for i in args)
        print("var: ",var/len(args))