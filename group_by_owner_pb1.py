def group_by_owner(files):
    result = {}
    for file,owner in files.items():
        result[owner] = result.get(owner,[]) + [file]
    return result

files = {
        'Input.txt': 'Randy',
        'Code.py': 'Stan',
        'Output.txt': 'Randy'

        }
# files = {}
# numberofrecords = int(input("please enter the number of records"))
# for _ in range(numberofrecords):
#     files[input()] = input()
print(group_by_owner(files))