def count_division(num):
    count = 0
    if num < 2:
        return count
    else:
        while num >= 2:
            num = num // 2
            count += 1
        return count


print(count_division(4))
print(count_division(2))
print(count_division(5))
print(count_division(16))
