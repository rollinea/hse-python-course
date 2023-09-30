# title Merge
# description Слияние двух отсортированных массивов в один
# ---end---
def merge(first, second):
    merged_list = []
    i, j = 0, 0
    while i < len(first) and j < len(first):
        if first[i] < second[j]:
            merged_list.append(first[i])
            i += 1
        else:
            merged_list.append(second[j])
            j += 1

    while i < len(first):
        merged_list.append(first[i])
        i += 1

    while j < len(second):
        merged_list.append(second[j])
        j += 1

    return merged_list
