'''
Created on Dec 3, 2016

@author: Tanner Johnson
'''

from Recommender import averages
from Recommender import similarities
from Recommender import recommend
from ReadFood import processData

foodfile = 'foodRatings.txt'
fooditems, fooddict = processData(foodfile)

resultavg = averages(fooditems, fooddict)
print "Restaurants and their average ratings"
print "-------------------------------------"
for item in resultavg:
    print item
print

person1 = "Shirley"
resultsim = similarities(person1, fooddict)
print "Ratings similar to", person1
print "--------------------------"
for pers in resultsim:
    print pers
print

n = 3
resultrec = recommend(resultsim, fooditems, fooddict, n)
smallresultrec = resultrec[:3]
print "Recommendations for Shirley with", n, "most similar raters"
print "------------------------------------------------------"
for item in smallresultrec:
    print item
print

person2 = "Xiawei"
resultsim2 = similarities(person2, fooddict)
print "Ratings similar to", person2
print "-------------------------"
for iteM in resultsim2:
    print iteM
print

resultrec2 = recommend(resultsim2, fooditems, fooddict, n)
smallresultrec2 = resultrec2[:3]
print "Recommendations for Xiawei with", n, "most similar raters"
print "-----------------------------------------------------"
for thin in smallresultrec2:
    print thin
    








    