from Tests import DFA_test

set1 = set( {'a','b'})
set2 = set ({'a','b','c'})

set3 = set()
for i in set1:
    print(i)
    for j in set2:

        set3.add(i+j)
    
print(set3)