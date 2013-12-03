def anagrams(input):
    output = []
    output2 = []
    for i in input:
        word1 = [c for c in i]
        word1.sort()
        for j in input:
            word2 = [c for c in j]
            word2.sort()
            if word1 == word2 and i != j:
                output2.extend([i,j])
    for k in output2:
        if k not in output:
            output.append(k)
    return output
