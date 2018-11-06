import numpy as np
N = 5
#data = np.genfromtxt('shakespeare_sentences.txt')
data = [np.array(line.split()) for line in open('shakespeare_sentences.txt')]
words = {}
for sen in data:
	for word in sen:
		if word in words:
			words[word] +=1
		else:
			words[word] =1
words_sorted = sorted(words, key=words.get, reverse=True)[:N]
print(words_sorted)
l = []
for sen in data:
	mydict = {}
	for i in words_sorted:
		mydict[i]=0
	for word in sen:
		if word in mydict:
			mydict[word] +=1
	print (mydict.values())
