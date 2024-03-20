import pandas as pd
import re

#grabbing database of words
!git clone https://github.com/fordsfords/moby_words_2


#refining set (removing words containing s, adding a spot for length in order to drop all words less than 4 letters)
alph=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

sblist=pd.read_csv("/content/moby_words_2/crosswd.txt")

sblist.columns=['words']

sbdict=sblist.dropna()

sbdict=sbdict[~sbdict['words'].str.contains('s')]

sbdict['length']=sbdict.words.str.len()
sbdict=sbdict[sbdict.length>=4]
sbdict=sbdict[sbdict.length<=22] #feels like a reasonable one (longest word in spelling bee history)

#solving
#alternative solution
sblist=pd.read_csv("/content/moby_words_2/crosswd.txt")

sblist.columns=['words']

sbdict=sblist.dropna()

sbdict=sbdict[~sbdict['words'].str.contains('s')]

sbdict['length']=sbdict.words.str.len()
sbdict=sbdict[sbdict.length>=4]
sbdict=sbdict[sbdict.length<=22] #feels like a reasonable one

middle=input("Type the middle letter   ")

loop=sbdict.dropna()


other=input("Type the other letters     ")
letters=set(other+middle)

answers=[]

for i in loop.words:
  word=set(i)
  if word.issubset(letters):
    answers.append(i)
