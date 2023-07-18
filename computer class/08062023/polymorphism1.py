'''class sam:
    def aa(self,a):
        print(a)
    def aa(self,a,b):
        print(a+b)
    def aa (self,a,b,c):
        print(a+b+c)
s=sam()
s.aa(10,20)'''

'''class over:
    def load(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
O=over()   
print("Sum",o.load(10)) 
print("Sum1",o.load(10,20))
print("Sum",o.load (10,20,30))'''

class multiple:
    def add(self,*args):
        sum=40
        for i in args:
            sum+=i
            print("add values",sum) 

m=multiple()
m.add(40,50)
m.add(40,50,100)
m.add(40,50,100,200)
m.add(10,20,60,100,150)