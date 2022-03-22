# https://projecteuler.net/problem=42

from Maps import ALPHABET_MAP

def get_triangle_num(n):
    return (n/2)*(n+1)

with open("p042_words.txt", "r") as words_file:
    words = words_file.readline().split(',')
    count = 0
    for word in words:
        word_num = 0
        word = word.replace("\"", "")
        for l in word:
            word_num += ALPHABET_MAP[l]
        i = 1
        triangle_num = get_triangle_num(i)
        while triangle_num <= word_num:
            if word_num == triangle_num:
                print(word, word_num)
                count += 1
            i += 1
            triangle_num = get_triangle_num(i)

print('total triangle words: {0}'.format(count))