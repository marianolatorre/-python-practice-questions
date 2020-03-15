input = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

output={'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}




def group_by_owners(files):
    result = {}
    for file in files:
        owner = files[file]
        result[owner]= result.get(owner,[]) + [file]
    return result

print(group_by_owners(input))
