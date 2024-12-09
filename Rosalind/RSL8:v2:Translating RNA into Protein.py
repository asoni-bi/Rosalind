from Bio.Seq import Seq

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL8.txt"

with open(file, 'r') as seq_file:
    rna_seq = Seq(seq_file.read().strip())  # Seq is converting the str to Seq format. Seq operations can then be used.

# passing to_stop=True prevents appending * which indicates a stop codon or end of protein
protein = rna_seq.translate(to_stop=True)
print(protein)
