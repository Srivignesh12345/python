from list import *
print("Welcome to Amazon grocery")

while True:
    print("1. New Stock\n2. Update existing\n3.Delete\n4.View all\n5. Exit")
    operation=int(input("Enter the number to perform respective process "))
    if operation==1:
        create()
    elif operation==2:
        proName=input("Enter the product name to update")
        update (proName)
    elif operation==3:
        proName=input("Enter the product name to delete")
        delete(proName)
    elif operation==4:
        view()
    else:
        print("Invalid operation")
        break