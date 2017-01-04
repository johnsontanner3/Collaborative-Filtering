'''
Created on Dec 3, 2016

@author: Tanner Johnson
'''
from __future__ import division
import ReadFood
import ReadBooks
import ReadMovies


def averages(itemlist, dictratings):
    '''
    returns averageList as list of tuples 
    where each tuple has item rated and the 
    average float rating for all
    who have rated it. 
    '''
    averageList = []
    for rrnt in itemlist:
        where = itemlist.index(rrnt) # index of interest
        avg = []
        count = 0
        for v in dictratings.values():
            # v is list of integers
            rtng = v[where]
            if rtng != 0:
                avg.append(rtng)
                count += 1
            else:
                pass
        tot = sum(avg)
        if count == 0:
            theAvg = 0
        else:
            theAvg = float(tot/count)
        addThis = (rrnt, theAvg)
        averageList.append(addThis)
    return sorted(averageList, reverse=True, key=lambda x: x[1])
    
    
def similarities(name, dictratings):
    '''
    returns reordered which is a list of tuples with rater-name (string)
    in index 0 and similarity-index (float) in index 1. Sort with most
    similar rater first. Use sum of dot products for the similarity
    index for EACH comparison with 'name' parameter. 
    '''
    similarList = []
    nameValue = dictratings[name] # ratings for our person of interest
    for k,v in dictratings.iteritems():
        dotProducts = []
        if k == name:
            pass
        else:
            for i, val in enumerate(v):
                dotIt = val * nameValue[i]
                dotProducts.append(dotIt)
        similarList.append((k, sum(dotProducts)))
    similarListFinal = [item for item in similarList if item[0] != name]
        
#     print similarListFinal
    reordered = sorted(similarListFinal, reverse=True, key=lambda x: (x[1]))
    return reordered
    
    
    
     
def recommend(similarList, itemlist, dictratings, n):
    '''
    returns recommendList, a list of recommended items in tuple
    with item first then score (int) for that item.
    n (int) is how many ratings from similarList should be used. 
    take similarity value and multiply through all that 
    person's ratings to weight them. Then add and take float avg.
    So let's look at Lee and make suggestions.  
    '''
    recommendList = []
    simCutoff = similarList[:n]
    for (pers, simRating) in simCutoff:
        weighted = []
#         count = 0
        originalRatings = dictratings[pers] # list of originals
        for val in originalRatings:
            weighted.append(simRating*val)
        recommendList.append(weighted)
#     print 'raw weighted:', recommendList # should be raw list, not averaged indexed with original itemlist
    Tots = [sum(x) for x in zip(*recommendList)]
#     print 'sum weighted:', Tots # not avgs yet, just totals
    voted = []
    for i in range(len(itemlist)):
#         voted = []
        count = 0
        for item in recommendList:
#             count = 0 # at this pos
            if item[i] != 0:
                count += 1
        voted.append(count) 
#     print 'actually ranked:', voted
    avgs = []
    for ind, valU in enumerate(Tots):
        if voted[ind] == 0:
            subAv = 0
        else:
            subAv = float(valU/voted[ind])
        avgs.append(subAv)
#     print 'averages:', avgs
    Rcmd = []
    for i,v in enumerate(avgs):
        where = itemlist[i]
        Rcmd.append((where, v))
#     print 'unsorted recommendations:', Rcmd
    sortedRcmds = sorted(Rcmd, reverse=True, key=lambda x: x[1])
    return sortedRcmds
    

    


if __name__ == '__main__':
    filename = 'foodRatings.txt'
    #filenameA = 'authorsAndBooks.txt' 
    #filenameB = 'bookRatings.txt'
    #filename = 'movieRatings.txt'
    module = ReadFood
    #module = ReadBooks
    #module = ReadMovies
    input1 = module.processData(filename)[0]
    input2 = module.processData(filename)[1]
    print averages(input1, input2)
    print similarities('JoJo', input2)
    simList = similarities('JoJo', input2)
    n = 5
    print recommend(simList, input1, input2, n)
