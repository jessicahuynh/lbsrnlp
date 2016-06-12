import sys, argparse

def parse_sent(s):
	form = s[0] + '('
	for i in range(1,len(s)):
		if s[i] in relations:
			form = form + ',' + s[i] + '('
		elif (s[i] == 'in' and s[i+1] == 'front' and s[i+2] == 'of'):
			form = form + ',in_front_of('
		elif s[i] == 'left' and s[i+1] == 'of':
			form = form + ',left_of('
		elif (s[i] == 'right' and s[i+1] == 'of'):
			form = form + ',right_of('
		elif s[i] in objects:
			form = form + s[i]
		elif s[i] == 'paper' and s[i+1] == 'sheet':
			form = form + 'paper_sheet'
		elif s[i] == 'edge':
			form = form + 'edge'
		elif s[i] == 'center':
			form = form + 'center'

	form = form + ')'
	if ',' in form:
		form = form + ')'
	return form

if __name__ == '__main__':
	# command line arguments
	parser = argparse.ArgumentParser(description='Creates functional forms from sentences (either POS tagged or not)',epilog='No arguments will attempt to transform a sentences.txt file that has no POS tagging')

	parser.add_argument('sentence', nargs='?', help='transform a single sentence',default=None)
	parser.add_argument('-p','--pos', help='take into account POS tags', action='store_true')
	parser.add_argument('-i', '--input', help='specify input file', nargs='?', type=str, default=None)

	args = vars(parser.parse_args())
	print(args)
	
	# get events, objects, relations
	events = list(open('events.txt'))
	events = [x.strip() for x in events]

	objects = list(open('objects.txt'))
	objects = [x.strip() for x in objects]

	relations = list(open('relations.txt'))
	relations = [x.strip() for x in relations]
	relations.append('against')
	relations.append('at')

	# handle the arguments
	if not args['pos']:
		if args['sentence']:
			# no pos tags, one sentence
			print(parse_sent(args['sentence'].split()))
		else:
			# no pos tags, all of a file
			forms = open('functional_forms.txt','w')

			if not args['input']:
				args['input'] = 'sentences.txt'

			with open(args['input']) as f:
				for sentence in f:
					s = sentence.split()
					
					print(parse_sent(s),file=forms)

			forms.close()
	elif args['pos']:
		if args['sentence']:
			# pos tags, one sentence
			print('pos the one sentence')
		elif args['input']:
			# pos tags, given input file
			print('pos ' + args['input'])
		else:
			# pos tags, sentences.txt
			print('pos sentences.txt')