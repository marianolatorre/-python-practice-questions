passing = (
    ([1,2,3],3),
    ([1,1,1],2),
    ([2,1,1],3),
    ([1,1],2),
    ([1,2,3],4),
    ([0,0],0),
    ([1,2,3,4,5,6,7,8],15),
)

notPassing = (
    ([0,0],1),
    ([1,1,1],1),
    ([1,1,1],3),
    ([1,2,3,4,5,6,7,8],16),
)

def sumEqualsInput(elements, total) -> bool:
    #print(elements, total)
    for i, value_i in enumerate(elements):
        if total - value_i in elements[i+1:]:
            return True
    return False

print("passing")
for test in passing:
    print(sumEqualsInput(test[0],test[1]))

print("not passing")
for test in notPassing:
    print(sumEqualsInput(test[0],test[1]))