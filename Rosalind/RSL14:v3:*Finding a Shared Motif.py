from Bio import SeqIO

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL14.txt"
with open(file, 'r') as dna_fasta_file:
    dna_records = list(SeqIO.parse(dna_fasta_file, "fasta"))

dna_seqs = sorted([record.seq for record in dna_records], key=len)


def get_longest_common_substr(seq_list):
    longest_common_substr = ""
    # seq_list[0] is the base seq, substrings of which will be matched against other seqs
    base_seq_len = len(seq_list[0])
    while base_seq_len > 0:
        for i in range(len(seq_list[0]) - base_seq_len + 1):
            substr = seq_list[0][i: i+base_seq_len]
            if all(substr in seq for seq in seq_list[1:]):
                if len(substr) > len(longest_common_substr):
                    longest_common_substr = substr
        base_seq_len -= 1
    return longest_common_substr


longest_common_substring = get_longest_common_substr(dna_seqs)
print(longest_common_substring)
print(len(longest_common_substring))

