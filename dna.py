eva = {"female": "TGAAGGACCTTC", "white": "AAAACCTCA", "blonde": "TTAGCTATCGC", "blue": "TTGTGGTGGC", "oval": "AGGCCTCA"}
larisa = {"female": "TGAAGGACCTTC", "white": "AAAACCTCA", "brown": "GCCAGTGCCG", "brown": "AAGTAGTGAC", "oval": "AGGCCTCA"}
matej = {"male": "TGCAGGAACTTC", "white": "AAAACCTCA", "black": "CCAGCAATCGC", "blue": "TTGTGGTGGC", "oval": "AGGCCTCA"}
miha = {"male": "TGCAGGAACTTC", "white": "AAAACCTCA", "brown": "GCCAGTGCCG", "green": "GGGAGGTGGC", "square": "GCCACGG"}


with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()
    #print(dna)

for x in eva:
    if eva[x] in dna:
        print("Eva " + (x))
for x in larisa:
    if larisa[x] in dna:
        print("Larisa " + (x))
for x in matej:
    if matej[x] in dna:
        print("Matej " + (x))
for x in miha:
    if miha[x] in dna:
        print("Miha " + (x))

