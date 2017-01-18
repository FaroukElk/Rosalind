# My solutions to Bioinformatic problems on rosalind.info

# Consensus and Profile
Problem involves analyzing a collection of DNA sequences for the most common nucleotide present at each of the sequence's position. We can then use the common nucleotide information to infer a possible ancestor sequence among the collection. 

Input file is a collection of DNA sequences in FASTA format

Output file is a possible common ancestor sequence followed by a matrix for the number of times each nucleotide appears among the collection of sequences.

# Computing GC Content
We are tasked with finding the DNA sequence among a collection of sequences with the highest amount of guanine and cytosine.

Input file is a collection of DNA sequences in FASTA format

Output file is the ID of the string with the highest GC-content, followed by the GC-content percentage of that string.

# RNA Splicing
Given a DNA sequence followed by a collection of subsequences to act as introns. Tasked with removing the introns and concatenating the exons to form an RNA sequence ready for translation.

Output file is a protein string resulting from transcribing and translating the exons of the DNA sequence.

# Open Reading Frames
Problem involves searching for open reading frames within an RNA sequence and translating the ORF into a protein.

Input file is a DNA sequence

Output file is the distinct protein strings that can be translated from the ORFs of the DNA sequence

# Overlap Graphs
For a collection of strings and an integer k, we are tasked with finding the sequences whose k-suffix matches the k-prefix of another sequence.

Input file is a collection of DNA sequences in FASTA format

Output file is the adjacency list of overlaps where k = 3

# Finding a Motif in DNA
Problem involves finding the starting indexes of a substring pattern within a DNA sequence.

Input is the DNA sequence and the pattern to be searched

Output is all locations of the pattern within the DNA sequence

# Finding a Shared Motif
Problem involves finding a longest common substring that is a present in every member of a DNA collection. The program starts with the longest possible substring and works down until the first substring that is common between all sequences is found.

Input file is a collection of DNA sequences in FASTA format

Output file is the first substring found to be common among the collection
