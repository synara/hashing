from hashing import HashingTable
from user import User

def menu():
    print("---------- MENU ----------")
    print("1. generate data \n2. constains user\n3. find user\n4. show users")  
    return int(input("choose one of the options: "))


def alert():
    print("there's not users on the base. firstly, generate data.")
    
      
if __name__ == '__main__':
    
    generates = False
    option = menu()
    tablesize = 0
    hashtable = HashingTable(tablesize)

    if option == 1: 
        tablesize = int(input("how many users should be created? "))
        hashtable = HashingTable(tablesize)
        hashtable.generatedata()
        generates = True
    
    elif  option == 2:
        if generates:
            key = input("enter the user name: ")
            exists = hashtable.contains(key)
        
            if exists:
                print("the requested user exists in the database.")
            else: 
                print("the informed user doesn't exist in the database.")
        else: 
            alert()

    elif option == 3:
        if generates:
            key = input("enter the user name: ")
            hashtable.get(key)
        else: 
            alert()

    elif option == 4:
        if generates: 
            hashtable.showusers()
        else: 
            alert()
    
    while True:
        n = input('continue? [y/n] ')
        if n == "y":
            option = menu()
            if option == 1: 
                tablesize = int(input("how many users should be created? "))
                hashtable = HashingTable(tablesize)
                hashtable.generatedata()
                generates = True
        
            elif option == 2:
                if generates:
                    key = input("enter the user name: ")
                    exists = hashtable.contains(key)
                    if exists:
                        print("the requested user exists in the database.")
                    else: 
                        print("the informed user doesn't exist in the database.")
                else: 
                    alert()

            elif option == 3:
                if generates:
                    key = input("enter the user name: ")
                    hashtable.get(key)
                else: 
                    alert()

            elif option == 4:
                if generates: 
                    hashtable.showusers()
                else: 
                    alert()
        else:
            exit()

 