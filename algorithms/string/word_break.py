def word_break(adict, astr):
    """Check whether a string can be broken into words from a dictionary

    This algorithm is a solution to the word break problem described on the IDeserve link: 
    http://www.ideserve.co.in/learn/word-break-problem.

    The solution is a dynamic programming approach, which is achieved by walking through
    the string and checking all string subsets to see whether the current string can be
    broken into valid words. The solution for every string size is stored into the OPT
    array, so if a subset of a string forms a valid word, the validity of the remaining
    portion of the string can be checked in O(1). 

    Time Complexity: 

    O(n^2). For every portion of the string, we check all possible substrings until
    either a valid string can be formed or no valid string can be formed. 

    Space Complexity: 

    O(n). This algorithm uses a list for memoization. The size of the list is the
    size of the input string, resulting in O(n) memory usage. 
    """

    adict = set(adict)
    OPT = [True]

    for i in range(1, len(astr) + 1):
        valid = False
        j = i - 1

        while valid == False and j >= 0:
            if astr[j:i] in adict and OPT[j] == True:
                valid = True
            j -= 1

        OPT.append(valid)

    return OPT.pop()
