class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = []

    def append(self, item):
        # storage is at capacity and first item is the oldest
        if len(self.storage) == self.capacity and self.current == len(self.storage):
            # remove first element and insert value into index 0
            self.storage.pop(0)
            self.storage.insert(0, item)
            self.current = 1
        # storage is at capacity and second item is the oldest
        elif:
            pass
        # storage is not at capacity, append item and increment current
        else:
            self.storage.append(item)
            self.current += 1

    def get(self):
        return f"Storage: {self.storage}, Current: {self.current}"


buffer = RingBuffer(3)

print("should return []")   # should return []
print(buffer.get())   # should return []

buffer.append('a')
print(buffer.get())   # should return ['a'], 1
buffer.append('b')
print(buffer.get())   # should return ['a', 'b'], 2
buffer.append('c')
print(buffer.get())   # should return ['a', 'b', 'c'], 3


print("should return ['a', 'b', 'c']")
print(buffer.get())   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

print("should return ['d', 'b', 'c']")
print(buffer.get())   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
