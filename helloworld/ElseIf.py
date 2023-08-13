import re
pattern = '[a-z]+'
string = '-----2344-Hello--World!'
result = re.search(pattern, string)
print(result)
print(result.group())
