def min_edits(astr, bstr):
    """Find the minimum edit distance between two strings

    This algorithm is a solution to the minimum edit distance problem described on the
    IDeserve link: http://www.ideserve.co.in/learn/edit-distance-dynamic-programming. 

    This problem simplifies down to a sequence alignment problem and can be solved
    using dynamic programming. There are three types of edits, each with an edit
    distance of one: insertions, deletions, and substitutions. As a result, in 
    calculating the minimum edit distance of two substrings {a0...ai} and {b0...bj}
    we observe four cases: 

    1. ai and bj match, and no edits are required. 
    2. ai and bj do not match, and a substitution on ai yields an optimal solution.
    3. ai and bj do not match, and an insertion on ai yields an optimal solution.
    4. ai and bj do not match, and a deletion on ai yields an optimal solution.

    Another critical point in solving this solution is the fact that a deletion of ai
    is synonymous with an insertion on bj, and vice versa. This allows us to simplify
    the four cases into two classes: one that requires a gap or a shift (an insertion
    or deletion), and one that does not (a match or a substitution). Furthermore, we
    can determine which case to take when a match does not occur based on previously
    calculated values. That is, if ai and bj do not match, the optimal solution is the
    case that results in the minimum edit distance. 

    Time Complexity: 

    O(nm). The final solution relies on the fact that we calculate solutions for every
    subproblem of astr (length n) and bstr (length m). 

    Space Complexity:

    O(nm). The OPT array is a double list of dimensions n x m.
    """

    return min_edits_util(astr, bstr, len(astr), len(bstr))

def min_edits_util(astr, bstr, alen, blen):
    OPT = [[0] * (alen + 1) for bchar in range(blen + 1)]

    for i in range(blen + 1):
        for j in range(alen + 1):

            if i == 0:
                # j insertions in front of bstr
                OPT[0][j] = j

            elif j == 0:
                # i insertions in front of astr
                OPT[i][0] = i

            else:
                # all possibilities
                match = OPT[i - 1][j - 1] + int(not (bstr[i - 1] == astr[j - 1]))
                ashift = OPT[i][j - 1] + 1
                bshift = OPT[i - 1][j] + 1
                OPT[i][j] = min(match, ashift, bshift)

    return OPT[blen][alen]
