from hashing import HashingTable
from user import User

def menu():
    print("---------- MENU ----------")
    print("1. generate data \n2. find user\n3. show users")  
    return int(input("choose one of the options: "))

def options(option, tablesize, hashtable):
    generates = False
    
      
if __name__ == '__main__':
    
    option = menu()
    tablesize = 0
    hashtable = HashingTable(tablesize)

    if option == 1: 
        tablesize = int(input("how many users should be created? "))
        hashtable = HashingTable(tablesize)
        hashtable.generatedata()
        generates = True
        hashtable.showusers()
    
    elif option == 2:
        if generates:
            key = input("enter the user name: ")
            hashtable.get(key)
        else: 
            print("there's not users on the base. firstly, generate data.")
    
    elif option == 3:
        if generates: 
            hashtable.showusers()
        else: 
            print("no data has been generated, so there are no users to view.")
    print("\n\n")
    
    while True:
        n = input('continue? [y/n] ')
        if n == "y":
            option = menu()
            if option == 1: 
                tablesize = int(input("how many users should be created? "))
                hashtable = HashingTable(tablesize)
                hashtable.generatedata()
                generates = True
                hashtable.showusers()
            elif option == 2:
                if generates:
                    key = input("enter the user name: ")
                    hashtable.get(key)
                else: 
                    print("there's not users on the base. firstly, generate data.")
    
            elif option == 3:
                if generates: 
                    hashtable.showusers()
                else: 
                    print("no data has been generated, so there are no users to view.")
        else:
            exit()

 