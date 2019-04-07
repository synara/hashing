from user import User

class HashingTable(object):
    def __init__(self, tablesize):
        self.tablesize = tablesize
        self.slots = [[User]] * self.tablesize

    def hash(self, astring):
        sum = 0
        for pos in range(len(astring)):
            sum += ord(astring[pos])
            
        return sum % self.tablesize

    def put(self, key, user):
        hashindex = self.hash(key)

        if self.slots[hashindex] == [User]:
            self.slots[hashindex] = []
            self.slots[hashindex].append(user)
        else: 
            indexvalues = len(self.slots[hashindex])

            for i in range(indexvalues):
                name = self.slots[hashindex][i].name
                if self.slots[hashindex][i].name != key: 
                    newhashindex = self.chaining(hashindex)
               
                    #esse while procura um novo hash index enquanto ele for igual a chave ou o slot nao estiver vazio
                    while self.slots[newhashindex] != [User] and self.slots[newhashindex][i].name != key:
                        newhashindex = self.chaining(newhashindex)
               
                    if self.slots[newhashindex] == [User]:
                        self.slots[newhashindex] = []
                        self.slots[newhashindex].append(user)
                    else:
                        self.slots[newhashindex] = user #substitui
                else:
                    self.slots[hashindex][i] = user 
                   
            
    def chaining(self, oldhash):
        #reprogramar usando a tecnica de chaining (esqueci como que eh rs)
        return ( oldhash + 1 ) % self.tablesize

    def contains(self, name):
        return self.search(self.slots[self.hash(name)], name) != None
        
    def search(self, values, key):
        index = None
        for i in range(len(values)):
            if values[i].name == key:
                index = i
        return index

    def get(self, key):
        exists = self.contains(key)

        if exists:
            slot = self.hash(key)
            index = self.search(self.slots[slot], key)

            name = self.slots[slot][index].name
            height = str(self.slots[slot][index].height)
            print(f"----- user ----- \n  name: {name} \n  height: {height}")
        else:
            print("the informed user doesn't exist in the database.")

    
    def generatedata():
        pass

if __name__ == '__main__':

    user = User("Synara", 1.63)
    hashtable = HashingTable(5)
    hashtable.put(user.name, user)
    
    user = User("Suelly", 1.63)
    hashtable.put(user.name, user)

    user = User("Suelyl", 1.63)
    hashtable.put(user.name, user)

    user = User("Suelly", 1.63)
    hashtable.put(user.name, user)

    hashtable.get("Suelyl")
