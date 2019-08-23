class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = [None]*capacity

    def append(self, item):
        # self.current pointer is at end of self.storage
        if self.current == self.capacity:
            # assign item to the first element of self.storage
            self.storage[0] = item
            # set self.current pointer to index 1
            self.current = 1
        else:
            # assign item to self.current pointer index of self.storage
            self.storage[self.current] = item
            # increment self.current pointer
            self.current += 1

    # return self.storage with all occurences of None removed
    def get(self):
        return list(filter(lambda a: a != None, self.storage))

    # helper debugging method
    def debug(self):
        return f"Storage: {self.storage}, Current: {self.current}"
