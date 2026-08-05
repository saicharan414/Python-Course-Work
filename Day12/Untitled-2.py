fa=eval(input("Follows Account: "))
cf=eval(input("CLse Friend: "))
if fa:
    if cf:
        print("Story Visible")
    else:
        print("Not in close Friends List")
else:
    print("Follow theAccount First")