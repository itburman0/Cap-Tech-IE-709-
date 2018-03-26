#List Comprehensions

sentence = "the quick Blue Dragon Flies over the fat hippo"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)

#Ending Exercise

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7, 45.8, 76.3]
newlist = [int(x) for x in numbers if x > 0]
print(newlist)

#I noticed that it gets rid of the decimal numbers and rounding is omitted. 