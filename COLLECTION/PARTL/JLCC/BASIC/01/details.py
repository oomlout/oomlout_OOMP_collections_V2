
######  Auto translated oomp file

def load(newPart,it):
    oType = "COLLECTION"
    oSize = "PARTL"
    oColor = "JLCC"
    oDesc = "BASIC"
    oIndex = "01"
    hexID = "COLJLCB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['name'].append('JLC Parts Library')
    newPart['description'].append('A collection of all OOMP parts with JLC parts library details')
    newPart['code'].append('jlcb')
    newPart['collection'].append({'items': ['CAPC-0402-X-NF100-V16', 'CAPC-0402-X-NF100-V50', 'CAPC-0402-X-NF10-V50', 'CAPC-0402-X-NF1-V50', 'CAPC-0402-X-NF20-V16', 'CAPC-0402-X-NF2-V50', 'CAPC-0402-X-NF3-V50', 'CAPC-0402-X-NF47D-V50', 'CAPC-0402-X-NF70-V10', 'CAPC-0402-X-NF8-V50', 'CAPC-0402-X-PF100-V50', 'CAPC-0402-X-PF10-V50', 'CAPC-0402-X-PF12-V50', 'CAPC-0402-X-PF15D-V50', 'CAPC-0402-X-PF1-V50', 'CAPC-0402-X-PF20-V50', 'CAPC-0402-X-PF22D-V50', 'CAPC-0402-X-PF22-V50', 'CAPC-0402-X-PF30-V50', 'CAPC-0402-X-PF3-V50', 'CAPC-0402-X-PF47D-V50', 'CAPC-0402-X-PF50-V50', 'CAPC-0402-X-PF5-V50', 'CAPC-0402-X-PF70-V50', 'CAPC-0402-X-PF7-V50', 'CAPC-0402-X-PF8-V50', 'CAPC-0402-X-UF10-V63D', 'CAPC-0402-X-UF1-V25', 'CAPC-0402-X-UF2-V63D', 'CAPC-0402-X-UF47D-V10', 'CAPC-0603-X-NF100-V50', 'CAPC-0603-X-NF10-V50', 'CAPC-0603-X-NF1-V50', 'CAPC-0603-X-NF20-V25', 'CAPC-0603-X-NF2-V50', 'CAPC-0603-X-NF30-V25', 'CAPC-0603-X-NF3-V50', 'CAPC-0603-X-NF47D-V50', 'CAPC-0603-X-NF5-V50', 'CAPC-0603-X-NF70-V25', 'CAPC-0603-X-NF7-V50', 'CAPC-0603-X-NF8-V50', 'CAPC-0603-X-PF100-V50', 'CAPC-0603-X-PF10-V50', 'CAPC-0603-X-PF12-V50', 'CAPC-0603-X-PF1-V50', 'CAPC-0603-X-PF200-V50', 'CAPC-0603-X-PF20-V50', 'CAPC-0603-X-PF22-V50', 'CAPC-0603-X-PF30-V50', 'CAPC-0603-X-PF3-V50', 'CAPC-0603-X-PF47D-V50', 'CAPC-0603-X-PF50-V50', 'CAPC-0603-X-PF5-V50', 'CAPC-0603-X-PF6-V50', 'CAPC-0603-X-PF70-V50', 'CAPC-0603-X-PF7-V50', 'CAPC-0603-X-PF80-V50', 'CAPC-0603-X-PF8-V50', 'CAPC-0603-X-UF10-V10', 'CAPC-0603-X-UF10-V25', 'CAPC-0603-X-UF1-V50', 'CAPC-0603-X-UF2-V16', 'CAPC-0603-X-UF2-V63D', 'CAPC-0603-X-UF47D-V16', 'CAPC-0805-X-NF100-V100', 'CAPC-0805-X-NF100-V50', 'CAPC-0805-X-NF10-V50', 'CAPC-0805-X-NF1-V50', 'CAPC-0805-X-NF20-V50', 'CAPC-0805-X-NF2-V50', 'CAPC-0805-X-NF30-V50', 'CAPC-0805-X-NF3-V50', 'CAPC-0805-X-NF47D-V50', 'CAPC-0805-X-NF5-V50', 'CAPC-0805-X-NF70-V50', 'CAPC-0805-X-NF7-V50', 'CAPC-0805-X-NF8-V50', 'CAPC-0805-X-PF100-V50', 'CAPC-0805-X-PF10-V50', 'CAPC-0805-X-PF12-V50', 'CAPC-0805-X-PF20-V50', 'CAPC-0805-X-PF22-V50', 'CAPC-0805-X-PF30-V50', 'CAPC-0805-X-PF3-V50', 'CAPC-0805-X-PF50-V50', 'CAPC-0805-X-PF5-V50', 'CAPC-0805-X-PF70-V50', 'CAPC-0805-X-PF7-V50', 'CAPC-0805-X-PF8-V50', 'CAPC-0805-X-UF10-V25', 'CAPC-0805-X-UF10-V50', 'CAPC-0805-X-UF1-V50', 'CAPC-0805-X-UF2-V50', 'CAPC-0805-X-UF47D-V25', 'CAPC-0805-X-UF7-V63D', 'CAPC-1206-X-NF100-V50', 'CAPC-1206-X-NF10-V50', 'CAPC-1206-X-NF1-V2000', 'CAPC-1206-X-NF1-V500', 'CAPC-1206-X-NF20-V50', 'CAPC-1206-X-UF100-V63D', 'CAPC-1206-X-UF10-V50', 'CAPC-1206-X-UF1-V50', 'CAPC-1206-X-UF2-V10', 'CAPC-1206-X-UF2-V25', 'CAPC-1206-X-UF2-V50', 'CAPC-1206-X-UF47D-V50', 'CAPC-1206-X-UF7-V10', 'ICIC-SC16-X-K2003-01', 'ICIC-SC18W-X-K2803-01', 'MOSN-SO23-X-K2N7002-01', 'MOSN-SO23-X-KAO3400A-01', 'MOSP-SO23-X-KAO3401A-01', 'MOSP-SO23-X-KSI2301CDS-01', 'RESE-0805-X-O163-01', 'TRNN-SO23-X-K5551-01', 'TRNN-SO23-X-KD882-01', 'TRNN-SO23-X-KMMBT2222A-01', 'TRNN-SO23-X-KMMBT3904-01', 'TRNN-SO23-X-KS8050-01', 'TRNN-SO23-X-KS9013-01', 'TRNN-SO23-X-KSS8050-01', 'TRNP-SO23-X-KB772-01', 'TRNP-SO23-X-KMMBT5401-01', 'TRNP-SO23-X-KS8550-01', 'TRNP-SO23-X-KS9012-01', 'TRNP-SO23-X-KS9015-01', 'TRNP-SO23-X-KSS8550-01', 'XTAL-3215-X-KZ327D-01', 'XTAL-5032-X-MZ11-01']})


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

