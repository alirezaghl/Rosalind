#Generate the k-mer compostion of a string, from the chapter 3 of the vol1 

def composition(c, Data):
    comp = []
    for i in range(len(Data) - c + 1):
        comp.append(Data[i:i+c])
    return comp

with open('/content/rosalind_ba3a (3).txt', 'r') as f:
    data = f.read().splitlines()
    k = int(data[0])
    g = data[1]

result = composition(k,g)

with open('result.txt', 'w') as out:
    for s in result:
        out.write(s)
        out.write('/n')

for s in result:
    print(s)