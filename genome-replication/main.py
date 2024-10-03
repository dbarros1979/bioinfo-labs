# ori is the Vibrio cholerae oriC region used for various function tests
ori = "ATCAATGATCAACGTAAGCTTCTAAGCATGATCAAGGTGCTCACACAGTTTATCCACAACCTGAGTGGATGACATCAAGATAGGTCGTTGTATCTCCTTCCTCTCGTACTCTCATGACCACGGAAAGATGATCAAGAGAGGATGATTTCTTGGCCATATCGCAATGAATACTTGTGACTTGTGCTTCCAATTGACATCTTCAGCGCCATATTGCGCTGGCCAAGGTGACGGAGCGGGATTACGAAAGCATGATCATGGCTGTTGTTCTGTTTATCTTGTTTTGACTGAGACTTGTTAGGATAGACGGTTTTTCATCACTGACTAGCCAAAGCCTTACTCTGCCTGACATCGACCGTAAATTGATAATGAATTTACATGCTTCCGCGACGATTTACCTCTTGATCATCGATCCGATTGAAGATCTTCAATTGTTAATTCTCTTGCCTCGACTCATAGCCATGATGAGCTCTTGATCATGTTTCCTTAACCCTCTATTTTTTACGGAAGAATGATCAAGCTGCTGCTCTTGATCATCGTTTC"

# Print length of ori
print("Length of ori:", len(ori))

# Function to count approximate pattern matches
def ApproximatePatternCount(Text, Pattern, d):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if HammingDistance(Text[i:i+len(Pattern)], Pattern) <= d:
            count += 1
    return count

# Function to find approximate pattern matches
def ApproximatePatternMatching(Pattern, Genome, d):
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
        if HammingDistance(Genome[i:i+len(Pattern)], Pattern) <= d:
            positions.append(i)
    return positions

# Function to calculate Hamming distance
def HammingDistance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1
    return distance

# Function to count occurrences of a pattern in text
def PatternCount(Text, Pattern):
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i:i+len(Pattern)] == Pattern:
            count += 1
    return count

# Function to get frequent words in a text
def FrequencyMap(Text, k):
    freq = {}
    for i in range(len(Text) - k + 1):
        kmer = Text[i:i + k]
        if kmer in freq:
            freq[kmer] += 1
        else:
            freq[kmer] = 1
    return freq

def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    max_count = max(freq.values())
    for key in freq:
        if freq[key] == max_count:
            words.append(key)
    return words

# Function to find the reverse of a pattern
def Reverse(Pattern):
    return Pattern[::-1]

# Function to get the complement of a DNA pattern
def Complement(Pattern):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join([complement[base] for base in Pattern])

# Function to find the reverse complement of a DNA pattern
def ReverseComplement(Pattern):
    return Complement(Reverse(Pattern))

# Function to find exact matches of a pattern in a genome
def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i:i + len(Pattern)] == Pattern:
            positions.append(i)
    return positions

# Function to calculate the skew array of a genome
def SkewArray(Genome):
    skew = [0]
    for base in Genome:
        if base == 'G':
            skew.append(skew[-1] + 1)
        elif base == 'C':
            skew.append(skew[-1] - 1)
        else:
            skew.append(skew[-1])
    return skew

# Function to find the position of minimum skew in a genome
def MinimumSkew(Genome):
    skew = SkewArray(Genome)
    min_skew = min(skew)
    positions = [i for i, val in enumerate(skew) if val == min_skew]
    return positions

# Function to find the position of maximum skew in a genome
def MaximumSkew(Genome):
    skew = SkewArray(Genome)
    max_skew = max(skew)
    positions = [i for i, val in enumerate(skew) if val == max_skew]
    return positions

# Function to create a symbol array for a given genome and symbol
def SymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]
    for i in range(n):
        array[i] = PatternCount(ExtendedGenome[i:i + (n//2)], symbol)
    return array

# Optimized version of SymbolArray
def FasterSymbolArray(Genome, symbol):
    array = {}
    n = len(Genome)
    ExtendedGenome = Genome + Genome[0:n//2]

    # Look at the first half of Genome to compute the first array value
    array[0] = PatternCount(Genome[0:n//2], symbol)

    for i in range(1, n):
        array[i] = array[i - 1]
        if Genome[i - 1] == symbol:
            array[i] -= 1
        if ExtendedGenome[i + (n//2) - 1] == symbol:
            array[i] += 1
    return array

# Function to find positions of mismatches between two DNA sequences
def HammingDistance(p, q):
    return sum([1 for i in range(len(p)) if p[i] != q[i]])

# Testing functions with a small Vibrio cholerae genome excerpt
Text = "CGCGATACGTTACATACATGATAGACCGCGCGCGATCATATCGCGATTATC"
Pattern = "CGCG"
k = 3

print("Frequent Words:", FrequentWords(Text, k))
print("Reverse Complement of 'TTGTGTC':", ReverseComplement("TTGTGTC"))
print("Pattern Matching positions:", PatternMatching(Pattern, ori))
print("Hamming Distance between 'GGGCCGTTGGT' and 'GGACCGTTGAC':", HammingDistance("GGGCCGTTGGT", "GGACCGTTGAC"))
print("Minimum Skew positions:", MinimumSkew(ori))
print("Maximum Skew positions:", MaximumSkew(ori))
