def count_positives_sum_negatives(arr):
    """
    This function returns an array, where the first element 
    is the count of positives numbers and the second element 
    is sum of negative numbers.
    """

    count_of_pos_numb = 0
    sum_of_neg_numb = 0
    if len(arr) == 0:
        return []
    for number in arr:
        if number > 0:
            count_of_pos_numb += 1
        elif number < 0:
            sum_of_neg_numb += number
    return [count_of_pos_numb, sum_of_neg_numb]
