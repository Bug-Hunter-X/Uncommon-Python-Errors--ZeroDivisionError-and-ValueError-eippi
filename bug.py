def function_with_uncommon_error(x, y):
    if x == 0:
        return 1 / x  # ZeroDivisionError
    elif y < 0:
        raise ValueError("y must be non-negative")
    else:
        return x + y