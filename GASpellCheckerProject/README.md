### Project Overview

 Have you always wondered how google autocorrects your spelling and offers accurate suggestions? Stay on to understand the method behind the madness. The only pre-requisite you need is a willingness to learn (and a little knowledge of probability won't hurt).Before we go any further, first let's understand the problem. The various cases of errors are:

The misspelt word has no meaning. Example typing acrss instead of across (Non-Word Error (NWE))
The misspelt word has meaning thought not what the user originally intended. Example typing feed when you actually wanted to type freed (Real Word Error (RWE))
For the purpose of this error, we will deal with the first kind of errors only i.e. user has misspelt the word in such a way that the misspelt word does not exist in the dictionary. Here you are working on 0643.xml file, which consists of lots of words and phrases.

Why to solve the project?
After completing this project you can able to build the basic level of spell checker module. In this project, you will apply the following concepts.

Text preprocessing
NOTE: The spell checker code that we will be using is a modified version of [Peter Norvig's Spelling Corrector]


### Approach taken to solve the problem

 Convert the text into lower case
The first thing you have to do is to write a function that reads the contents of the files that we have.

Instructions:
Some part of the code is already given to you.

Write a function "words" that :

Takes 'text' as a parameter.

Returns 'text to lower format'



Create the list of all possible words
In this task you need to list down all the possible correct words from the file. suppose you write simple word called beautiful so it will print out all the possible words match with this words. Let's solve the task.

Instructions:
Write a function "edits" that :

Takes 'word' as a parameter.
Create the empty list first_edited_word
Create the empty list second_edited_word
Create the empty list third_edited_word
The word which are coming from function edit store them in variable first_edited_word
Iteration for creating the edits for firsteditedword is given to you.
Repeat the same procedure for the secondeditedword and append the result in the third_edited_word
Returns 'first_edited word','second_edited_word','third_edited_word'





Probability of the word in the file
In the previous task you have predicted the all the possible words. In this task your aim is to find the probability of each word which is listed in the document.

Instructions:
Write a function "probability" that :

Takes 'word' and 'N=sum(WORDS.values())'as a parameter.
Initialize prob_list which stores probability of corresponding word in the word list.
Iterate the loop over word.
find probability of each word by taking ratio of count of that word WORDS[w] and total words in corpus (N) and store the result in variable p_w.
append probability of each word into list prob_list which contain probability of all words.
Returns 'prob_list'



Predicting the correct spelling.
In the last task you are creating the list of all the possible word which are match with the given wrong word. In this task you will be using all the functions which are created before. We will get the corrected result for all the words which are stored in the document. Google trained the large amount to documents so we will get the corrected spelling.

Instructions:
Write a function "correction" that :

Takes 'word' as a parameter.

Get lists of all possible words you can get by making one simple edit and two simple edits in the query word and store it in first_edited_word,second_edited_word and third_edited_word respectively. Use the 'edits()' function we implemented earlier.

From lists found in above step you have to select only correct words, use 'known()' function which takes any list of words and return only known words from vocabulary.

From list 'first_edited_word' and 'second_edited_word' and 'third_edited_word'select only known words using 'known()' function and save it in lists 'known_words_1edit','known_words_2edit' and 'known_words_3edit' respectively. Observe that 'known_word' variable is a list which will contain the query word if it is known in vocabulary and would be empty otherwise.

Using if-else condition you have to implement three possible

conditions (a) return query word itself if it is in vocabulary, so check if length of 'known_word' list is 0, if not zero it means word is in vocabulary and so return it. If it is zero then move to next condition.

(b) if list 'knownwords1edit' is non-empty then you don't need to look further return word with maximum probability in this list in 1st line get probability of all the words in this list in 2nd line get the index with maximum value of probability in 3rd line return word with maximum probability

(c) perform same operation with 'knownwords2edit' and 'knownwords3edit'.

(d) return query word if none of these last four case give a known word

Returns 'word'

print the function correction('swet') and check the result. For the practice you can try other words also.









