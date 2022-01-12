def groupAnagrams(words):
    anagrams = []
    if not words:
        return anagrams
    nums = [''.join(sorted(word)) for word in words]
    print(nums)
    d = {}
    for i, e in enumerate(nums):
        d.setdefault(e, []).append(i)
        print(d)
    for index in d.values():
        collection = tuple(words[i] for i in index)
        if len(collection) > 1:
            anagrams.append(collection)
    return anagrams
if __name__ == '__main__':
    words = ['bfee', 'ebef', 'cat', 'god', 'tac', 'dog', 'feeb' ,'tca', 'gdo']
    anagrams = groupAnagrams(words)
    ana_list=[]
    for anagram_val in anagrams:
        ana_list.append(anagram_val)
    my_string = ''
    for i in ana_list:
        for j in i:
            my_string = my_string+" "+j
    print(my_string)
 
