from Bio import SeqIO

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL14.txt"
with open(file, 'r') as dna_fasta_file:
    dna_records = list(SeqIO.parse(dna_fasta_file, "fasta"))

dna_seqs = [record.seq for record in dna_records]


def get_longest_common_substr(seq_list):
    longest_common_substr = ""
    for i in range(len(seq_list[0])):
        for j in range(i + 1, len(seq_list[0])):
            substr = seq_list[0][i: j+1]

            if all(substr in seq for seq in seq_list[1:]):
                if len(substr) > len(longest_common_substr):
                    longest_common_substr = substr
    return longest_common_substr


print(get_longest_common_substr(dna_seqs))
print(len(get_longest_common_substr(dna_seqs)))
