def count_positives_sum_negatives(arr):
    return [len(list(filter((lambda x: x > 0), arr))), sum(x for x in arr if x < 0)] if len(arr) > 0 else []
