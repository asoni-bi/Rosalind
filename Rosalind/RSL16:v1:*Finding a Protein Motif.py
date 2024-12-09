import requests
import re

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL16.txt"
with open(file, 'r') as access_ids:
    acc_id_list = access_ids.read().split('\n')


def get_primary_acc_id(acc_id):
    split_index = acc_id.find("_")
    if split_index != -1:
        primary_acc_id = acc_id[:split_index]
    else:
        primary_acc_id = acc_id
    return primary_acc_id


def get_seq_from_uniprot(primary_id):
    url = f"https://www.uniprot.org/uniprot/{primary_id}.fasta"
    response = requests.get(url)
    if response.ok:
        header, sequence = response.text.strip().split('\n', 1)
        sequence = sequence.replace('\n', '')
        return sequence
    else:
        print("failed to fetch sequence for {}".format(primary_id))
        return None


def get_motif_locations(seq, pattern, motif_len):
    motif_locations = ""
    for i in range(len(seq)-motif_len+1):
        motif = seq[i: i+motif_len]
        if re.match(pattern, motif):
            motif_locations += (str(i+1) + " ")
    return motif_locations


def motif_positions_by_acc_id(id_list, motif_pattern, length):
    for raw_acc_id in id_list:
        acc_id = get_primary_acc_id(raw_acc_id)
        protein_seq = get_seq_from_uniprot(acc_id)
        if protein_seq:
            motif_positions = get_motif_locations(protein_seq, motif_pattern, length)
            if len(motif_positions) > 0:
                print(raw_acc_id)
                print(motif_positions)


motif_positions_by_acc_id(acc_id_list, r'^N[^P][ST][^P]$', 4)
