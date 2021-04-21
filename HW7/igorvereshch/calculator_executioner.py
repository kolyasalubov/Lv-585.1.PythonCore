import calculator

def execute(first_number: float, second_number: float, operator: str)->float:
    '''
    Returns result of operation between two numbers

    Parameters
    ----------
    first_number: first argument of operation\n
    second_number: second argument of operation\n
    operator: defines operation

    Returns
    -------
    result of operation
    '''

    if operator == '+':
        return calculator.add(first_number, second_number)
    elif operator == '-':
        return calculator.subtract(first_number, second_number)
    elif operator == '*':
        return calculator.multiply(first_number, second_number)
    elif operator == '/':
        return calculator.divide(first_number, second_number)
    else:
        return "Вибачте, дані введено неправильно"

operator = input("Введіть бажану для виконання операцію: '+', '-', '*' або '/': ")
first_number = float(input("Введіть перше число: "))
second_number = float(input("Введіть друге число: "))
result = execute(first_number, second_number, operator)
print(f"{first_number} {operator} {second_number} = {result}")
