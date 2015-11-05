import os
import glob

def strip_parenthesis(L):
	new_list = []
	for item in L:
		i = item.strip("(").strip(")")
		if not i.isupper():
			new_list.append(i)
		else:
			if i is "I":
				new_list.append(i)
	return new_list

d = {}
sentences_annotated = []
sentences_bare = []

path = 'MASC-3.0.0/original-annotations/Penn_Treebank/'
listing = os.listdir(path)

for filename in listing:
	f = open(path+filename)
	# get sentences
	sentence_part = ""
	sentence_part_bare = ""
	for line in f.readlines():
		t = line.split()
		stripped = strip_parenthesis(t)
		
		if len(t) > 2 and t[0] == "(":
			sentences_annotated.append(sentence_part)
			sentence_part = '\t'.join(t)
			
			sentences_bare.append(sentence_part_bare)
			sentence_part_bare = ' '.join(stripped).strip()
		else:
			sentence_part = sentence_part + " " + "\t".join(t)
			sentence_part_bare = sentence_part_bare + " " + ' '.join(stripped)
		
	del sentences_annotated[0]
	del sentences_bare[0]
	
	f.close()
		
	print "finished " + filename + "!"

output = open("sentence_annotated.txt","w")
for s in sentences_annotated:
	output.write(s)
	output.write('\n')
output.close()

# get rid of double punctuation
fixed_sentences_bare = []
for s in sentences_bare:
	fixed_sentences_bare.append(s.replace(", ,",",") \
		.replace("`` ","") \
		.replace("'' ","") \
		.replace(". .",".") \
		.replace(", ;",";") \
		.replace(": ...","") \
		.replace(". !","") \
		.replace(". :","") \
		.replace("$ $","$") \
		.replace(". .",".") \
		.replace(". ,",",") \
		.replace(". ?","?") \
		.replace(": --","--") \
		.replace(": :",":") \
		.replace("(,",",") \
		.replace("(.","."))	

output2 = open("sentence_bare.txt","w")
for s in fixed_sentences_bare:
	output2.write(s)
	output2.write('\n')
output2.close()

print "done!"