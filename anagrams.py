#CHALLENGE - given a list of words, return the words that are anagrams of other words within the same list

#version 1
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

# version 2
def ana(word, words):
    a = "".join(sorted(word))
    anas = []
    for i in words:
        if "".join(sorted(i)) == a:
            anas.append(i)
    return anas


# version 3
def ana(lst):
    results=set()
    for word in lst:
        clone = [cloneword for cloneword in lst]
        asdf = sorted(word.lower())
        clone.remove(word)
        #print clone
        for word2 in clone:
            asdf2 = sorted(word2.lower())
            if asdf == asdf2:
                results.add(word)
                results.add(word2)
    return results
