# Overlap Graphs problem,3c problem

def overlap_graph(fasta):
    n = len(fasta)
    for i in range(n):
        for j in range(n):
            if i != j and fasta[i][1:] == fasta[j][:-1]:
                print(patterns[i] + ' -> ' + patterns[j])

with open('/content/rosalind_ba3c (1).txt', 'r') as f:
    data = [line.strip() for line in f]

overlap_graph(data)