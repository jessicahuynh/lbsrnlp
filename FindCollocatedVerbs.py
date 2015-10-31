import os
import glob

d = {}
sentences = []

path = 'MASC-3.0.0/original-annotations/Penn_Treebank/'
listing = os.listdir(path)

for filename in listing:
	f = open(path+filename)
	# get sentences
	sentence_part = ""
	for line in f.readlines():
		t = line.split()
		
		if len(t) > 2 and t[0] == "(":
			sentences.append(sentence_part)
			sentence_part = '\t'.join(t)
		else:
			sentence_part = sentence_part + " " + "\t".join(t)
		
	del sentences[0]
	
	f.close()
	
	# get the verbs and nouns
	for line in sentences:
		# nouns in the sentence
		sentence_nouns = []
		
		t = line.split()
		for i in range(len(t)):		
			if len(t) > 2 and (t[i].startswith("(NN") or t[i].startswith("NN")) and not t[i].startswith("(NNP"):
				# get noun
				noun = t[i+1].strip("))").lower()
				sentence_nouns.append(noun)
				if noun not in d:
					d[noun] = {}
				
		#print sentence_nouns
		
		for j in range(len(t)):
			# verb stuff here
			if len(t) > 2 and (t[j].startswith("(VB")):
				verb = t[j+1].strip(")").lower()
			
				for n in sentence_nouns:
					counts = d[n]
					if verb in d[n]:
						counts[verb] = counts[verb] + 1
					else:
						counts[verb] = 1
					d[n] = counts
					
	print "finished " + filename + "!"

output = open("collocations.txt","w")
for noun in d:
	output.write(' '.join((noun, ' ', str(d[noun]), '\n')))
output.close()

print "done!"