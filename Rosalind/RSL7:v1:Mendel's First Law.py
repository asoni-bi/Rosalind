def cal_self_cross(num):
    self_cross = 0
    for diff in range(num):
        self_cross += diff
    return self_cross


def cal_cross_breed(num1, num2):
    cross_breed = num1 * num2
    return cross_breed


def cal_total_outcomes(k, m, n):
    self_cross_outcomes = (cal_self_cross(k) + cal_self_cross(m) + cal_self_cross(n)) * 4
    cross_breed_outcomes = (cal_cross_breed(k, m) + cal_cross_breed(k, n) + cal_cross_breed(m, n)) * 4
    total_outcomes = self_cross_outcomes + cross_breed_outcomes
    return total_outcomes

# homozygous dominant x anything = 4 dominants out of 4 outcomes
# heterozygous x heterozygous = 3 dominants out of 4 outcomes
# heterozygous x homozygous recessive = 2 dominants out of 4 outcomes
# homozygous recessive x homozygous recessive = 0 dominants out of 4 outcomes
def cal_total_dominant(k, m, n):
    dominant_k_breeds = (cal_self_cross(k) + cal_cross_breed(k, m) + cal_cross_breed(k, n)) * 4
    dominant_m_breeds = (cal_self_cross(m) * 3) + (cal_cross_breed(m, n) * 2)
    # no dominant breeds for n(recessive) self cross
    total_dominant = dominant_k_breeds + dominant_m_breeds
    return total_dominant


def cal_dominance_probability(k, m, n):
    dominance_probability = float(cal_total_dominant(k, m, n) / cal_total_outcomes(k, m, n))
    return dominance_probability


print(cal_dominance_probability(2, 2, 2))
print(cal_dominance_probability(2, 3, 1))
print(cal_dominance_probability(17, 25, 27))








