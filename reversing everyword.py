Sentence = input()
words = Sentence.split(" ") 
newWords = [word[::-1] for word in words] 
newSentence = " ".join(newWords)
print(newSentence) 
