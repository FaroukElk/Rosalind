from sys import argv

#loads DNA sequences from FASTA file format
def load_sequences(FASTA_File): 
	sequence_list = []
	sequence = ""
	start = True
	with open(FASTA_File) as sequence_data:
		for line in sequence_data:
			if start == True:
				start = False
			else:
				if line.startswith(">"):
					sequence_list.append(sequence)
					sequence = ""
				else:
					sequence += line.strip()
		sequence_list.append(sequence)
	return sequence_list

#Counts which nucleotide base is in each of the DNA sequences position
def Nucleotide_Count(sequences): 
	A_count_and_position, C_count_and_position, G_count_and_position, T_count_and_position = [], [], [], []
	i = 0
	while i < len(sequences[0]):
		A_count = 0 
		G_count = 0
		C_count = 0
		T_count = 0
		for j in range(len(sequences)):
			if sequences[j][i] == "A":
				A_count += 1
			elif sequences[j][i] == "T":
				T_count += 1
			elif sequences[j][i] == "G":
				G_count += 1
			else:
				C_count += 1
		i += 1
		A_count_and_position.append(A_count)
		T_count_and_position.append(T_count)
		G_count_and_position.append(G_count)
		C_count_and_position.append(C_count)
	return A_count_and_position, T_count_and_position, G_count_and_position, C_count_and_position
		
"""The nucleotides with the highest count at each position are used to hypothesize the common DNA ancestor. 
Precedence is A > T > G > C"""	
def Common_Ancestor(A_count, T_count, G_count, C_count): 
	common_sequence = ""
	for i in range(len(A_count)):
		if A_count[i] >= T_count[i] and A_count[i] >= C_count[i] and A_count[i] >= G_count[i]:
			common_sequence += "A"
		elif T_count[i] >= A_count[i] and T_count[i] >= C_count[i] and T_count[i] >= G_count[i]:
			common_sequence += "T"
		elif G_count[i] >= A_count[i] and G_count[i] >= T_count[i] and G_count[i] >= C_count[i]:
			common_sequence += "G"
		elif C_count[i] >= A_count[i] and C_count[i] >= T_count[i] and C_count[i] >= G_count[i]:
			common_sequence += "C"
	return common_sequence

if __name__ == "__main__":
	script, filename = argv
	sequences = load_sequences(filename)
	test_sequences = ["ATCCAGCT", "GGGCAACT", "ATGGATCT", "AAGCAACC", "TTGGAACT", "ATGCCATT", "ATGGCACT"]
	ACount, TCount, GCount, CCount = Nucleotide_Count(sequences)
	with open("answer.txt", "w") as answer:
		answer.write(Common_Ancestor(ACount, TCount, GCount, CCount))
		answer.write("\n")
		answer.write("A: ")
		answer.write(" ".join(str(x) for x in ACount))
		answer.write("\n")
		answer.write("C: ")
		answer.write(" ".join(str(x) for x in CCount))
		answer.write("\n")
		answer.write("G: ")
		answer.write(" ".join(str(x) for x in GCount))
		answer.write("\n")
		answer.write("T: ")
		answer.write(" ".join(str(x) for x in TCount))



	

