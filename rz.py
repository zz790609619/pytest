import re

z = 'helosamqw213e1+2sad/m+'
r = re.search(r'(h.*w)([0-9]+e1)(\+.*\+)', z)
print(r.group(3))

