def max_subarray_sum(alist):
    """Maximum subarray sum.

    Given an array of unordered positive and negative integers, find the maximum subarray
    sum in the array.

    This algorithm uses a dynamic programming solution that continuously builds up 
    maximal sums for subarrays as long as those sums are greater than or equal to zero. 
    The algorithm walks through the array and tracks a running sum, updating a max 
    variable when a max is found. If the sum is negative, the sum is reset and a running
    sum is recalculated. 

    This algorithm uses a dynamic programming solution that computes the maximum sum for
    the subarray {a1 ... ai}, where i <= n. As long as at least one non-negative value
    exists in the array, then a subarray ending in ai with a sum less than zero is not
    the maximum subarray. Thus, anytime a negative sum is computed, the running sum
    restarts, and any time a max sum is found, a max variable is updated with that sum. 
    In the case of an all-negative array, the maximum value of the array makes up the 
    maximum subarray sum, because the addition of any other negative values will always
    produce a lower value. 

    Time Complexity:

    O(n). The solution loops through the array one time.

    Space Complexity:

    O(1). The computation can be done with constant memory.
    """

    n = len(alist)
    curr = 0
    max_sum = 0
    is_neg = True

    for i in range(1, n + 1):

        if alist[i - 1] + curr >= 0:
            curr += alist[i - 1]
            is_neg = False

            if curr > max_sum:
                max_sum = curr

        else:
            curr = 0

    return max(alist) if is_neg else max_sum
