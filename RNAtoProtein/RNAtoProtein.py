#Returns a protein string from an RNA sequence
def RNA_to_Protein(RNA):
	protein = ""
	for i in range(0, len(RNA), 3):
		codon = RNA[i:i+3]
		if codon_protein_pairs[codon] == "STOP":
			break
		else:
			protein += codon_protein_pairs[codon]
	return protein
	
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


	
sampleRNA = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
print (RNA_to_Protein(sampleRNA))

#Outputs "MAMAPRTEINSTRING"