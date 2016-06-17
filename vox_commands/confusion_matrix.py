# Let's get a confusion matrix for results with the POS flag on (test results) using results with the flag off as ground truth (GT).

# True positives: parsed form shows up in test results and GT
# False positives: form shows up in test results and not in GT
# False negatives: form shows up in GT and not in test results
# True negatives: I wouldn't think there should be any of these???

if __name__ == '__main__':
	true_pos = 0
	false_pos = 0
	false_neg = 0
	true_neg = 0

	gt = list(open('functional_forms.txt'))
	pos = list(open('output.txt'))
	
	all = gt + pos
	print(len(all))
	all = set(all)
	print('Unique forms: {}'.format(len(all)))

	for form in all:
		if form in pos and form in gt:
			true_pos += 1
		elif form in pos and form not in gt:
			false_pos += 1
		elif form in gt and form not in pos:
			false_neg += 1
		else:
			true_pos += 1

	print('TP: {}\tFN: {}\nFP: {}\tTN: {}'.format(true_pos,false_pos,false_neg,true_neg))