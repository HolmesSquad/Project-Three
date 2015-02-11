def quickSortDes(fullList):
   quickSortHelperDes(fullList,0,len(fullList)-1)

def quickSortHelperDes(fullList,first,last):
   if first < last:

       splitpointQD = partitionDes(fullList,first,last)

       quickSortHelperDes(fullList, first, splitpointQD - 1)
       quickSortHelperDes(fullList, splitpointQD + 1, last)


def partitionDes(fullList, first, last):
   pivotQD = fullList[first]

   leftMarkQD = first + 1
   rightMarkQD = last

   finishedQD = False
   while finishedQD == False:

       while leftMarkQD <= rightMarkQD and fullList[leftMarkQD] >= pivotQD:
            leftMarkQD += 1

       while fullList[rightMarkQD] <= pivotQD and rightMarkQD >= leftMarkQD:
           rightMarkQD += -1

       if rightMarkQD < leftMarkQD:
           finishedQD = True
       else:
           tempVarQD = fullList[leftMarkQD]
           fullList[leftMarkQD] = fullList[rightMarkQD]
           fullList[rightMarkQD] = tempVarQD

   tempVarQD = fullList[first]
   fullList[first] = fullList[rightMarkQD]
   fullList[rightMarkQD] = tempVarQD


   return rightMarkQD


def quickSortAsc(fullList):
   quickSortHelperAsc(fullList,0,len(fullList)-1)

def quickSortHelperAsc(fullList,first,last):
   if first < last:

       splitpointQA = partitionAsc(fullList,first,last)

       quickSortHelperAsc(fullList, first, splitpointQA - 1)
       quickSortHelperAsc(fullList, splitpointQA + 1, last)


def partitionAsc(fullList, first, last):
   pivotQA = fullList[first]

   leftMarkQA = first + 1
   rightMarkQA = last

   finishedQA = False
   while finishedQA == False:

       while leftMarkQA <= rightMarkQA and fullList[leftMarkQA] <= pivotQA:
            leftMarkQA += 1

       while fullList[rightMarkQA] >= pivotQA and rightMarkQA >= leftMarkQA:
           rightMarkQA += -1

       if rightMarkQA < leftMarkQA:
           finishedQA = True
       else:
           tempVarQA = fullList[leftMarkQA]
           fullList[leftMarkQA] = fullList[rightMarkQA]
           fullList[rightMarkQA] = tempVarQA

   tempVarQA = fullList[first]
   fullList[first] = fullList[rightMarkQA]
   fullList[rightMarkQA] = tempVarQA


   return rightMarkQA


fullList = [54,26,93,17,77,31,44,55,20,1,2,3,4,89,99,89,44,335]
quickSortAsc(fullList)
print(fullList)


fullList = [54,26,93,17,77,31,44,55,20,1,2,3,4,89,99,89,44,335]
quickSortDes(fullList)
print(fullList)
