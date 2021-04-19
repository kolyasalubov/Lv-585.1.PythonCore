def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    count = 0
    sum_neg = 0
    for i in arr:
        if i > 0:
            count += 1
        elif i < 0:
            sum_neg += i
    return [count, sum_neg]
print(count_positives_sum_negatives([1, -2, 4, -1]))