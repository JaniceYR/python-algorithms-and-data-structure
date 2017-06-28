def count_word(string):
    words = string.split()
    word_count = {}
    for word in words:
        word_count[word] = 0

    for word in words:
        word_count[word] += 1

    return word_count


print(count_word("I I I I am Janice janice Janice kaka kaka ka"))
