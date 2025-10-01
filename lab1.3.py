def read_fasta(file_path):
    sequence = ""
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line.startswith(">"):
                sequence += line
    return sequence

file_path = "C:/Users/ana/Desktop/bioinfo/lab1/sequence.fasta"

seq = read_fasta(file_path)

seq = seq.upper()

alphabet = sorted(set(seq))

total = len(seq)
percentages = {}
for char in alphabet:
    count = seq.count(char)
    percentages[char] = (count / total) * 100

print(f"Alphabet: {alphabet}\n")
print("Percentage of each symbol:")
for char, percent in percentages.items():
    print(f"{char}: {percent:.2f}%")