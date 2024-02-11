from Bio import SeqIO

seqs_file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/rosalind_gc.txt"

# dna_in_fasta = list(SeqIO.parse(f"./inputs/{args.file_name}", "fasta"))
dna_in_fasta = list(SeqIO.parse(seqs_file, "fasta"))
print(dna_in_fasta)


def computing_gc_content(dna_records):
    temp = -1
    result = ""
    for record in dna_records:
        total_character = len(record.seq)
        gc_count = record.seq.count("G") + record.seq.count("C")
        gc_percentage = (gc_count / total_character) * 100
        if gc_percentage > temp:
            result = f"{record.id}\n{gc_percentage}"
            temp = gc_percentage
    return result


# output = computing_gc_content(dna_in_fasta)
