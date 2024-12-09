# s = "GATATATGCATATACTT"
# t = "ATAT"

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL9.txt"
with open(file, 'r') as dna_motif_file:
    dna_motif = dna_motif_file.read().strip().split("\n")

s = dna_motif[0]
t = dna_motif[1]
t_positions = ""
for i in range(len(s)):
    if s[i:i+len(t)] == t:
        t_positions += str(i+1) + " "

print(t_positions)
