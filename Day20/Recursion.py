def display(n): 
    if n>10:
        return 
    print(n)
    display(n+1)
display(1)