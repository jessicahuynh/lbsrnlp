import nltk

tagged = open('tagged.txt','w')

with open('sentences.txt') as f:
	for sentence in f:
		s = sentence.split()
		tags = nltk.pos_tag(s)
		print(tags,file=tagged)

tagged.close()