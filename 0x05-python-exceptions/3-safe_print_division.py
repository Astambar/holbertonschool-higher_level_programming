#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        return result
    finally:
        print(f"Inside result: {result}")
    return result
