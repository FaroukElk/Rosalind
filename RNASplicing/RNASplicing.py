from sys import argv
	
#Amino acid codon pairs	
NucleotideAAPairs = {
"UUU": "F", "UUC": "F",
"UUA": "L", "UUG": "L",
"UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
"UAU": "Y", "UAC": "Y",
"UAA": "STOP", "UAG": "STOP", "UGA": "STOP",
"UGU": "C", "UGC": "C",
"UGG": "W",
"CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
"CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", 
"CAU": "H", "CAC": "H",
"CAA": "Q", "CAG": "Q",
"CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
"AUU": "I", "AUC": "I", "AUA": "I",
"AUG": "M",
"ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
"AAU": "N", "AAC": "N",
"AAA": "K", "AAG": "K",
"AGU": "S", "AGC": "S",
"AGA": "R", "AGG": "R",
"GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
"GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
"GAU": "D", "GAC": "D",
"GAA": "E", "GAG": "E",
"GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"}

#Converts DNA to RNA
def DNAtoRNA(DNA):
	RNA = DNA.replace("T", "U")
	return RNA
	
#Removes introns from DNA	
def IntronSplice(DNA,Introns):
	for intron in Introns:
		DNA = DNA.replace(intron, "")
	return DNA
	
#Transcribes RNA to protein string	
def RNA_to_Protein(RNA):
	protein = ""
	for i in range(0, len(RNA), 3):
		codon = RNA[i:i+3]
		if NucleotideAAPairs[codon] == "STOP":
			break
		else:
			protein += NucleotideAAPairs[codon]
	return protein
	
#Loads the DNA sequence and intron strings	
def loadSequenceAndIntrons(filename): 
	with open(filename) as data:
		start = 0
		intron = ""
		intronlist = []
		for line in data:
			if line.startswith(">") and start == 0:
				sequence = ""
				start = 1
			elif start == 1:
				if line.startswith(">"):
					start = 2
				else:
					sequence += line.strip()
			else:
				if line.startswith(">") and intron != "":
					intronlist.append(intron)
					intron = ""
				else:
					intron += line.strip()
		intronlist.append(intron)
		return sequence, intronlist
	
if __name__ == "__main__":
	script, filename = argv
	sequence, intronlist = loadSequenceAndIntrons(filename)
	DNA = IntronSplice(sequence, intronlist)
	RNA = DNAtoRNA(DNA)
	protein = RNA_to_Protein(RNA)
	with open("answer.txt", "w") as answer:
		answer.write(protein)
				