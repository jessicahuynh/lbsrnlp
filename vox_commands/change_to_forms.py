import sys, argparse, ast

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

	return close_form(form)

def parse_pos(tagged):
	form = ""

	i = 0
	while i < len(tagged):
		word, pos = tagged[i]
		
		if 'VB' in pos:
			form = form + word + '('
		elif pos == 'IN' and word == 'in' and tagged[i+1][0] == 'front' and tagged[i+2][0] == 'of':
			form = form + ',in_front_of('
			i = i + 2
		elif tagged[i][0] == 'left' and tagged[i+1][0] == 'of' and 'IN' in tagged[i+1][1]:
			form = form + ',left_of('
			i = i + 1
		elif tagged[i][0] == 'right' and tagged[i+1][0] == 'of' and 'IN' in tagged[i+1][1]:
			form = form + ',right_of('
			i = i + 1
		elif 'IN' in pos:
			form = form + ',' + word + '('
		elif 'NN' in pos and i < len(tagged) - 1 and tagged[i+1][1] == 'NN':
			form = form + word + '_' + tagged[i+1][0]
			i = i + 1
		elif 'NN' in pos:
			form = form + word

		i = i + 1
	
	return close_form(form)

def close_form(form):
	form = form + ')'
	for i in range(form.count(',')):
		form = form + ')'
	return form

if __name__ == '__main__':
	# command line arguments
	parser = argparse.ArgumentParser(description='Creates functional forms from sentences (either POS tagged or not)',epilog='No arguments will attempt to transform a sentences.txt file (without --pos) or a tagged.txt file (with --pos)')

	parser.add_argument('sentence', nargs='?', help='transform a single sentence',default=None)
	parser.add_argument('-p','--pos', help='take into account POS tags', action='store_true')
	parser.add_argument('-i', '--input', help='specify input file', nargs='?', type=str, default=None)
	parser.add_argument('-o', '--output', help='specify output file', nargs='?', type=str, default='functional_forms.txt')

	args = vars(parser.parse_args())
	print(args)
	
	# handle the arguments
	if not args['pos']:
		# get events, objects, relations
		events = list(open('events.txt'))
		events = [x.strip() for x in events]

		objects = list(open('objects.txt'))
		objects = [x.strip() for x in objects]

		relations = list(open('relations.txt'))
		relations = [x.strip() for x in relations]
		relations.append('against')
		relations.append('at')
		
		if args['sentence']:
			# no pos tags, one sentence
			print(parse_sent(args['sentence'].split()))
		else:
			# no pos tags, all of a file
			forms = open(args['output'],'w')

			if not args['input']:
				print('No input file given, transforming sentences.txt')
				args['input'] = 'sentences.txt'

			with open(args['input']) as f:
				for sentence in f:
					s = sentence.split()
					
					print(parse_sent(s),file=forms)

			forms.close()
	elif args['pos']:
		if args['sentence']:
			# pos tags, one sentence
			print(parse_pos(ast.literal_eval(args['sentence'])))
		else:
			# pos tags, all of a file
			forms = open(args['output'],'w')

			if not args['input']:
				print('No input file given, transforming tagged.txt')
				args['input'] = 'tagged.txt'

			with open(args['input']) as f:
				for sentence in f:
					s = ast.literal_eval(sentence)

					print(parse_pos(s),file=forms)
			forms.close()
