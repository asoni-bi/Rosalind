from Bio import SeqIO
# read FASTA file and save DNA seq
file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL18.txt"
with open(file, 'r') as fasta_dna_file:
    dna_records = list(SeqIO.parse(fasta_dna_file, "fasta"))

dna_seq = dna_records[0].seq
bp = {"A": "T", "T": "A", "C": "G", "G": "C"}
start_codon = {"AUG"}
stop_codons = {"UAA", "UAG", "UGA"}
codon_aa_dict = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V", "UUA": "L",
           "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P",
           "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T",
           "GCA": "A", "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
           "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
           "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
           "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G", "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
           "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}

# reverse DNA seq and store it
def get_reversed_seq(sequence):
    rev_seq = ''.join(reversed(sequence))
    return rev_seq

# complement reversed DNA and store it
def complement_bp(sequence):
    complemented_seq = ""
    for nucleotide in sequence:
        complemented_seq += bp[nucleotide]
    return complemented_seq

def transcribe_to_mrna(sequence):
    rna_seq = ""
    for nucleotide in sequence:
        if nucleotide != "T":
            rna_seq += nucleotide
        else:
            rna_seq += "U"
    return rna_seq


# function to translate ORFs to proteins
def translate_to_protein(open_reading_frame):
    protein_seq = ""
    for i in range(0, len(open_reading_frame)-2, 3):
        # print(open_reading_frame[i:i+3])
        protein_seq += codon_aa_dict[open_reading_frame[i:i+3]]
    return protein_seq


# look for ORFs - substrings that start with start codon and ends before the stop codons(excludes stop codon)
# If an ORF is found, translate it and append to the protein list
def get_unique_protein_list(sequence):
    unique_protein_list_of_given_seq = []
    for frame in range(3):
        for i in range(frame, len(sequence)-2, 3):
            if sequence[i:i+3] in start_codon:
                for j in range(i+3, len(sequence)-2, 3):
                    if sequence[j:j+3] in stop_codons:
                        open_reading_frame = sequence[i:j]
                        protein_seq = translate_to_protein(open_reading_frame)
                        if protein_seq not in unique_protein_list_of_given_seq:
                            unique_protein_list_of_given_seq.append(protein_seq)
                        break
    return unique_protein_list_of_given_seq

def get_unique_seqs_from_protein_lists(list_of_protein_lists):
    unique_seqs = list_of_protein_lists[0]
    for i in range(1, len(list_of_protein_lists)):
        for protein_seq in list_of_protein_lists[i]:
            if protein_seq not in unique_seqs:
                unique_seqs.append(protein_seq)
    return unique_seqs


transcribed_seq = transcribe_to_mrna(dna_seq)
reverse_complemented_transcribed_seq = transcribe_to_mrna(complement_bp(get_reversed_seq(dna_seq)))
forward_seq_protein_list = get_unique_protein_list(transcribed_seq)
reverse_complemented_seq_protein_list = get_unique_protein_list(reverse_complemented_transcribed_seq)
combined_protein_list = [forward_seq_protein_list, reverse_complemented_seq_protein_list]
unique_seqs_from_protein_lists = get_unique_seqs_from_protein_lists(combined_protein_list)

for protein in unique_seqs_from_protein_lists:
    print(protein)