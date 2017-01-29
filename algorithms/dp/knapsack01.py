def knapsack01(weights, benefits, limit):
    """Given a set of items, each with weight and benefit, determine the items to include
    in the knapsack so that the total weight is less than or equal to a given limit and
    the total benefit is maximized. 

    This solution uses dynamic programming to solve the 0-1 knapsack problem. Using a 
    2-dimensional list, the value of the optimal solution of the 0-1 knapsack problem
    is solved for every subset of the items {0 ... i} along with a maximum allowable
    weight, w. The recursive relationship is given by: 

    OPT[i][w] = OPT[i - 1][w] if weight[i] > w
    else OPT[i][w] = MAX{OPT[i - 1][w], OPT[i - 1][w - weight[i]]}

    The 2-dimensional list is then traced backwards to retrieve the items that correspond
    to the value of the optimal solution.

    In this solution, OPT[0...I][0] = OPT[0][0...W] = 0, corresponding to the fact that
    the maximum benefit for a weight limit of 0 is equivalent to the maximum benefit for
    a subset of 0 items, both of which are 0.

    Time Complexity:

    O(nW). The solution is achieved in psuedo-polynomial time, as a function of the 
    number of items and the maximum allowable weight.

    Space Complexity:

    O(nW). Memoization requires a 2-dimensional list of dimensions n x W.
    """

    max_benefits, OPT = find_max_benefits(weights, benefits, limit, len(weights))
    items = trace_items(OPT, weights, limit, len(weights))
    return max_benefits, items

def find_max_benefits(weights, benefits, limit, max_items):
    OPT = [[0] * (limit + 1) for i in range(max_items + 1)]

    for i in range(1, max_items + 1):
        for w in range(1, limit + 1):
            if weights[i - 1] > w:
                OPT[i][w] = OPT[i - 1][w]
            else:
                OPT[i][w] = max(OPT[i - 1][w], 
                                benefits[i - 1] + OPT[i - 1][w - weights[i - 1]])

    return OPT[max_items][limit], OPT

def trace_items(OPT, weights, limit, max_items):
    items = []
    w = limit

    for i in range(max_items, 0, -1):
        if OPT[i][w] != OPT[i - 1][w]:
            items.append(i)
            w = w - weights[i - 1]

    if w >= weights[0]:
        items.append(1)

    return items
