input = ["hello","goodbye","hello"]

def removeDups(values):
    return list(set(values))

print(input,removeDups(input))