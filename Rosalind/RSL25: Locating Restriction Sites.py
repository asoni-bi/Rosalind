from Bio import SeqIO

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL25.txt"

with open(file, 'r') as seq_file:
    sequences = list(SeqIO.parse(seq_file, 'fasta'))

dna_seq = str(sequences[0].seq)
bp = {"A": "T", "T": "A", "C": "G", "G": "C"}


def get_reversed_seq(sequence):
    rev_seq = ''.join(reversed(sequence))
    return rev_seq


# complement reversed DNA and store it
def complement_bp(sequence):
    complemented_seq = ""
    for nucleotide in sequence:
        complemented_seq += bp[nucleotide]
    return complemented_seq


def get_palindrome_substrings(seq1, seq2, min_limit, max_limit):
    total_palindromes = 0
    if min_limit > len(seq1):
        return 0
    if max_limit > len(seq1):
        max_limit = len(seq1)
    for i in range(len(seq1)):
        if len(seq1[i:i+min_limit]) != min_limit:
            print("Total palindromes: " + str(total_palindromes))
            break
        for k in range(min_limit, max_limit+1):
            if len(seq1[i:i+k]) != k:
                break
            if seq1[i:i+k] == get_reversed_seq(seq2[i:i+k]):
                total_palindromes += 1
                print(str(i+1) + "\t" + str(len(seq1[i:i+k])))


complemented_sequence = complement_bp(dna_seq)
print(dna_seq)
print(complemented_sequence)
print("----------------------------------------------------")
get_palindrome_substrings(dna_seq, complemented_sequence, 4, 12)
