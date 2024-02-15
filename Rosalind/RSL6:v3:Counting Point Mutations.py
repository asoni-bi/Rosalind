# import operator
import time
start_time = time.time()
##############################################################

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL6.txt"
with open(file) as seq_file:
    seq_list = (seq_file.read()).split("\n")

seq1 = seq_list[0]
seq2 = seq_list[1]

print(sum(1 for base1, base2 in zip(seq1, seq2) if base1 != base2))

# OR
# print(sum(map(operator.ne, seq1, seq2)))


##############################################################

end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)