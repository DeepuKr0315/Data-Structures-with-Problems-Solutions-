def groupAnagrams(strings):
    if len(strings) == 0:
        return []
    hash = {}
    sortedStr = [''.join(sorted(i)) for i in strings]
    for i in range(len(strings)):
        if sortedStr[i] in hash:
            hash[sortedStr[i]].append(strings[i])
        else:
            hash[sortedStr[i]] = [strings[i]]
    return list(hash.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))