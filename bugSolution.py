def function_with_uncommon_error(x, y):
    try:
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        elif y < 0:
            raise ValueError("y must be non-negative")
        else:
            return x + y
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None  # Or handle the error appropriately
    except ValueError as e:
        print(f"Error: {e}")
        return None  # Or handle the error appropriately