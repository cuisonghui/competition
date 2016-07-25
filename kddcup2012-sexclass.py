from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import preprocessing
from sklearn import tree

featureList=[]
labelList=[]

allElectronicsData = open('/Users/yihui/Downloads/track2/training.txt', 'r')
lines = allElectronicsData.readline()
#print(lines)


headers = lines.split()

for lines in allElectronicsData:
    strs = lines.split()
    print strs
    print strs[7],strs[11]
    #print strs
    #rowDict = {}
    #labelList.append(strs[len(strs)-1])
    #for i in range(1,len(strs)-1):
        #rowDict[headers[i]] = strs[i]
    #featureList.append(rowDict)

print labelList
print featureList
