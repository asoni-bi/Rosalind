# Initialize the list with number of rabbits alive in 1st 2 months as this is a given
pairs_alive = [1, 1]


def rabbits_alive(n, m):  # n is month in which we need to find live rabbits, m is no. of months after which rabbits die
    for i in range(2, n):
        # since we have 2 items in the pairs_alive list, we will start iterating from index 2 till index 5
        # or in other words month 3 to month 6
        if i < m:
            # i < m (index 2 if m is 3), which means until month 3, which means until none of the rabbits died
            # if m is 3, rabbits will start dying after month 3, that means first death will be in month 4
            # so, we don't need to account for deaths yet, and pairs_alive in the current month will be:
            # pairs_alive in last month (Fn−1) + new offsprings in current month, which we know,
            # is equal to the total number of pairs_alive in the month before the last month (Fn-2)
            pairs_alive_in_current_month = pairs_alive[i-1] + pairs_alive[i - 2]
        elif i == m:
            # i == m (index 3 if m is 3), which means month 4
            # Since rabbits start dying in month 4, we need to account for deaths to calculate pairs_alive in month 4
            # which will be: pairs_alive in last month(Fn−1) + new offsprings in current month(Fn-2) - deaths this month
            # deaths this month = newborns m months ago (as now they are m months old and will die)
            # again, no. of offsprings in a given month  = no. of pairs_alive in the month before the last month
            # deaths this month = newborns m months ago = pairs_alive 2 months before m months back from current month
            # pairs_alive 2 months before m months back from current month =  pairs_alive[current month(i +1) - m (to
            # represent m months back) - 2(to represent 2 months before m months)
            # deaths this month = pairs_alive[(i+1) - m - 2] = pairs_alive[i - m -1]
            # now when i == m, which in this case is 3, current month is 4. If we calculate deaths in month 4,
            # deaths this month(month4) = pairs_alive[i - m -1] = pairs_alive[3 - 3 - 1] = pairs_alive[-1], this will
            # return the last value in the list which will be wrong
            # so for this scenario only, we will subtract the death directly as we know,
            # this will be the first death, and since we started with 1 pair, the first death after m months
            # will always be of 1 pair
            # pairs_alive_in_current_month = (Fn−1) + (Fn-2) - deaths this month
            pairs_alive_in_current_month = pairs_alive[i-1] + pairs_alive[i-2] - 1
        else:
            # for all other cases where i > m (4 > 3, or 5 > 3...) that is, current month is 5, or 6...
            # deaths this month = pairs_alive[(i+1) - m - 2] = pairs_alive[i - m -1]
            pairs_alive_in_current_month = pairs_alive[i - 1] + pairs_alive[i - 2] - pairs_alive[i - m - 1]
        pairs_alive.append(pairs_alive_in_current_month)
    return pairs_alive[-1]  # returns last value in the pairs_alive list which is pairs_alive in nth month


print(rabbits_alive(6, 3))






