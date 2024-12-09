from Bio import SeqIO

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL14.txt"
with open(file, 'r') as dna_fasta_file:
    dna_records = list(SeqIO.parse(dna_fasta_file, "fasta"))


def get_shortest_seq():
    shortest_seq = dna_records[0].seq
    for record in dna_records:
        if len(record.seq) < len(shortest_seq):
            shortest_seq = record.seq
    return shortest_seq


def get_sub_str_matches():
    shortest_dna_seq = get_shortest_seq()
    match = {}
    for i in range(len(shortest_dna_seq)):
        for j in range(i+1, len(shortest_dna_seq)):
            sub_str = shortest_dna_seq[i:j+1]
            match.update({sub_str: 0})
            for dna_seq in dna_records:
                if sub_str in dna_seq.seq:
                    match[sub_str] += 1
    return match


def get_most_common_longest():
    substr_matches = get_sub_str_matches()
    max_occurrence = max(substr_matches.values())
    max_occurred_substr_list = []
    for key, value in substr_matches.items():
        if value == max_occurrence:
            max_occurred_substr_list.append(key)
    max_length = max(len(s) for s in max_occurred_substr_list)
    most_common_longest_list = [s for s in max_occurred_substr_list if len(s) == max_length]
    return most_common_longest_list


print("shortest: " + get_shortest_seq())
print(get_most_common_longest())
print(get_most_common_longest()[0])









