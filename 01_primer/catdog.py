chars = ['c','a','t','d','o','g']
def catdog(chars):
    if len(chars) == 0:
        return [""]
    else:
        last = chars.pop()
        prev = catdog(chars)
        result = []
        for item in prev:
          i = 0
          while i <= len(item):
              result.append(item[:i] + last + item[i:])
              i += 1
        return result

print(catdog(chars))
print(len(catdog(chars)))


"""
from itertools import permutations
s = 'catdog'
perms = permutations(s)
res = []
for x in perms:
    res.append(''.join(x))
print(len(res))
"""
