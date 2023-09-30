[Merge](#merge)

[Sum of elements on diag](#sum-of-elements-on-diag)

<!-- end -->


## Merge
### Слияние двух отсортированных массивов в один  
```python
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

```
## Sum of elements on diag
### Сумма элементов на главной и побочной диагоналях матрицы  
```python
def diagonalSum(matrix):
    diag_sum = 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            if i == j or i + j == len(mat) - 1:
                diag_sum += mat[i][j]
                print(mat[i][j])

    return diag_sum

```
