'''
Created on Dec 3, 2016

@author: Tanner Johnson
'''
from Recommender import averages
from Recommender import similarities
from Recommender import recommend
from ReadBooks import processData

foodfileA = 'authorsAndBooks.txt'
foodfileB = 'bookRatings.txt'
fooditems, fooddict = processData(foodfileA, foodfileB)

resultavg = averages(fooditems, fooddict)
smallresultavg = resultavg[:20]
print "Books and their average ratings"
print "-------------------------------"
for item in smallresultavg:
    print item
print

person1 = "Rosa"
resultsim = similarities(person1, fooddict)
smallresultsim = resultsim[:20]
print "Ratings similar to", person1
print "----------------------------"
for pers in smallresultsim:
    print pers
print

person2 = "Cedric Jones"
resultsim2 = similarities(person2, fooddict)
smallresultsim2 = resultsim2[:20]
print "Ratings similar to", person2
print "----------------------------"
for pers in smallresultsim2:
    print pers
print

person3 = "Cust6"
resultsim3 = similarities(person3, fooddict)
smallresultsim3 = resultsim3[:20]
print "Ratings similar to", person3
print "----------------------------"
for pers in smallresultsim3:
    print pers
print

resultrec1 = recommend(resultsim, fooditems, fooddict, 20)
smallresultrec1 = resultrec1[:10]
print "Recommendations for", person1, "with top 20 most similar raters"
print "------------------------------------------------------------"
for x in smallresultrec1:
    print x
print

resultrec2 = recommend(resultsim2, fooditems, fooddict, 20)
smallresultrec2 = resultrec2[:10]
print "Recommendations for", person2, "with top 20 most similar raters"
print "------------------------------------------------------------"
for x in smallresultrec2:
    print x
print

resultrec3 = recommend(resultsim3, fooditems, fooddict, 20)
smallresultrec3 = resultrec3[:10]
print "Recommendations for", person3, "with top 20 most similar raters"
print "------------------------------------------------------------"
for x in smallresultrec3:
    print x
    