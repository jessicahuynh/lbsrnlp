import sys

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

events = list(open('events.txt'))
events = [x.strip() for x in events]

objects = list(open('objects.txt'))
objects = [x.strip() for x in objects]

relations = list(open('relations.txt'))
relations = [x.strip() for x in relations]
relations.append('against')
relations.append('at')

if len(sys.argv) == 2:
	print(parse_sent(sys.argv[1].split()))
else:
	forms = open('functional_forms.txt','w')

	with open('sentences.txt') as f:
		for sentence in f:
			s = sentence.split()
			
			print(parse_sent(s),file=forms)

	forms.close()