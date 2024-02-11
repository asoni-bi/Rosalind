import re

dataset = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""

clean_dataset = ((dataset.replace("\n", "")).replace('>', "")).strip()
print(clean_dataset)
pattern = r'Rosalind_\d+'
id_list = re.findall(pattern, clean_dataset)
seq_list = re.split(pattern, clean_dataset)
seq_list = [seq for seq in seq_list if seq]
print(id_list)
print(seq_list)

data_dict = {key: value for key, value in zip(id_list, seq_list)}
print(data_dict)
gc_content_dict = {}
for label, dna_seq in data_dict.items():
    gc_content = float(((dna_seq.count("G") + dna_seq.count("C")) / len(dna_seq)) * 100)
    gc_content_dict.update({label: gc_content})

print(gc_content_dict)

sorted_labels = sorted(gc_content_dict, key=gc_content_dict.get)
resultant_id = sorted_labels[len(sorted_labels)-1]
sorted_gc_content_dict = {key: gc_content_dict[key] for key in sorted_labels}
print(sorted_gc_content_dict)
resultant_gc_percent = sorted_gc_content_dict[resultant_id]
print(resultant_id)
print(resultant_gc_percent)








