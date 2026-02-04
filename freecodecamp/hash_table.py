class HashTable:
    def __init__(self):
        self.collection = {}
    
    def hash(self, text: str):
        return sum(ord(x) for x in text)
    
    def add(self, key, value):
        if self.hash(key) in self.collection:
            self.collection[self.hash(key)][key] = value
        else:
            self.collection[self.hash(key)] = {key: value}
    
    def remove(self, key):
        if self.hash(key) in self.collection:
            self.collection.pop(self.hash(key))
        else:
            pass
    
    def lookup(self, key):
        if self.hash(key) in self.collection:
            return self.collection[self.hash(key)][key]
        else:
            return None
        
        

variable = HashTable()
variable.add("ciao", 10)
variable.add("ciao", 12)

