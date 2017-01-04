'''
Created on Dec 3, 2016

@author: Tanner Johnson
'''
def processData(booktitles, bookratings):
    '''
    This function is designed to read the files with authors and books 
    as well as the file with book ratings by individuals and 
    returns itemlist of unique books and their titles, as well as
    a dictionary, dictratings, with each key being an individual in bookratings
    and the corresponding value being a list of ratings for each book-author item
    in itemlist--zeros in the list represent non-rated books by the individual. 
    The value list order for each key corresponds with the order in itemlist. 
    '''
    itemlist = []
    f = open(booktitles)
    for item in f:
        xx = item.strip().split("::")
        yy = [xx[-1], xx[-2]]
        zz = ",".join(yy)
        itemlist.append(zz)
#     print itemlist
    bleh = []
    g = open(bookratings)
    for item in g:
        bleh.append(item.strip())
#     print bleh
    listnum = [x for i,x in enumerate(bleh) if i % 61 == 0]
#     print listnum
    dictratings = {}
    for item in listnum:
        if item not in dictratings:
            dictratings[item] = [ int(this) for this in bleh[bleh.index(item) +1: bleh.index(item) + 61] ]
#     print itemlist
    return itemlist, dictratings
    

    
if __name__ == '__main__':
    titles = 'authorsAndBooks.txt'
    ratings = 'bookRatings.txt'
#     print processData(titles, ratings)
    processData(titles, ratings)