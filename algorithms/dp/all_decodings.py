def all_decodings(astr):
    """Count all possible decodings of a given digit sequence

    If there exists an encoding scheme where integer 1 encodes to 'A', 2 to 'B', ... , 26
    to 'Z', write a program to count all possible decodings of a given digit sequence. 

    This solution uses dynamic programming to compute the possible decodings. The 
    solution observes two cases for the integer substring astr{1 ... i}: 

    (1) The two digit number ending in astr{i} corresponds to a valid encoding.
    (2) The two digit number ending in astr{i} does not correspond to a valid encoding.

    In both cases, we add the number of possible decodings from the previous decodings, 
    since the single digit can extend every previous decoding. However, if the first case
    is true, then we also must add the number of encodings for the astr{1 ... i - 2} case
    as well. This results in the following recurrence relation: 

    OPT[i] = OPT[i - 1] + {OPT[i - 2] if astr[i - 2:i] is between 10 and 26}

    Time Complexity:

    O(n). The number of loops is given by n, the length of the substring.

    Space Complexity:

    O(1). The solution can be performed in constant time since at most, the previous two 
    values are necessary to obtain the next solution.
    """

    n = len(astr)

    if n <= 1:
        return n

    OPT = [1] * 3

    for i in range(2, n + 1):
        OPT[i % 3] = OPT[(i - 1) % 3]
        if 10 <= int(astr[i - 2:i]) <= 26:
            OPT[i % 3] += OPT[(i - 2) % 3]

    return OPT[n % 3]
