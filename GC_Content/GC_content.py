from sys import argv
script, filename = argv

#Reads FASTA file and returns a dictionary with ID:sequence pairs
def load_sequences(FASTA_file):
	sequences = {}
	sequence = ""
	start = True
	with open(FASTA_file) as sequence_data:
		for line in sequence_data:
			if start == True:
				sequence_id = line.rstrip().lstrip(">")
				start = False
			else:
				if line.startswith(">"):
					sequences[sequence_id] = sequence
					sequence_id = line.rstrip().lstrip(">")
					sequence = ""
				else:
					sequence += line.strip()
		sequences[sequence_id] = sequence
		return sequences

#Iterates through sequence dictionary and finds the sequence with the highest GC content
def gc_content(sequences):
	GC_content = {}
	max_ID = ""
	max_percent = 0
	for ID, DNA in sequences.items():
		GC_count = DNA.count("G") + DNA.count("C")
		GC_percent = float(GC_count)/len(DNA) * 100
		GC_content[ID] = GC_percent
		if GC_percent > max_percent:
			max_percent = GC_percent
			max_ID = ID
	return GC_content.items(), max_ID, max_percent
		
if __name__ == "__main__":
	sequences = load_sequences(filename)
	max_ID, max_percent = gc_content(sequences)[1:]
	with open("answer.txt", "w") as answer:
		answer.write("ID with the maximum GC content is %s" % max_ID)
		answer.write(" at %f" % max_percent)
		answer.write("%")