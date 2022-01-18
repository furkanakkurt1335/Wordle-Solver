# Wordle-Solver
This solver helps in solving the word game 'Wordle'. The game link is [here](https://www.powerlanguage.co.uk/wordle/).  

#### The solver variables:  
* ```'letters_not_in_l'``` variable should be changed according to the letters that are established not to be in the word at all. If one entered the word 'slick' and the 'c' was in the correct position but the others were not to be in the word, then one must append ```'slik'``` to the list.  
Example: ```letters_not_in_l = ['tred', 'swzz', 'log']```  
* ```'letters_must_be_in'``` variable should be changed according to the letters that are established to be in the word but in another position.  
Example: ```letters_must_be_in = [('a', 1), ('t', 2)]```  
* ```'word'``` variable should be changed according to the established positions of letters (greens).  
Example: ```word = '.a.ic'```  

The data in the file 'Mystery Word List.txt' is taken from the words used in the js script file to construct the puzzle.  

The best word to start the game with is *SLATE*. The frequencies out of the word-list file are used in calculation.