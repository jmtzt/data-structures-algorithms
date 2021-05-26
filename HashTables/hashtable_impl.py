class HashTable:
    
    def __init__(self):
        self.size = 3
        self.hashes = [None] * self.size

    def __str__(self):
        return str(self.__dict__)

    def hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
        return hash


    def put(self, key, value):
        hash_val = self.hash(key)
        if not self.hashes[hash_val]:
            self.hashes[hash_val] = [[key, value]]
        else:
            self.hashes[hash_val].append([key, value])
        return None


    def get(self, key):
        hash_val = self.hash(key)
        ref = self.hashes[hash_val]
        for i in range(len(ref)):
            if ref[i][0] == key:
                return ref[i][1]
        return None

    def remove(self, key):
        hash_val = self.hash(key)
        ref = self.hashes[hash_val]
        for i in range(len(ref)):
            if ref[i][0] == key:
                ref.pop(i)
                return None
        return None
    
h=HashTable()
h.put('a',1000)
h.put('b1',10)
h.put('c23',300)
h.put('d324',200)
h.put('34544',1)
h.put('43333',2)
h.put('554555',3)
h.put('6555555',4)
print(h.get('a'))
print(h)
h.remove('a')
print(h)

    
