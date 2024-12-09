from Bio import SeqIO
from Bio.Seq import Seq

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL21.txt"
with open(file, 'r') as seqs_file:
    seq_list = list(SeqIO.parse(seqs_file, "fasta"))

dna_seq = seq_list[0].seq
intron_list = [i.seq for i in seq_list[1:len(seq_list)]]


def remove_introns(dna_sequence, list_of_introns):
    for intron in list_of_introns:
        if intron in dna_sequence:
            dna_sequence = dna_sequence.replace(intron, '')
    return dna_sequence


coding_dna_seq = Seq(remove_introns(dna_seq, intron_list))
mrna_seq = coding_dna_seq.transcribe()
protein_seq = mrna_seq.translate()[:-1]

print(protein_seq)







