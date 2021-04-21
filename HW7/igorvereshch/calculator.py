def add(first_number: float, second_number: float)->float:
    return first_number + second_number

def subtract(first_number: float, second_number: float)->float:
    return first_number - second_number

def multiply(first_number: float, second_number: float)->float:
    return first_number * second_number

def divide(first_number: float, second_number: float)->float:
    if second_number == 0:
        return float('inf')
    return first_number / second_number