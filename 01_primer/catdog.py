chars = ['c','a','t','d','o','g']
def catdog(chars):
    # print("what?????")
    if len(chars) == 0:
        return [""]
    else:
        last = chars.pop()
        prev = catdog(chars)
        result = []
        print(prev)
        for item in prev:
          i = 0
          while i <= len(item):
              result.append(item[:i] + last + item[i:])
              i += 1
        return result

print(len(chars))
print(len(catdog(chars)))
