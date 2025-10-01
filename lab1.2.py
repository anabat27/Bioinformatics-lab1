
S = "ACGGGCATATGCGCcc"

S = S.upper()

alphabet = sorted(set(S))

total = len(S)
percentages = {}
for nuc in alphabet:
    count = S.count(nuc)
    percentages[nuc] = (count / total) * 100

print(f"Alphabet: {alphabet}\n")
print("Percentage of each nucleotide:")
for nuc, percent in percentages.items():
    print(f"{nuc}: {percent:.2f}%")
