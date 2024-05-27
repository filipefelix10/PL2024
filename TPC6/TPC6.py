import re
data = '[1234ALA] 567 89'
pattern = re.compile(r'\[(\d+)(\w+)\]')

s = re.search(pattern,data)

print(s.group(2))