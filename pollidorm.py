def pollidorm(name):
    length=len(name)-1
    for index in range(length):
        if name[index]==name[length - index]:
            return True
    return False
print(pollidorm("raceca"))
#index of first will be [0] so how do we make [-1] total length - 1 gives index now is [0] = [5] we have to iterate when the index increases from from it should decrease from the back so [length - index] [5-1]=4 checking is 4==1 worka


def pollidorm(name):
    if name==name[::-1]:
            return True
    return False

print(pollidorm("racecar"))
