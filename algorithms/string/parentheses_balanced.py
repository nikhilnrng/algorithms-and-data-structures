def parentheses_balanced(astr):
    """Check whether parentheses in a string are balanced

    This algorithm is a solution to the check balanced parentheses problem described on the
    IDeserve link: http://www.ideserve.co.in/learn/check-balanced-parentheses-in-a-string.

    This solution uses two loops that search for open brackets and then, when an open bracket
    is found, searches for a corresponding closed bracket. If the open bracket loop finds
    a closed bracket, it returns Invalid. If it passes the area searched by the closed bracket
    loop, it returns Valid, since no more open brackets are remaining. 

    On the other hand, if the closed bracket loop finds an open bracket, or passes the search
    area of the open bracket loop, it returns Invalid. 

    Time Complexity:

    O(n). This algorithm passes every character of the string once until a solution is 
    obtained.

    Space Complexity:

    O(1). This algorithm utilizes two pointers for the search.
    """

    if astr == '':
        return True

    start = 0
    end = len(astr) - 1
    found_open = False
    found_closed = False

    while True:

        while found_open is False:
            if astr[start] == '(':
                found_open = True
            elif astr[start] == ')':
                return 'Invalid'
            elif start >= end:
                return 'Valid'

            start += 1
    
        found_open = False

        while found_closed is False:
            if astr[end] == ')':
                found_closed = True
            elif astr[end] == '(' or end <= start:
                return 'Invalid'

            end -= 1

        found_closed = False
