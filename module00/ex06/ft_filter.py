
def ft_filter(func, seq):
    """Yields all values from the iterable
    for which the function returns a truthful value"""
    return [item for item in seq if func(item)]
