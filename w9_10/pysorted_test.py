import sys

with open(sys.argv[1], "r") as word_list:
    words = list(word_list)

alph_sorted_list = sorted(words)

len_sorted_list = sorted(alph_sorted_list, key=len)
print(len_sorted_list)



strs = ['cccc', 'aaaa', 'd', 'bb', 'bbbb']
strs.sort()

print(sorted(strs, key=len))

