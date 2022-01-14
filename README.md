# Wordle-Solver
This solver helps in solving the word game 'Wordle'.  

#### The solver variables:  
* 'letters_not_in_l' variable should be changed according to the letters that are established not to be in the word at all. If one entered the word 'slick' and the 'c' was in the correct position but the others were not to be in the word, then one must append 'slik' to the list.
Example: letters_not_in_l = ['tred', 'swzz', 'log']  
* 'letters_must_be_in' variable should be changed according to the letters that are established to be in the word but in another position.  
Example: letters_must_be_in = [('a', 1), ('t', 2)]
* 'word' variable should be changed according to the established positions of letters (greens).  
Example: word = '.a.ic'  

The data in the file '5 letter words.txt' is taken from the Collins Dictionary.  

Best word to start the game is 'AEONS', using the frequencies out of the word-list file.  
