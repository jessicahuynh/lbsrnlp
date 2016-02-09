import nltk

with open("definitions-pos.txt",'a') as d:
    with open("definitions.txt") as f:
        for line in f:
            if line[0] == "-":
                tokenized = nltk.tokenize.word_tokenize(line[1:]) #don't include the - at the start
                tagged = nltk.pos_tag(tokenized)
                d.write(str(tagged))
                d.write("\n")
            else:
                d.write(str(line))