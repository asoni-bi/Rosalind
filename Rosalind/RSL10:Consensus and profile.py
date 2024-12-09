from Bio import SeqIO

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL10.txt"

with open(file, 'r') as fasta_dna_file:
    dna_records = list(SeqIO.parse(fasta_dna_file, "fasta"))

seq_length = (len(dna_records[0].seq))
profile = {"A": [], "C": [], "G": [], "T": []}

for i in range(seq_length):
    a_counter = c_counter = g_counter = t_counter = 0
    for record in dna_records:
        if record.seq[i] == "A":
            a_counter += 1
        elif record.seq[i] == "C":
            c_counter += 1
        elif record.seq[i] == "G":
            g_counter += 1
        elif record.seq[i] == "T":
            t_counter += 1

    profile["A"].append(a_counter)
    profile["C"].append(c_counter)
    profile["G"].append(g_counter)
    profile["T"].append(t_counter)

consensus = ""
for j in range(seq_length):
    temp_cons = ""
    c = 0
    for k in range(len(profile)):
        if list(profile.values())[k][j] > c:
            c = list(profile.values())[k][j]
            temp_cons = list(profile.keys())[k]
    consensus += temp_cons

print(consensus)
for key, value in profile.items():
    print(key + ": " + ' '.join(map(str, value)))
