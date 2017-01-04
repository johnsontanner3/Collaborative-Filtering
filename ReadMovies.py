'''
Created on Dec 3, 2016

@author: Tanner Johnson
'''
def processData(filename):
    '''
    This function is designed to read the file movieRatings.txt. It returns a list of unique items
    that are the unique movies, itemlist2. It also returns a dictionary dictratings 
    that contains keys of individuals who have rated movies and the corresponding value
    pair is a list of ratings for each movie in itemlist2--zeros represent non-rated
    movies. 
    '''
    pre_itemlist = []
    f = open(filename)
    for line in f:
        pre_itemlist.append(line.strip())
    itemlist = []
    for item in pre_itemlist:
        theStarts = [i for i,x in enumerate(item) if x == '(']
        theEnds = [i for i,x in enumerate(item) if x == ')']
        student = item[item.index('(')+1: item.index(")")]  # first index of (
        movie = item[theStarts[1]+1:theEnds[1]]
        ranking = int(item[theStarts[2]+1:theEnds[2]])
        together = [student,movie,ranking]
        itemlist.append(together)
    itemlist2 = list(set([thing[1] for thing in itemlist]))
#     print itemlist2
    uniqueStudents = list(set([item[0] for item in itemlist]))
#     return len(itemlist2)
    dictratings = {}
    for stud in uniqueStudents:
        if stud not in dictratings:
            dictratings[stud] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        for seT in itemlist:
            if seT[0] == stud:
                dictratings[stud][itemlist2.index(seT[1])]  += seT[-1]
    return itemlist2, dictratings
        
    
    
    
if __name__ == '__main__':
    file = 'movieRatings.txt'
#     print processData(file)
    processData(file)