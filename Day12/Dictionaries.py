bus={'s1':'Booked','s2':'Available','s3':'Available','s4':'Booked','s5':'Available'}
for i in bus:
    if bus.get(i)=='Available':
        print(i,bus.get(i))