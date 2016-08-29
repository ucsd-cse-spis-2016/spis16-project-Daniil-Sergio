from visual_function import percentvisual

data = [ {'nickname' : 'drazzzer', 'major' : 'CS',
          'gender' : 'male'}, {'nickname' : 'serg98', 'major' : 'CS',
          'gender' : 'female'}]
name1 = data[0]
name2 = data[1]




def perMatch(data, name1,name2):
    '''Takes 2 Dictionaries as paramaters, returns the percentage of matched values'''
    dictname1 = {}
    dictname2 = {}

    for l in range(len(data)): 
        if name1 == data[l]['nickname']:
            dictname1 = data[l]
            break
        elif name2 == data[l]['nickname']:
            dictname2 = data[l]
            break
            
    total = len(dictname1.keys()) - 1
    matchcount = 0
    for l in dictname1:
        if l != 'nickname':
            if dictname1[l] == dictname2[l]:
                matchcount = matchcount + 1

    
    percent = float(matchcount)/total
    percentvisual(percent,600,50, (10,255,100))
    



perMatch(data,'drazzzer','serg98')
