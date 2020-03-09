# Write a function to return if two words are exactly "one edit" away, where an edit is:
#  - Inserting one character anywhere in the word (including at the beginning and end)
#  - Removing one character
#  - Replacing exactly one character
#  assumption: no spaces used in input
# 
#  A - B = 0 ==> max one swap
#  A -B = 1 ==> one deletion
#  A- B = -1 ==> one addition

passing = (
    ("", ""),
    ("a", "a"),
    ("hello", "hello"),
    ("hello", "helo"),
    ("hello", "hell"),
    ("hello", "ello"),
    ("hello", "helo")
)
    
notPassing = (
        ("hello","hel"),
        ("hello","heo"),
        ("hello","llo"),
        ("hello","hlo"),
        ("hello",""),
        ("hello","hallu")
)

def distance(a, b, allowed_diff):
    if allowed_diff < 0:
        return False

    len_a=len(a)
    len_b=len(b)
    diff=abs(len_a - len_b)
    # print (a,b,len_a,len_b,diff)
    if diff > allowed_diff:
        return False

    next_a="" 
    next_b=""

    if len_a > 0:
        next_a=a[0]
    if len_b > 0:
        next_b=b[0]

    if len(next_a) == 1 and len(next_b) == 1:
        if next_a == next_b:
            return distance(a[1:], b[1:], allowed_diff)
        else:
            return distance(a, b[1:], allowed_diff-1) or distance(a[1:], b, allowed_diff-1)

    
    return True


print("Passing")
for testcase in passing:
    print(distance(testcase[0],testcase[1],1))
print("\n\nNot Passing")
for testcase in notPassing:
    print(distance(testcase[0],testcase[1],1))
