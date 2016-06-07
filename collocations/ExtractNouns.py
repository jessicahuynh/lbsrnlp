import sys

f = open(sys.argv[1])
for line in f.readlines():
 	t = line.split()
	for i in range(len(t)):
		if len(t) > 2 and (t[i].startswith("(NN") or t[i].startswith("NN")) and not t[i].startswith("(NNP"):
			print "\t".join(t)
			print t[i+1].strip("))")
