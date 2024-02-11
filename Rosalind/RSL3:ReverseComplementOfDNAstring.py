# reverse complement a given string. (1st reversed, then complemented/translated)

# Optimal Solution
# s = "AAAACCCGGT"   # solution: "ACCGGGTTTT"
# rev_s = s[::-1]
# translation_data = str.maketrans({"A": "T", "T": "A", "G": "C", "C": "G"})
# rev_c_s = rev_s.translate(translation_data)
# print(rev_c_s)


# 1st code

s = "AAAACCCGGT"
s_list = list(s)

# Swapping: Alternate to block 1 for reversing the string without creating a new list
# i = 0
# # last_index = len(s_list) - 1
# while i < len(s_list) / 2:
#     temp = s_list[i]
#     last_index = len(s_list) - 1 - i
#     s_list[i] = s_list[last_index]
#     s_list[last_index] = temp
#     i += 1
#     # last_index -= 1
# print(s_list)

# Block 1
rev_list_s = []
while len(s_list) > 0:
    rev_list_s.append(s_list.pop(len(s_list)-1))

print(rev_list_s)

rc_list = []
for item in rev_list_s:
    if item == "T":
        rc_list.append("A")
    elif item == "A":
        rc_list.append("T")
    elif item == "C":
        rc_list.append("G")
    elif item == "G":
        rc_list.append("C")

print(rc_list)
rc_str = "".join(rc_list)
print(rc_str)
