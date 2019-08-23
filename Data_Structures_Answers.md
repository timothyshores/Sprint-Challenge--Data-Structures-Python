Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

```
if self.current == self.capacity:
    self.storage[0] = item # O(1)
    self.current = 1 # O(1)
else: 
    self.storage[self.current] = item # O(1)
    self.current += 1 # O(1)
```

Both conditions have a runtime of O(2) or const time which is O(1)

2. What is the space complexity of your ring buffer's `append` function?

The size of self.storage will always be self.capacity

3. What is the runtime complexity of your ring buffer's `get` method?

Linear time O(n) because Python's filter function creates an iterator that checks every element in self.storage to see if the value is None

https://docs.python.org/3/library/functions.html#filter

4. What is the space complexity of your ring buffer's `get` method?

The get method does not create a new list to return. The elements returned are in the self.storage list.

5. What is the runtime complexity of the provided code in `names.py`?

O(n^2) due to nested for loops

6. What is the space complexity of the provided code in `names.py`?

names_1 is a list with n elements where n is the number of lines in names_1.txt
names_2 is a list with n elements where n is the number of lines in names_2.txt
duplicates is a list with n elements where n is the number of 

7. What is the runtime complexity of your optimized code in `names.py`?

```
duplicates = []                         #O(1)
bst = BinarySearchTree(names_1[0])      #O(1)

for name1 in names_1[1:]:               #O(n-1)
    bst.insert(name1)                   #O(1)

for name2 in names_2:                   #O(n)
    if bst.contains(name2):             #O(log n)
        duplicates.append(name2)        #O(1)
```

Create duplicates list and bst is O(2). Looping through names_1 is O(n). Looping through names_2 and checking if bst contains name2 is O(n log n). The runtime complexity is O(n log n)

8. What is the space complexity of your optimized code in `names.py`?

Both names_1 & names_2 are lists where the size is the number of names in names_1.txt and names_1.txt respectively. Then bst is the size of the names_1 list where every element in the list is a node in a BST. Duplicates is the size of the number of duplicate names which at maximum could be the size of the smaller list.