# Practice 1
+ [Hello World](#hello-world)
+ [Max Sequence](#max-sequence)
+ [SumRanges](#sumranges)

## Hello World
### Вывести "hello", "world", "helloworld" в зависимости от индекса
```python
def helloWorld(n):
    for i in range(1,n+1):
        if i % 3 == 0  and i % 5  == 0:
            print("helloworld")
        elif i % 3 == 0:
            print("hello")
        elif i % 5 == 0:
            print("world")
        else:
            print(i)
```
## Max Sequence
### Вывести длину максимальной по включению последовательности, состоящей из единиц
```python
def find_max_seq(lst):
    cur_max, best_max = 0, 0
    
    for i in range(len(lst)):
        if lst[i] == 1:
            cur_max += 1
        else:
            if cur_max > best_max:
                best_max = cur_max
            
            cur_max = 0
            i += 1
            
    return best_max
```

## SumRanges
### Вывести подпоследовательность в виде "начало -> конец", если ее элементы отличаются не более, чем на 1. 
```python
def sumRanges(lst):
    
    ans = []
    start = 0
    
    for i in range(len(lst)):
        
        if (i + 1 == len(lst)) or (lst[i] + 1 != lst[i+1]):
            
            if i != start:
                ans.append(f"{lst[start]} -> {lst[i]}")
            else:
                ans.append(str(lst[i]))
            
            start = i + 1
        
    return ans
```
