S = input()
words = S.split(" ") 
newWords = [word[::-1] for word in words] 
newSentence = " ".join(newWords)
print(newSentence) 
