from user import User
import random
import string
import sys

class HashingTable(object):
    def __init__(self, tablesize):
        self.tablesize = tablesize
        self.slots = [[User]] * self.tablesize

    def hash(self, key):
        sum = 0
        for pos in range(len(key)):
            sum += ord(key[pos]) * pos
            
        return sum % self.tablesize

    def put(self, key, user):
        hashindex = self.hash(key)

        if self.slots[hashindex] == [User]:
            self.slots[hashindex] = []
            self.slots[hashindex].append(user)
        else: 
            indexvalues = len(self.slots[hashindex])

            #refatorar depois usando o search/contains
            for i in range(indexvalues):
                name = self.slots[hashindex][i].name
                if self.slots[hashindex][i].name != key: 
                    newhashindex = self.chaining(hashindex)
               
                    #esse while procura um novo hash index enquanto ele for igual a chave ou o slot nao estiver vazio
                    #gera um loop quando tento inserir um numero de usuarios maior que o tanto de slots - perguntar ao professor
                    while self.slots[newhashindex] != [User] and self.slots[newhashindex][i].name != key:
                        newhashindex = self.chaining(newhashindex)

                    if self.slots[newhashindex] == [User]:
                        self.slots[newhashindex] = []
                        self.slots[newhashindex].append(user)
                    else:
                        self.slots[newhashindex].append(user)
                else:
                    self.slots[hashindex] = user 
                   
            
    def chaining(self, currentindex):
        #reprogramar usando a tecnica de chaining (esqueci como que eh rs)
        newindex = currentindex + 1    
        return newindex if (newindex <= (self.tablesize - 1)) else (newindex % self.tablesize)

    def contains(self, name):
        return self.search(self.slots[self.hash(name)], name) != None
        
    def search(self, values, key):
        index = None
        for i in range(len(values)):
            if values[i].name == key:
                index = i
        return index

    def showusers(self):
        for i in range(self.tablesize):
            if self.slots[i] != [User]:
                print(f"key: {i}")
                for j in range(len(self.slots[i])):
                    print(f"  name: {self.slots[i][j].name} \n  height: {self.slots[i][j].height}\n")


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

    
    def generatedata(self):
        vowels = "aeiou"
        consonants = "".join(set(string.ascii_lowercase) - set(vowels))
        
        for i in range(self.tablesize):
            namesize = random.randint(3, 18)
            name = ""
            for n in range(namesize):
                if n % 2 == 0:
                    name += random.choice(consonants)
                else:
                    name += random.choice(vowels)
                
            user = User(name, round(random.uniform(1,2),2))
            self.put(name, user) 