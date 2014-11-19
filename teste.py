''' Lab_Bigram '''
def bigram(word, two_gram, chk):
    '''Input(string): Word -> Output: Max of 2Bigram and Frequency'''
    for i in xrange(len(word)-1):
        if word[i:i+2] in two_gram:
            two_gram[word[i:i+2]] += 1
        else:
            two_gram[word[i:i+2]] = 1
    first, freq = max(two_gram.items(), key = lambda item:item[1])
    for i in two_gram:
        if freq == two_gram[i]:
            chk.append(i)
    first = len(word)
    for i in chk:
        if word.find(i) < first:
            first = word.find(i)
    print word[first:first+2] + '\n' + str(freq)
bigram(raw_input(), {}, [])
