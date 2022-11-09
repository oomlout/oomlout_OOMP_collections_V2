
######  Auto translated oomp file

def load(newPart,it):
    oType = "COLLECTION"
    oSize = "MCUU"
    oColor = "ATTINY84"
    oDesc = "STAN"
    oIndex = "01"
    hexID = "COLATTINY84"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('ATTiny84 Projects')
    newPart['description'].append('A collection of all OOMP projects that have as ATTINY84 in them')
    newPart['code'].append('attiny84')
    newPart['collection'].append({'items': ['PROJ-SPAR-11801-STAN-01', 'PROJ-SPAR-13118-STAN-01', 'PROJ-SPAR-15290-STAN-01', 'PROJ-SPAR-16653-STAN-01', 'PROJ-SPAR-16985-STAN-01']})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

