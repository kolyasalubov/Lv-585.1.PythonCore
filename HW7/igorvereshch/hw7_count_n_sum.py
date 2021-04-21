def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    count = 0
    sum_ = 0
    for i in arr:
        if i > 0:
            count += 1
        elif i < 0:
            sum_ += i
    return [count, sum_]

count_positives_sum_negatives([1,2,-3,4,-5,6,7,8,-9,10,11,12,-13])