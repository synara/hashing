class User(object):
    def __init__(self, name, height):
        self.name = name
        self.height = height

class Hashingtable(object):
    def __init__(self, tablesize):
        self.tablesize = tablesize
        self.list = [None] * self.tablesize
        self.buildslots(self.tablesize)

    def buildslots(self, listsize):
        for i in range(0, listsize):
            self.list[i] = []

    def hash(self, astring):
        sum = 0
        for pos in range(len(astring)):
            sum += ord(astring[pos])
            
        return sum % self.tablesize

    def put(self, key, user):
        index = self.hash(key)
        

    def contains(self, name):
        pass
    
    def get(self, key):
        pass

if __name__ == '__main__':
    user = User("synara", 1.63)
    hashtable = Hashingtable(5)
    hashtable.put(user.name, user)
