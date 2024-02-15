import time
start_time = time.time()
##############################################################


file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL6.txt"
with open(file) as seq_file:
    my_string = seq_file.read()

my_list = my_string.split("\n")
# my_list = my_string.split(" ")
seq1 = my_list[0]
seq2 = my_list[1]
mismatch = 0

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        mismatch += 1

print(mismatch)


######################################################
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", execution_time)