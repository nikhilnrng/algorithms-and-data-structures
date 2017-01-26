def max_as(num):
    """Find the maximum number of A's using four keys

    This algorithm is a solution to the max A's problem described on the IDeserve link: 
    http://www.ideserve.co.in/learn/how-to-print-maximum-number-of-a-using-given-four-keys.

    The solution to this relies on the fact that the maximum number of A's that can be
    written follows a pattern of printing some number of A's, selecting the printed A's,
    copying the A's, and then repeatedly pasting the copy buffer. Additionally, another
    critical point is that for keystrokes of 6 or less, the number of A's that can be
    written is equal to the number of available keystrokes. 

    For i keystrokes, where i is greater than 6, the maximum number of A's is given by
    MAX(2 * OPT[i - 3], 3 * OPT[i - 4], ... , (i - 2) * OPT[1]). To understand this 
    clearly, we'll look at the first and last terms of this equation: 

    2 * OPT[i - 3] -> If we begin the CTRL-A, CTRL-C, CTRL-V process at the last 
                      possible moment, we copy OPT[i - 3] one time. 
    (i - 2) * OPT[1] -> If we begin the CTRL-A, CTRL-C, CTRL-V process at the earliest
                        possible moment, we copy OPT[1] (i - 2) times, since we have
                        to account for the CTRL-A and CTRL-C keystrokes.

    Time Complexity:

    O(n^2). For all n values, we trace back from {1 ... (n - 3)} to find the breaking
    point at which we start the copy and paste process.

    Space Complexity:

    O(n). This algorithm uses an n-sized list to store the optimal value of A's that
    can be achieved for all values {1 ... n}.
    """

    if num <= 6:
        return num

    OPT = [0] * (num)

    for i in range(6):
        OPT[i] = i + 1 # store {1 ... 6}

    for i in range(6, num):
        OPT[i] = i + 1 # press 'A' i times
        for j in range(i - 3, -1, -1):
            temp = (i - j - 1) * OPT[j] # test all breakpoints
            if temp > OPT[i]:
                OPT[i] = temp # update OPT if temp is greater than current value

    return OPT[num - 1]
