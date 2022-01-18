import os, json

def get_freq(word):
	res_freq = 0
	for i in range(len(word)):
		curr_letter = word[i]
		res_freq += lett_freq_d[curr_letter][str(i)]
	return res_freq

path = os.path.dirname(os.path.realpath(__file__))
lett_freq_d = json.load(open(f'{path}\\mystery-word-list-letter-frequencies.json', 'r', encoding='utf-8'))
word_list = open(f'{path}\\Mystery Word List.txt', 'r', encoding='utf-8').read().split('\n')
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
