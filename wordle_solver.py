import os

def get_freq(word):
	res_freq = 0
	for i in range(len(word)):
		curr_letter = word[i]
		res_freq += lett_freq_d[(curr_letter, i)]
	return res_freq

lett_freq_d = {('a', 0): 1698, ('b', 0): 1555, ('c', 0): 1512, ('d', 0): 1128, ('e', 0): 693, ('f', 0): 847, ('g', 0): 965, ('h', 0): 844, ('i', 0): 473, ('j', 0): 446, ('k', 0): 789, ('l', 0): 1046, ('m', 0): 1225, ('n', 0): 647, ('o', 0): 532, ('p', 0): 1184, ('q', 0): 93, ('r', 0): 948, ('s', 0): 2206, ('t', 0): 1264, ('u', 0): 420, ('v', 0): 404, ('w', 0): 596, ('x', 0): 36, ('y', 0): 225, ('z', 0): 176, ('a', 1): 4103, ('b', 1): 172, ('c', 1): 338, ('d', 1): 245, ('e', 1): 2863, ('f', 1): 73, ('g', 1): 139, ('h', 1): 927, ('i', 1): 2239, ('j', 1): 32, ('k', 1): 137, ('l', 1): 1193, ('m', 1): 327, ('n', 1): 671, ('o', 1): 3069, ('p', 1): 336, ('q', 1): 25, ('r', 1): 1543, ('s', 1): 341, ('t', 1): 403, ('u', 1): 1824, ('v', 1): 126, ('w', 1): 226, ('x', 1): 83, ('y', 1): 458, ('z', 1): 59, ('a', 2): 1959, ('b', 2): 664, ('c', 2): 701, ('d', 2): 774, ('e', 2): 1421, ('f', 2): 271, ('g', 2): 616, ('h', 2): 334, ('i', 2): 1668, ('j', 2): 81, ('k', 2): 406, ('l', 2): 1603, ('m', 2): 885, ('n', 2): 1757, ('o', 2): 1426, ('p', 2): 560, ('q', 2): 32, ('r', 2): 2201, ('s', 2): 1021, ('t', 2): 1048, ('u', 2): 990, ('v', 2): 417, ('w', 2): 349, ('x', 2): 170, ('y', 2): 381, ('z', 2): 217, ('a', 3): 2214, ('b', 3): 423, ('c', 3): 770, ('d', 3): 829, ('e', 3): 3252, ('f', 3): 278, ('g', 3): 612, ('h', 3): 423, ('i', 3): 1963, ('j', 3): 61, ('k', 3): 628, ('l', 3): 1295, ('m', 3): 612, ('n', 3): 1391, ('o', 3): 1282, ('p', 3): 526, ('q', 3): 5, ('r', 3): 1225, ('s', 3): 945, ('t', 3): 1385, ('u', 3): 899, ('v', 3): 259, ('w', 3): 192, ('x', 3): 26, ('y', 3): 271, ('z', 3): 186, ('a', 4): 2362, ('b', 4): 129, ('c', 4): 300, ('d', 4): 917, ('e', 4): 2679, ('f', 4): 145, ('g', 4): 261, ('h', 4): 654, ('i', 4): 910, ('j', 4): 10, ('k', 4): 502, ('l', 4): 971, ('m', 4): 406, ('n', 4): 1522, ('o', 4): 857, ('p', 4): 285, ('q', 4): 9, ('r', 4): 1190, ('s', 4): 3767, ('t', 4): 1284, ('u', 4): 247, ('v', 4): 41, ('w', 4): 122, ('x', 4): 144, ('y', 4): 2116, ('z', 4): 122}

path = os.path.dirname(os.path.realpath(__file__))
word_list = open(f'{path}\\5 letter words.txt', 'r', encoding='utf-8').read().split('\n')
letters_not_in_l = []
letters_not_in_set = set()
for word in letters_not_in_l:
	for letter in word:
		letters_not_in_set.add(letter)

word = '.....'
letters_must_be_in = []
for i in word:
	if i in letters_not_in_set: letters_not_in_set.remove(i)
for i in letters_must_be_in:
	if i[0] in letters_not_in_set: letters_not_in_set.remove(i[0])
words_available = []
add_pass = False
for possible_word in word_list:
	includes_letters_not_possible = False
	for letter in possible_word:
		if letter in letters_not_in_set:
			includes_letters_not_possible = True
			break
	if includes_letters_not_possible: continue
	add_pass = True
	for pos in range(len(word)):
		if word[pos] != '.' and possible_word[pos] == word[pos]:
			add_pass = True
		if word[pos] != '.' and possible_word[pos] != word[pos]:
			add_pass = False
			break
	for i in letters_must_be_in:
		if i[0] not in possible_word or possible_word[i[1]] == i[0]:
			add_pass = False
			break
	if add_pass: words_available.append(possible_word)
words_available_with_freq = []
for i in words_available:
	words_available_with_freq.append((get_freq(i), i))
words_available_with_freq = list(reversed(sorted(words_available_with_freq)))
for i in words_available_with_freq:
	print(i[1], end=' ')
print()
if len(words_available) > 200: print('More than 200 words possible')
