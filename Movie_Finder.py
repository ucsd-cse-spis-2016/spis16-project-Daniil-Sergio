import urllib

def parseData(fname):
    for l in urllib.urlopen(fname):
        yield eval(l)






def findMovie(movie,num):
    names = getTitle()
    alsoBought = []
    
    for user in metadata:
        try:
            if user['title'].find(movie) != -1:
                for alsoB in user['related']['buy_after_viewing']:            
                    alsoBought.append(alsoB)
        except:
            print ''

    finalDict = [{name: [0, 0]} for name in alsoBought]
    i = 0
    for review in data:
        if review['asin'] in alsoBought:
            for elem in finalDict:
                try:
                    elem[names[review['asin']]][1] += 1
                    elem[names[review['asin']]][0] += review['overall']
                except:
                    i += 1
    print finalDict
    compDict = {}
    for elem in finalDict:
        for mov in elem:
            print elem, mov
            elem[mov][0] = (float(elem[mov][0])/float(elem[mov][1]))
            compDict[mov] = float(elem[mov][0]) * float(elem[mov][1])
    
    finished = sorted(compDict.iteritems(), key=lambda (k,v): (v,k))

    return finished
        
    
        
    

def getTitle():
    final = {}
    i = 0
    for elem in metadata:
        try:
            final[elem['asin']] = elem['title']
        except:
            i += 1
    return final


print "Reading Data..."
data = list(parseData("http://cses.ucsd.edu/spis/reviews_Movies_and_TV_5.json"))   
print "done"


print "Reading Metadata..."
metadata = list(parseData("http://cses.ucsd.edu/spis/meta_Movies_and_TV.json"))
print "done"

print findMovie('Everyday', 5)

