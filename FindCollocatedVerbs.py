import sys

f = open(sys.argv[1])
for line in f.readlines():
	t = line.split()
	if t[2].startswith("NN"):
		print "\t".join(t)
