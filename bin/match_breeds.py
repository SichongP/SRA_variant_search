import os
import errno
def open_file(filename):
	try:
		fp = open(filename)
	except IOError as e:
		if e.errno == errno.ENOENT:
			print("Error: Cannot find file {} at src/".format(filename))
			return None
		raise
	else:
		with fp:
			return fp.readlines()
def match_breeds(varianthash, breeds, output):
#breeds is a file containing a list of samples and their breeds in a csv format
#Read breeds file
	breedhash = {}
	try:
		out = open(output, 'w')
	except IOError as e:
		if e.errno == errno.EACCES:
			print("Error: Permission denied when trying to write to output")
			exit(1)
		raise Exception("Failed to open file")
	out.write('chr,pos,breeds\n')
	breedCount={}
	for line in open_file(breeds):
		if line.isspace():
			continue
		sample, breed = line.strip().split(',')
		file = sample + ".txt"
		breedhash[file] = breed
	for identifier in varianthash:
		out.write(identifier)
		b = []
		for file in varianthash[identifier]:
			if not varianthash[identifier][file] == ".":
				if file in breedhash:
					if breedhash[file] not in breedCount:
						breedCount[breedhash[file]] = 1
						b.append(breedhash[file]) 
					else:
						breedCount[breedhash[file]]+=1
		for breed in b:
			out.write(',' + breed + ',' + breedCount[breed])
