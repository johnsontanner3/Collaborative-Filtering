'''
Created on Dec 3, 2016

@author: Tanner Johnson
'''
def processData(filename):
    '''
    This function is designed to read the file foodRatings.txt 
    to return itemlist and dictratings. itemlist is a list of unique 
    eateries and dictratings is a dictionary with keys of individuals
    who have participated in rating eateries with corresponding values
    as a list of ratings that match itemlist's values and order. Non-zero
    numbers in value pairs represent rated eateries by the individual.  
    '''
    pre_wordlist = []
    f = open(filename)
    for line in f:
        line = line.strip()
        pre_wordlist.append(line)
    xx = [x for i,x in enumerate(pre_wordlist) if i % 2 != 0]
#     print pre_wordlist
    rest_list = []
    for rtngs in xx:
        yy = rtngs.split()
        for i,x in enumerate(yy):
            if i % 2 == 0:
                rest_list.append(x)
    itemlist = sorted(list(set(rest_list)))
#     print itemlist
    ans = []
    for item in pre_wordlist:
        if pre_wordlist.index(item) % 2 != 0:
            ans.append(( pre_wordlist[pre_wordlist.index(item) - 1] , [x for i,x in enumerate(item.split()) ]) )
#     print ans
    newans = []
    dictratings = {}
    for (pers, ranks) in ans:
        if pers not in dictratings:
               
            dictratings[pers] = [0,0,0,0,0,0,0] # could also do [0]*7
        xxx = [x for i,x in enumerate(ranks) if i%2 == 0] # list of restaurants
        for item in xxx:
            if item in itemlist:
                where = itemlist.index(item)
                dictratings[pers][where] += int(ranks[ranks.index(item) + 1])
    return itemlist, dictratings
    
    
    
if __name__ == '__main__':
    file = "foodRatings.txt"
#     print processData(file)
    processData(file)