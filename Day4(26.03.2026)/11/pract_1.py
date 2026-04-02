import re

string = "Текст. Который написал я! Или не я?"

result = re.split(r'[.!?]\s*',string)

for part in result:
    print(part)


