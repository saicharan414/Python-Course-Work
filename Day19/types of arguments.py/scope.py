"""def display(n):
    n=n+10
    print("Inside: ",n)
n=10
display(n)
print("outside: ",n)


def display():
    global n
    n+=10
    print("Inside: ",n)
display()
print("Outside: ",n)


#updating with Gloabl variable
def display():
    global n
    n="PFS"
    print("updated Course:",n)
n="JFS"
display()
print("Final Course:",n)

#without using Gloabl variable

def display():
    n="PFS"
    print("updated Course:",n)
n="JFS"
display()
print("Final Course:",n)


#Using Non local 
#The nonlocal keyword is used when you have a function inside another function, and the inner function wants to change a variable from the outer function.
def display():
    n="JFS"
    def update():
        nonlocal n
        n="PFS"
        print("updated course:",n)
    update()
    print("final course:",n)
"""
