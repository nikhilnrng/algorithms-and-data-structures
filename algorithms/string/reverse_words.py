def reverse_words(astr):
    """Reverse the words in a string while preserving whitespace delimiters

    This algorithm is a solution to the reverse words problem described on the 
    IDeserve link: http://www.ideserve.co.in/learn/reverse-words-in-a-string

    The solution walks through the string backwards and constructs a reversed string,
    adding characters to the reversed string each time it encounters an end to a word
    or an end to a sequence of whitespace. The 'is_space' and 'changed' variables
    are essentially just flags that indicate when a sequence of word characters 
    or whitespace characters is complete. 

    Time Complexity: 

    O(n). This algorithm decrements through the entire string sequence one time. 

    Space Complexity: 

    O(n). This algorithm utilizes a new 'out' variable to store the reversed string.

    Note, an alternate solution would be to reverse all the words, and then reverse
    the entire string. This solution would provide constant space complexity since
    a reverse string variable would not be required. However, Python strings are
    immutable, so such a solution would not technically be modifying the original 
    string, but instead, create a new string on each reversal. This is also observed
    in the solution below, in which the out variable is constantly concatenated to 
    until no more characters are left in the original string. 
    """

    if len(astr) == 0:
        return ''

    start = len(astr) - 1
    end = len(astr)
    is_space = astr[start:end] == ' '
    changed = not is_space
    out = ''

    while start > 0:

        while is_space is not changed:
            start -= 1
            is_space = astr[start:start + 1] == ' '

        out += astr[start + 1:end]
        end = start + 1
        changed = not is_space

    out += astr[start:end]
    return out
