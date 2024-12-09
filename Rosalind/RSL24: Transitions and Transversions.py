from Bio import SeqIO

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL24.txt"

with open(file, 'r') as seq_file:
    seq_list = list(SeqIO.parse(seq_file, "fasta"))

s1 = seq_list[0].seq
s2 = seq_list[1].seq

transition_count = 0
transversion_count = 0

for i in range(len(s1)):
    if (s1[i], s2[i]) in (('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')):
        transition_count += 1
    elif (s1[i], s2[i]) in (('A', 'C'), ('A', 'T'), ('C', 'G'), ('C', 'A'), ('T', 'G'), ('T', 'A'), ('G', 'C'),
                            ('G', 'T')):
        transversion_count += 1

print(round(transition_count / transversion_count, 11))
