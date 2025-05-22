class Set:
    def __init__(self, li = []):
        # constant => o(1) => dictionary
        self.dictionary = {}
        # s= {1, 3, 5, 6}
        for value in li:
            self.dictionary[value] = True
            
    def has(self, value):
        return value in self.dictionary
    def size(self):
        return len(self.dictionary)
            
s1 = Set([1, 2, 2, 3, 4, 1, 5])
# {1,2,3, 4, 5}

print(s1.size())