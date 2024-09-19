import random

def gen_mn():
    set1 = set(random.sample(range(1, 50), 10))  
    set2 = set(random.sample(range(1, 50), 10))  
    
    print("Множина 1:", set1)
    print("Множина 2:", set2)
    
    intersection = set1.intersection(set2)
    
    if intersection:
        print("Елементи, які входять в обидві множини:", intersection)
    else:
        print("Немає спільних елементів.")

#
gen_mn()
