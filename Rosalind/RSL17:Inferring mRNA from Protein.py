file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL17.txt"
with open(file, 'r') as protein_file:
    protein_seq = protein_file.read().strip()

codon_aa_dict = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V", "UUA": "L",
           "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P",
           "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T",
           "GCA": "A", "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
           "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
           "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
           "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G", "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
           "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}


def get_codon_count_for_aa(aa):
    aa_list = list(codon_aa_dict.values())
    codon_count_for_aa = aa_list.count(aa)
    return codon_count_for_aa


def get_possible_rna_count_for_protein(prot_seq):
    stop_codon_count = get_codon_count_for_aa("Stop")
    possible_rna_count = 1
    for aa in prot_seq:
        codons_for_aa = get_codon_count_for_aa(aa)
        possible_rna_count *= codons_for_aa
    possible_rna_count *= stop_codon_count
    return possible_rna_count


print(get_possible_rna_count_for_protein(protein_seq) % 1000000)











