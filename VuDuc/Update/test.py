import os
import json
 
# Opening JSON file
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Profile.json")

f = open(path)
profile = json.load(f)
print(my_path)


# dirname = os.path.dirname(__file__)
# filename = os.path.join(dirname, 'relative/path/to/file/you/want')
# print('..')
# print(filename)
