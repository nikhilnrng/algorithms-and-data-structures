def binary_strings(alen):
    """Count all possible binary strings of length N such that there are no consecutive 1's

    This algorithm is a solution to the problem described on the IDeserve link: 
    http://www.ideserve.co.in/learn/distinct-binary-strings-of-length-n-with-no-consecutive-1s.

    Given a string {a_1 ... a_i}, we observe two cases. If a_i is 0, a 0 or 1 can be appended.
    If a_i is 1, only a 0 can be appended to prevent consecutive 1's. Thus, the number of
    binary strings of length i ending in 0 is the sum of the a_(i - 1) ending in 0 and 1. The
    number of binary strings of length i ending in 1 is a_(i - 1) ending in 0. 

    Time Complexity:

    O(n)

    Space Complexity:

    O(1)
    """

    OPT_A = [1] * 2
    OPT_B = [1] * 2

    for i in range(1, alen):
        curr = i % 2
        prev = (i - 1) % 2
        OPT_A[curr], OPT_B[curr] = OPT_A[prev] + OPT_B[prev], OPT_A[prev]

    return OPT_A[(alen - 1) % 2] + OPT_B[(alen - 1) % 2]
