def search_sorted_list(key, alist):
    """Search a sorted list using binary search

    This algorithm is based off the IDeserve problem: 
    http://www.ideserve.co.in/learn/binary-search-in-a-sorted-array.

    The algorithm runs a binary search on the list until either the search key is found or
    the search returns an inconclusive value. 

    Time Complexity:

    O(log(n))

    Space Complexity:

    O(1)
    """

    start = 0
    end = len(alist) - 1

    while start <= end:
        mid = (start + end) / 2

        if alist[mid] == key:
            return mid
        elif alist[mid] > key:
            end = mid - 1
        else:
            start = mid + 1

    return -1
