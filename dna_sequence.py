#DNA Letter Counter Program  🧬

#Get the DNA sequence from the user
dna_sequence = input("Enter your DNA sequence:")

#count the number of each letter in the DNA sequence
count_A = dna_sequence.count("A")
count_G = dna_sequence.count("G")
count_T = dna_sequence.count("T")
count_C = dna_sequence.count("C")

#print the results
print("DNA sequence " + dna_sequence)
print("Number of A's: " + str(count_A))
print("Number of G's: " + str(count_G))
print("Number of T's: " + str(count_T))
print("Number of C's: " + str(count_C))