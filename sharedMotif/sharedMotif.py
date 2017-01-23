from sys import argv

#Starts with longest substring and checks if shared among all sequences
def Shared_Motif(sequences, maxlength, minlength): 
	while minlength > 0:
		for i in range(maxlength - minlength + 1):
			if i + minlength > maxlength:
				break
			else:
				substring = sequences[0][i:i+minlength]
				if checkAll(substring, sequences): #if substring passes check, then a longest substring is found
						return substring
		minlength -= 1

def checkAll(substring, sequences): # check if substring in all strings
		for sequence in sequences:
			if substring not in sequence:
				return False
		return True



def load_sequences(FASTA_File):
	sequence_list = []
	sequence = ""
	start = True
	minlength = 10000
	maxlength = 0
	with open(FASTA_File) as sequence_data:
		next(sequence_data) #skip first line
		for line in sequence_data:
			if line.startswith(">"):
				sequence_list.append(sequence)
				if len(sequence) < minlength: #checks for shortest sequence in list
					minlength = len(sequence)
				if len(sequence) > maxlength: #checks for longest sequence in list
					maxlength = len(sequence)
				sequence = ""
			else:
				sequence += line.strip()
		sequence_list.append(sequence)
	return sequence_list, minlength, maxlength
	
if __name__ == "__main__":
	script, filename = argv
	sequences, minlength, maxlength = load_sequences(filename)
	with open("answer.txt", "w") as answer:
		answer.write(Shared_Motif(sequences, maxlength, minlength))
