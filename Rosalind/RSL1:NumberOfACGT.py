
s = "GTCTGTACTCGTGTATAGAGAACGGTACGCGACGATTCGTGGGCGGGACTTTGATATGCGTATTCCGGACGGAAAGTGCCATCGCAAATTGATAGAGCATCTTGGATTTCACGCCAGCGAGGACGGCCGTACCGTGCCGGGCACACTATCTAGTATTGACTTGGTTCTGCAGTTCAGGCTTAGCCTTGTTACAATCCTGGTCAACCCTCGCTACGATCAAGCACTTACCGATGGCCCGAAGAAGTGTAGGGCCCGCATGATCCTCAACAATAGGGAGAGTCCCCCGAGGAGAGCCTTTGCCGGCGCTCCGAGTCGGGGGCGACCGTACACGGCAAGTCCCACTGGATTTTGTTGGAGCCGCGCTAAGGAGCCGTTGTCGGCTTTAACTATGAGGATCAGGCATCTTTAAGGGCCTTGTAATGCAAGATTCCCTACTATAGGTGGCCCGGCGAGATCTGCCGCCTGAAATCCGGGGAGGCGCGCAGAATAGAAGCGACCGTGGCAATCTACGATCTCTTGACAGAGTGTTTGATAGGGAAAACATCCTCTTGAGGGCAAGTCCCTCTTCTCTTAAAACTTATATGTGTTAATCCTGTCTCGAGACTTGTGCGTCTAAGGCGGAGTGATGGACGATCTACCTCGAAGTGAGAAGTCGTCGCATATAGGGCCGAAACCCCGAAAGACTTTCATAGTGCCACGCTTGAACACGTTCCACCTTCAGTACTATTCTCTGGATCGCGTCGGTTCATAGTTTCGTGGTGTCCGGGATCGCCGCGAACGTCAGTCCCATAGGAACGCGATAGGAAGAAAGACAGACCCCCC"

nucleotide_count = {"A": 0, "C": 0, "G": 0, "T": 0}

for nucleotide in list(s):
    if nucleotide in nucleotide_count.keys():
        nucleotide_count[nucleotide] += 1

print(str(nucleotide_count["A"]) + " " + str(nucleotide_count["C"]) + " "
      + str(nucleotide_count["G"]) + " " + str(nucleotide_count["T"]))

# OR
# print(str(s.count("A")) + " " + str(s.count("C")) + " " + str(s.count("G")) + " " + str(s.count("T")))