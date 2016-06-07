f = open('sentences.txt','w')

with open('events.txt') as e:
	objects = list(open('objects.txt'))
	relations = list(open('relations.txt')) 
	for line_e in e:
		line_e = line_e.rstrip()
		if ' ' in line_e and '\n' not in line_e:
			if 'lean' in line_e:
				for obj1 in objects:
					for obj2 in objects:
						line_split_e = line_e.split(' ',1)
						print(line_split_e[0]+' '+obj1.rstrip()+' '+line_split_e[1].rstrip()+' '+obj2.rstrip(),file=f)
			else:
				for obj in objects:
					line_split_e = line_e.split(' ',1)
					print(line_split_e[0]+' '+obj.rstrip()+' '+line_split_e[1].rstrip(),file=f)
		elif 'put' in line_e:
			for rel in relations:
				for obj1 in objects:
					for obj2 in objects:
						print(line_e.rstrip()+' '+obj1.rstrip()+' '+rel.rstrip()+' '+obj2.rstrip(),file=f)
		else:
			for obj in objects:
				print(line_e.rstrip()+' '+obj.rstrip(),file=f)

f.close()