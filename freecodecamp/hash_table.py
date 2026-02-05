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
        
        print(self.collection)
    
    def remove(self, key):
        print(self.collection)
        if self.hash(key) in self.collection and key in self.collection[self.hash(key)]:
            del self.collection[self.hash(key)][key]
        else:
            return
        print(self.collection)
        
    def lookup(self, key):
        if self.hash(key) in self.collection and key in self.collection[self.hash(key)]:
            return self.collection[self.hash(key)][key]
  
        else:
            return None
        
        

variable = HashTable()
variable.add("test", 10)
variable.add("ttes", 12)


