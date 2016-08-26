from visual_function import percentvisual

data = [ {'nickname' : 'drazzzer', 'major' : 'CS',
          'gender' : 'Male'}, {'nickname' : 'serg98', 'major' : 'CS',
          'gender' : 'Male'}]
name1 = data[0]
name2 = data[1]




def perMatch(name1,name2):
    '''Takes 2 Dictionaries as paramaters, returns the percentage of matched values'''
    total = len(name1.keys()) - 1
    matchcount = 0
    #print name1.keys()
    
    if name1['gender'] == name2['gender']:
        matchcount = matchcount + 1
    if name1['major'] == name2['major']:
        matchcount = matchcount + 1

    percent = float(matchcount)/total
    percentvisual(percent,600,50, (10,255,100))
    



perMatch(name1,name2)
