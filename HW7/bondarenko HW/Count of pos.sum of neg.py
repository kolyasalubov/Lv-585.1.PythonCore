def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    count_of_pos = 0
    sum_of_neg = 0
    for i in arr:
        if i > 0:
           count_of_pos += 1
        elif i < 0:
            sum_of_neg += i
    return [count_of_pos, sum_of_neg]

count_positives_sum_negatives([1,2,-3,4,-5,6,7,8,-9,10,11,12,-13])