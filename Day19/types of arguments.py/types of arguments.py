#Positional arguments
"""def display(name,rollnum):
    print(f"name:{name}")
    print(f"rollnum:{rollnum}")
display("charan",22)
display(43,"nani")

#Keyword arguments
def display(name,rollnum):
    print(f"name:{name}")
    print(f"rollnum:{rollnum}")
display(name="charan",rollnum=22)
display(rollnum=43,name="nani")
#Default arguments
def display(name,email="gmail.com",password=""):
    print(f'name:{name}')
    print(f'email:{email}')
    print(f'password:{password}')
display('xyz','xyz@gmail.com','xyz123')
display('xyz','xyz@gmail.com')

#variable length arguments
def display(*names):
    print(names)
display("charan")
display("sai","charan")
display("sai","chara","nani")
"""

#Keyword length arguments
def display(**products):
    print(products)
display(bag=5000)
display(bag=5000,book=30)
display(bag=5000,book=30,bottle=300)