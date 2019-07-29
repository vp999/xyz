### Project Overview

 The Primetime Emmy Award is an American award bestowed by the Academy of Television Arts & Sciences in recognition of excellence in American primetime television programming. They are considered television's equivalent to the Academy Awards(Oscars). In this project we will try to do some POS analysis on the show/series nominees over the years.

About the dataset
The dataset contains all the nominees for the different categories from 1947 to 2017. 

The dataset has details of 15289 nominees with following 4 features:

Feature	Description
year	Year the award show was conducted
category	The category the award was honoring the nominee for
winner	Binary value showing if the nominee won the award(0: Didn't win, 1: Won)
nominee	The nominee details





### Approach taken to solve the problem

 **POS tagging**
In our first task, we will load data and assign the POS tags to the title of the television shows/series

Instructions
Load data from the path and save it in a dataframe called 'df'

Split the names of the column nominee using "split()" method and map the same with "pos_tag()" method of nltk library and store the final result in 'tagged_titles'

Print 'tagged_titles' to see POS tagged show/series

Create a dataframe called 'tagged_titles_df' from 'tagged_titles' using "pd.DataFrame()"



**Most Frequent tags**
Let's see which are the most frequent tags present in the emmy nominated series/shows.

Instructions
We have already given you the pre execution code

Map the values of nominee column of 'tagged_titles_df' with "count_tags()" function(already defined) and save the result in a new column of 'tagged_titles_df' called 'tag_counts' (i.e. tagged_titles_df ['tag_counts'])

'tag_set' contains list of all possible tags is already given along with creation of tag column frequency for each tags.

Print 'tagged_titles_df' to see how the new dataframe looks

Create a subset of 'tagged_titles_df containing all the tags(i.e. tag_set) and store it in 'top_pos'

Apply "sum()" function on "top_pos" and save it back to 'top_pos'

Apply "sort_values()" function on "top_pos", take the last 10 values(which will be the top 10 most frequent POS tags) and save it back to 'top_pos'.

Plot the barplot of 'top_pos' to see the top 10 POS tags in emmy nominated shows/series

 


**POS that nominates!**
Let's find out having which verb gives you the best chance of being nominated?

Instructions
A vocabulary dictionary has been created for you called 'vocab'

Create a dataframe from 'vocab' using "pd.DataFrame.from_dict()" method and store it in a variable called 'vocab_df'. Add 'orient=Index' as parameter to the above method to make the POS tags as the columns.

Fill all the na values in 'vocab_df' with 0

Create a subset dataframe called 'top_verb_nominee' which stores the rows containing top 10 values for the tag 'VBG'

Plot the barplot of 'top_verb_nominee' to see the top 10 verbs in emmy nominated shows/series

Create a subset dataframe called 'top_noun_nominee' which stores the rows containing top 10 values for the tag 'NN'

Plot the barplot of 'top_noun_nominee' to see the top 10 nouns in emmy nominated shows/series








**Funny Winners**
In this task we will try to deduct having what proper nouns lead to a higher chance of comedy shows/series winning

Instructions:
Subset the dataframe 'df' to contain only those shows that have won and shows that are nominated in a category having 'Comedy' in it. Save the subsetted dataframe in 'new_df'

Split the names of the column nominee of 'new_df', map them with "pos_tag()" method of nltk library and store the final result in 'tagged_titles_winner'

Print 'tagged_titles_winner' to see POS tagged show/series

Create a dataframe called 'tagged_titles_winner_df' from 'tagged_titles_winner' using "pd.DataFrame()"

A vocabulary dictionary has been created for you called 'vocab'

Create a dataframe from 'vocab' using "pd.DataFrame.from_dict()" method and store it in a variable called 'vocab_df'. Add 'orient=Index' as parameter to the above method to make the POS tags as the columns.

Fill all the na values in 'vocab_df' with 0

Create a subset dataframe called 'top_proper_noun_nominee' which stores the rows containing top 5 values for the tag 'NNP'

Plot the barplot of 'top_verb_nominee' to see the top 5 proper nouns in emmy winning shows/series


