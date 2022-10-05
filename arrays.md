# Arrays
+ [Sum of elements on diag](#sum-of-elements-on-diag)
+ [Merge](#merge)
+ [Squares](#squares)
+ [Compress](#compress)


## Sum of elements on diag
Сумма элементов на главной и побочной диагоналях матрицы
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
## Merge
Слияние двух отстортированных массивов в один
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
## Squares
Вывести массив, состоящий из квадратов элементов исходного массива
```python
def squares(ar):
    
    for i in range(len(ar)):
        if ar[i] >= 0:
            k = i
            break
    
    sq = [el*el for el in ar]
    
    l = sq[:k]
    l.reverse()
    
    r = sq[k:]
    
    return merge(l,r) 
 ```
## Compress
```python
def compress(ar):
    
    ar.append(None)
    prev = ar[0]
    count = 1
    ans = []
    
    for i in range(1,len(ar)):
        if ar[i] != prev:
            if count != 1:
                ans.append(f"{prev}{count}")
            else:
                ans.append(f"{prev}")
            prev = ar[i]
            count = 1
        else:
            count += 1
            
    return ''.join(ans)
```
