from sys import argv

#Finds the sequences who have a matching prefix and suffix of 3
def buildGraph(sequence_map):
	graphlist = []
	for key, value in sequence_map.items():
		for key2, value2 in sequence_map.items():
			if key != key2 and value.endswith(value2[0:3]):
				graphlist.append((key, key2))
	return graphlist
	
#loads DNA sequences from FASTA file format
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
		

	
if __name__ == "__main__":
	script, filename = argv
	sequence = load_sequences(filename)
	resultGraph = buildGraph(sequence)
	with open("answer.txt", "w") as answer:
		for values in resultGraph:
			answer.write("%s %s \n" % (values[0], values[1]))