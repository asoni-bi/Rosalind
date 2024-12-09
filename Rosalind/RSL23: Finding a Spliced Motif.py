from Bio import SeqIO

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL23.txt"

with open(file, 'r') as seq_file:
    records = list(SeqIO.parse(seq_file, "fasta"))

dna_seq = records[0].seq
subseq = records[1].seq

index_list = [dna_seq.find(subseq[0]) + 1]
for n in subseq[1:]:
    # index = dna_seq[index_list[-1]:].find(n) + index_list[-1]
    index = dna_seq.find(n, index_list[-1]) + 1
    index_list.append(index)

print(" ".join(str(i) for i in index_list))




