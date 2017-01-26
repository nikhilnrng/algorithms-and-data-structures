def max_as(num):
    """Find the maximum number of A's using four keys

    This algorithm is a solution to the max A's problem described on the IDeserve link: 
    http://www.ideserve.co.in/learn/how-to-print-maximum-number-of-a-using-given-four-keys.

    This solution uses dynamic programming to find the number of A's that can be
    produced in n keystrokes. There are four possible keystrokes: (1) Print 'A', (2) Select
    ALL, (3) Copy, (4) Paste. From these four keystrokes, we can derive three possible
    cases that can occur on the ith keystroke: (1) print an 'A', (2) Copy and paste 'A's, 
    or (3) Paste 'A's. The third case requires the storage of the number of 'A's from the
    most recent copy throughout the algorithm. 

    Time Complexity:

    O(n). Requires traversal of all n values {1 ... n}.

    Space Complexity:

    O(1). This algorithm can be achieved in a fixed-sized list of four elements.
    """

    OPT = [0] * 4
    OPT[0] = 1
    OPT[1] = 2
    OPT[2] = 3
    prev = 0

    for i in range(3, num):
        max_val = max(1 + OPT[(i - 1) % 4], 
                      2 * OPT[(i - 3) % 4], 
                      prev + OPT[(i - 1) % 4])

        if max_val == 2 * OPT[(i - 3) % 4]:
            prev = OPT[(i - 3) % 4]
        OPT[i % 4] = max_val

    return OPT[(num - 1) % 4]
