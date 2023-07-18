from Grocery import grocery
from pickle import *

cart=[]

#myfile=open('departmental store.txt','wb')
#myfile.close()

def readfile():
    try:
        mystore=open('departmental store.txt','rb')
        return load(mystore)
    except EOFError as e: return []

def writefile(what):
    mystore=open('departmental store.txt','wb')
    dump(what,mystore)
    mystore.close()
    print('The stock is updated')

def create():
     product=input('enter the product name: ')
     brand=input('from which brand? ')
     mass=int(input('how many kg? '))
     goods=grocery(product,brand,mass)
 
#read
     cart=readfile() 
#write  
     cart.append(goods)
     writefile(cart)
     
def view():
    cart=readfile()
    for x in cart: 
       print(x)

def update(productname):
    cart=readfile()
    for i in range(len(cart)):
        if cart[i].product==productname:
            qs=input('what would u like to update? ')
            if qs=="mass":
                change=int(input('enter the new mass of the product'))
                cart[i].mass=change
                print('product mass updated')
            elif qs=="brand":
                changed=input('enter the new brand name')
                cart[i].brand=changed
                print('product brand is updated')
            elif qs=="name":
                changes=input('enter the new product name')
                cart[i].product=changes
                print('product name is updated')
           
            writefile(cart)
            return
    else: 
        print(productname, 'not found')    

def delete(productname):
    cart=readfile()
    position=-1
    for s in range(len(cart)):
        if cart[s].product==productname:
            position=s
            break
    if position!=-1:
        cart.pop(position)
        writefile(cart)
    else:
        print("invalid product ",productname)
        



#update('coriander powder')
#create()
#delete("chilli powder")
view()

