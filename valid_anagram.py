def validanagram( s, t):
    if len(s)!=len(t):
        return False
    storage={}
    for i in s:
        if i in storage:
            storage[i]+= 1
        else:
            storage[i]=1
            
    for j in t:
       if j not in storage or storage[j]==0:
           return False
       else:
           storage[j]-=1
           
    return True       
print("Test 1 (anagram):", validanagram("anagra", "nagaram")) # Expected: True
print("Test 2 (rat/car):", validanagram("rat", "tar"))         # Expected: False
print("Test 3 (ab/a):", validanagram("ab", "a"))    