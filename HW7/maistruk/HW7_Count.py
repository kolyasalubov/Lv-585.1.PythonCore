def count_positives_sum_negatives(arr):
    count_positive_num = 0
    sum_negatives = 0
    if len (arr) == 0:
        return 0
    for number in arr:
        if number > 0:
            count_positive_num +=1
        elif number < 0:
            sum_negatives += number
    return [count_positive_num, sum_negatives]


print(count_positives_sum_negatives([2, -3, 4, -6]))