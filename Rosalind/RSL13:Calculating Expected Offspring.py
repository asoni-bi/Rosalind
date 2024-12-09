# Probabilities of dominant offsprings: AA-AA = 1, AA-Aa = 1, AA-aa = 1, Aa-Aa = 0.75, Aa-aa = 0.5, aa-aa = 0

file = "/Users/astha/PycharmProjects/Bioinformatics Projects/Rosalind/Downloaded Datasets/RSL13.txt"
with open(file, 'r') as couples_count_file:
    couple_count_list = couples_count_file.read().split(" ")

dominance_probability = {"AA-AA": 1, "AA-Aa": 1, "AA-aa": 1, "Aa-Aa": 0.75, "Aa-aa": 0.5, "aa-aa": 0}


def cal_dominant_offsprings(offsprings_per_pair):
    total_dominant = 0
    for i in range(len(couple_count_list)):
        total_dominant += offsprings_per_pair * (int(couple_count_list[i]) * list(dominance_probability.values())[i])
    return total_dominant


print(cal_dominant_offsprings(2))



