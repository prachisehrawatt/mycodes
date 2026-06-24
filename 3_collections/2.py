'''The Word Frequency Analyzer (Beginner) You have a block of text and need to figure out which words are used most often.

Task: Write a function word_frequencies(text) that takes a string as input, converts it to lowercase, removes basic punctuation
 (like periods and commas), and returns a Counter object showing the frequency of each word.

Sample Input: "Python is great. Python is dynamic, and Python is easy to learn." 

Expected Output: Counter({'python': 3, 'is': 3, 'great': 1, 'dynamic': 1, 'and': 1, 'easy': 1, 'to': 1, 'learn': 1})
'''
from collections import Counter

lst = "Python is great. Python is dynamic, and Python is easy to learn."
a = Counter(lst.split())
print(a)