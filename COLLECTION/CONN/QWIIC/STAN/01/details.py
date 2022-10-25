
######  Auto translated oomp file

def load(newPart,it):
    oType = "COLLECTION"
    oSize = "CONN"
    oColor = "QWIIC"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "COLQWIIC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('QWIIC Breakouts')
    newPart['description'].append('A collection of all OOMP projects that have a qwiic connector')
    newPart['code'].append('qwiic')
    newPart['collection'].append({'items': []})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

