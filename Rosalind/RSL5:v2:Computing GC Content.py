# solution: 'Rosalind_3071', 53.28874024526199

import re

seqs_file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/rosalind_gc.txt"
with open(seqs_file) as file_data:
    read_file = file_data.read()

data_string = read_file
# print(data_string)


def get_clean_dict(dataset):  # create a clean dictionary with id and its corresponding sequence
    clean_data_dict = {}
    clean_dataset = ((dataset.replace("\n", "")).replace('>', "")).strip()
    pattern = r'Rosalind_\d+'
    id_list = re.findall(pattern, clean_dataset)  # adds all ids to the list
    seq_list = re.split(pattern, clean_dataset)  # add all substrings(sequences) to the list after splitting at id
    seq_list = [seq for seq in seq_list if seq]  # removes any empty sequence from the list
    clean_data_dict = {key: value for key, value in zip(id_list, seq_list)}
    return clean_data_dict


def get_gc_content_for_id_dict(data_dict):  # create a dictionary with id and its corresponding gc percentage
    gc_content_for_id = {}
    for label, dna_seq in data_dict.items():
        gc_content = float(((dna_seq.count("G") + dna_seq.count("C")) / len(dna_seq)) * 100)
        gc_content_for_id.update({label: gc_content})
    return gc_content_for_id


def get_sorted_data(gc_content_dict):
    # # below statement sorts the dict by values(gc %) in dict and creates a list of corresponding ids in that order
    # sorted_labels = sorted(gc_content_dict, key=gc_content_dict.get)
    # # below statement returns the id of the sequence with highest gc percent
    # resultant_id = sorted_labels[len(sorted_labels)-1]
    # # below statement creates a sorted dictionary with id and gc percent
    # sorted_gc_content_dict = {key: gc_content_dict[key] for key in sorted_labels}
    # resultant_gc_percent = sorted_gc_content_dict[resultant_id]
    # return resultant_id, resultant_gc_percent, sorted_gc_content_dict
    resultant_id = ""
    resultant_gc_percent = 0
    for label, gc_percent in gc_content_dict.items():
        if gc_percent > resultant_gc_percent:
            resultant_gc_percent = gc_percent
            resultant_id = label
    return resultant_id, resultant_gc_percent


def get_highest_gc_content_data(id_and_sequences):
    clean_dict = get_clean_dict(id_and_sequences)
    gc_content_for_id_dict = get_gc_content_for_id_dict(clean_dict)
    sorted_data = get_sorted_data(gc_content_for_id_dict)
    return sorted_data


print(get_highest_gc_content_data(data_string))








