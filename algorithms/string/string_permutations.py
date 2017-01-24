def string_permutation(astr):
    """Find all permutations of a string

    This algorithm is a solution to the find all permutations of a string problem
    described on the IDeserve link: 
    http://www.ideserve.co.in/learn/all-permutations-of-a-string.

    The solution recursively produces all the permutations of the string, starting
    with an empty string and building up the permutation using all the possible
    characters from the initial string. 

    Time Complexity:

    T(n) = n*T(n-1) + O(n). If U(n) = T(n)/n!, then T(n) can be represented in terms
    of U(n), such that U(n) = U(n-1) + O(1/(n-1)!) = O(1) + O(1/2!) + O(1/3!) + ... + 
    O(1/(n-1)!) = O(1). Therefore, T(n) = U(n) * n! = O(n!). The total running time 
    will be O(n * n!). 
    """

    all = list()
    string_permutation_util('', astr, all)
    return all

def string_permutation_util(perm, astr, all):
    if not len(astr):
        all.append(perm)
        return

    for i in range(len(astr)):
        next_perm = perm + astr[i] # add ith character to permutation
        next_astr = astr[:i] + astr[i + 1:] # remove ith character
        string_permutation_util(next_perm, next_astr, all)

def string_permutation_swap(astr):
    """Find all permutations of a string by swapping

    This function presents an alternative solution to returning all the permutations
    of a string, by swapping the values of the string repeatedly until no more swaps
    can be performed.
    """

    all = list()
    string_permutation_swap_util(list(astr), 0, len(astr) - 1, all)
    return all

def string_permutation_swap_util(perm, left, right, all):
    if left == right:
        perm = ''.join(perm) # perm is a list of chars
        all.append(perm)
        return

    for i in range(left, right + 1):
        perm[left], perm[right] = perm[right], perm[left] # swap left and right
        string_permutation_swap_util(perm, left + 1, right, all)
        perm[left], perm[right] = perm[right], perm[left] # swap back
