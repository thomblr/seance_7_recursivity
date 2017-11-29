def factorial(n):
    """Returns the factorial n!
    Parameters
    ----------
    n: strictly positive integer (int)

    Returns
    -------
    f: factorial of n (int)
    """

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))
