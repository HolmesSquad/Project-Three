#Ascending
def mergeSortAsc(fullList):
    if len(fullList) > 1:
        midMA = len(fullList) // 2
        lHalfMA = fullList[:midMA]
        rHalfMA = fullList[midMA:]

        mergeSortAsc(lHalfMA)
        mergeSortAsc(rHalfMA)

        aMA = 0
        bMA = 0
        cMA = 0

        while aMA < len(lHalfMA) and bMA < len(rHalfMA):
            if lHalfMA[aMA] < rHalfMA[bMA]:
                fullList[cMA] = lHalfMA[aMA]
                aMA += 1
                
            else:
                fullList[cMA] = rHalfMA[bMA]
                bMA += 1
            cMA += 1

        while aMA < len(lHalfMA):
            fullList[cMA] = lHalfMA[aMA]
            aMA += 1
            cMA += 1

        while bMA < len(rHalfMA):
            fullList[cMA] = rHalfMA[bMA]
            bMA += 1
            cMA += 1


        
                
#Descending 
def mergeSortDes(fullList):
    if len(fullList) > 1:
        midMD = len(fullList) // 2
        lHalfMD = fullList[:midMD]
        rHalfMD = fullList[midMD:]

        mergeSortDes(lHalfMD)
        mergeSortDes(rHalfMD)

        aMD = 0
        bMD = 0
        cMD = 0

        while aMD < len(lHalfMD) and bMD < len(rHalfMD):
            if lHalfMD[aMD] > rHalfMD[bMD]:
                fullList[cMD] = lHalfMD[aMD]
                aMD += 1
                
            else:
                fullList[cMD] = rHalfMD[bMD]
                bMD += 1
            cMD += 1

        while aMD > len(lHalfMD):
            fullList[cMD] = lHalfMD[aMD]
            aMD += 1
            cMD += 1

        while bMD > len(rHalfMD):
            fullList[cMD] = rHalfMD[bMD]
            bMD += 1
            cMD += 1

fullList = [12,32,43,56,876,654,654,387654,765,54,675,54,423,45,65,76,87,65,3,32,1]
mergeSortAsc(fullList)
print fullList

fullList = [12,32,43,56,876,654,654,387654,765,54,675,54,423,45,65,76,87,65,3,32,1]
mergeSortDes(fullList)
print fullList
        
                
 
