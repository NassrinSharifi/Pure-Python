"""first method"""
n, p, q = map(int, input().split())
words = []
num_of_similars = 0
for i in range(n):
    word = input()
    words.append(word)
for word_1 in words:
    for word_2 in words:
        if word_1[:p] == word_2[:p] and word_1[-q:] == word_2[-q:]:
            # print(word_1 , word_2)
            num_of_similars += 1
num_of_similars = int((num_of_similars - len(words)) / 2)
print(len(words) - num_of_similars)

# second method
# for i in range(n):
#     word = input()
#     words.append(word)
# for word_1 in words:
#     for word_2 in words[:words.index(word_1)] + words[words.index(word_1) + 1:]:  # a list without word_1
#         if word_1[:p] == word_2[:p] and word_1[-q:] == word_2[-q:]:
#             num_of_similars += 1
# num_of_similars = int(num_of_similars / 2)
# print(len(words) - num_of_similars)
