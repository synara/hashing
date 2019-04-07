from hashing import HashingTable
from user import User

if __name__ == '__main__':

    user = User("Suelly", 1.63)
    hashtable = HashingTable(5)
    hashtable.put(user.name, user)


    """generates = False
    print("---------- MENU ----------")
    print("1. generate data \n2. find user")  
    option = int(input("choose one of the options: "))
    tablesize = 0
    hashtable = HashingTable(tablesize)


    if option == 1: 
        tablesize = int(input("how many users should be created? "))
        generates = True
        hashtable = HashingTable(tablesize)
        hashtable.generatedata()
    
    elif option == 2:
        if generates:
            key = input("enter the user name: ")
            hashtable.get(key)
        else: 
            print("there's not users on the base. firstly, generate data.")"""
            
 

      

