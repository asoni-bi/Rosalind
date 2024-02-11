# solution: 249650241628 for n=33, k=3

n = int(input("Enter the month number: "))
k = int(input("Enter the number of offsprings per pair: "))

# f1 = f2 = 1
# f3 = f2 + (f1 * k)

seq_list = [1, 1]
pairs_next_month = 0
i = 2
while i < n:
    pairs_next_month = seq_list[i-1] + (seq_list[i-2] * k)
    seq_list.append(pairs_next_month)
    i += 1

print("Rabbit pairs alive in month {}: {}".format(n, seq_list[n-1]))
