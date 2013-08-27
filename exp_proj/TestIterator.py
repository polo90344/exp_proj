class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
    
    def __iter__(self):
        return self


class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
        
    
if __name__ == "__main__":
    ti = TestIterator()
    print(next(ti))
    print(next(ti))
    for i in range(10):
        print(next(ti))