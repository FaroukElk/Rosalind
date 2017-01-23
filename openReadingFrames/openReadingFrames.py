from sys import argv

#Searches for reading frames within RNA sequence and stores the protein strings in a set
def ORF_Search(RNA):
	proteins = set([])
	for i in range(len(RNA)):
		protein = ""
		codon = RNA[i:i+3]
		if len(codon) < 3:
			break
		if codon_protein_pairs[codon] == "M":
			for j in range(i,len(RNA), 3):
				codon2 = RNA[j:j+3]
				if len(codon2)<3:
					break
				if (codon_protein_pairs[codon2] == "STOP"):
					proteins.add(protein)
					break
				else:
					protein += codon_protein_pairs[codon2]
				
	return proteins
			
#Converts DNA stand to RNA
def DNAtoRNA(DNA):
	RNA = DNA.replace("T", "U")
	return RNA
	
#Returns reverse complement of DNA string
def ReverseComplement(DNA):
	complementary_bp = {"A":"T", "T":"A", "G":"C", "C":"G"}
	reverse_DNA_comp = ""
	for base in DNA[::-1]:
		reverse_DNA_comp += complementary_bp[base]
	return reverse_DNA_comp
	
codon_protein_pairs = {
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

if __name__ == "__main__":
	script, filename = argv
	sequence = ""
	with open(filename) as sequence_data: #load DNA sequence
		next(sequence_data)
		for line in sequence_data:
			sequence += line.strip()
	reverseDNA = ReverseComplement(sequence) #Find reverse complement of DNA sequence
	reverseRNA = DNAtoRNA(reverseDNA) #converts reverse complement of sequence to RNA
	ORFReverse = ORF_Search(reverseRNA) #searches for ORFs of the reverse complement
	ORFSequence = ORF_Search(DNAtoRNA(sequence)) #searches for ORFs of the original sequence
	ORFSequence.update(ORFReverse)
	with open("answer.txt",	"w") as answer:
		for protein in ORFSequence: #writes each protein to output file
			answer.write(protein)
			answer.write("\n")
