from user import User

class HashingTable(object):
    def __init__(self, tablesize):
        self.tablesize = tablesize
        self.slots = [None] * self.tablesize
        self.buckets = [None] * self.tablesize

    def hash(self, astring):
        sum = 0
        for pos in range(len(astring)):
            sum += ord(astring[pos]) * pos
            
        return sum % self.tablesize

    def put(self, key, user):
        hashindex = self.hash(key)
        
        if self.slots[hashindex] == None:
            self.slots[hashindex] = key
            self.buckets[hashindex] = user
        else:  
            if self.slots[hashindex] != key: 
                newhashindex = self.chaining(hashindex, len(self.slots))
               
               #esse while procura um novo hash index enquanto ele for igual a chave ou o slot nao estiver vazio
                while self.slots[newhashindex] != None and self.slots[newhashindex] != key:
                    newhashindex = self.nexthash(chaining,len(self.slots))
               
                if self.slots[newhashindex] == None:
                    self.slots[newhashindex] = key
                    self.buckets[newhashindex] = user
                else:
                    self.buckets[newhashindex] = buckets #replace
            else:
                self.buckets[hashindex] = user        
            
    def chaining(self, oldhash):
        #reprogramar usando a tecnica de chaining (esqueci como que eh rs)
        return ( oldhash + 1 ) % self.tablesize

    def contains(self, name):
        return self.search(self.buckets[self.tablesize], name) != None
        
    def search(self, buckets, key):
        index = None
        for i in range(len(buckets)):
            if buckets[i].name == key:
                index = i
        return index

    def get(self, key):
        exists = self.contains(key)
        
        if exists:
            index = self.hash(key)
            name = self.buckets[index].name
            height = str(self.buckets[index].height)
            print(f"----- user ----- \n  name: {name} \n  height: {height}")
        else:
            print("the informed user doesn't exist in the database.")

    
    def generatedata():
        pass