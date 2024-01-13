def callLimit(limit: int):
    """
    A decorator factory for creating a call-limited version of a function.

    This function takes an integer 'limit' and returns a decorator. The decorator can be
    applied to any function to restrict its number of calls to the specified limit. If the
    decorated function is called more than 'limit' times, it will print an error message and
    not execute the function.

    Args:
    - limit (int): The maximum number of allowed calls to the decorated function.

    Returns:
    - function: A decorator that limits the number of calls to the function it decorates.

    Example:
        @callLimit(2)
        def test_func():
            print("Function called")

        test_func()  # Will work
        test_func()  # Will work
        test_func()  # Will print "Function call limit exceeded" and not call the function
    """
    def callLimiter(function):
        """
        A decorator that limits the number of calls to the function it decorates.

        This function is an internal decorator used by the 'callLimit' decorator factory. It wraps
        around a given function and limits its calls as per the 'limit' specified in 'callLimit'.

        Args:
        - function (callable): The function to be decorated and call-limited.

        Returns:
        - function: A wrapper function that enforces the call limit.
        """
        count = 0  # Using a list to hold the count so it can be modified
        def limit_function(*args, **kwds):
            """
            A wrapper function that enforces the call limit on the decorated function.
        
            This internal function checks if the number of calls to the decorated function is within
            the allowed limit. If so, it calls and returns the result of the decorated function. If the
            limit is exceeded, it prints an error message.
        
            Args:
            - *args: Variable length argument list for the decorated function.
            - **kwds: Arbitrary keyword arguments for the decorated function.
        
            Returns:
            - The result of the decorated function if within the call limit; otherwise, None.
            """
            try:
                nonlocal count
                count += 1
                if (count < limit):
                    return function(*args, **kwds)
                raise AssertionError("Function call limit exceeded")
            except AssertionError as msg:
                print(msg)
        return limit_function

    return callLimiter