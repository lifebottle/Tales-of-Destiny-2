import os
from os.path import join
import pandas as pd
import itertools
import ntpath

def hexToJpn(pathTables, word):

    mapping = {}

    fo = open(os.path.abspath(os.path.join(pathTables,
                                            'dictionary//tod2_utf8.txt')), "r", encoding="utf8")
    Lines = fo.readlines()

    for line in Lines:
        mapping[line[0:4]] = line[6]

    for line in Lines:
        if (len(line) > 6):
            mapping[line[0:4]] = line[6]
        else:
            mapping[line[0:2]] = line[4]

    mapping["00"] = " "
    mapping["01"] = "\n"

    Hex = list(word)
    outputText = []
    i = 0
    while i < len(Hex)-1:
        if i + 3 > len(Hex):
            break
        if(Hex[i] + Hex[i+1] + Hex[i+3] + Hex[i+4] in mapping):
            outputText.append(mapping[Hex[i] + Hex[i+1] + Hex[i+3] + Hex[i+4]])
            i += 6
        elif(Hex[i] + Hex[i+1] in mapping):
            outputText.append(mapping[Hex[i] + Hex[i+1]])
            i += 3
        else:
            outputText.append(Hex[i] + Hex[i+1])
            i += 3

    return "".join(outputText)

def convertHex( hexValue):
    val = hexValue.replace(" ", "")
    print("\\x"+"\\x".join([val[i:i+2] for i in range(0, len(val), 2)]))

    
    
#Search if a file is containing one of the elements from the list
def lookForHex(listValues, fileName):

    with open(fileName, 'rb') as f:
        hexdata = f.read().hex()
        
    hexFound = [ele for ele in listValues if ele in hexdata]
    if len(hexFound) > 0:
        val = hexFound[0]
        hexFound2 = "\\x"+"\\x".join([val[i:i+2] for i in range(0, len(val), 2)])
        print(ntpath.basename(fileName) +' ' + val)


#Load the HEX mapping tables from a path
pathTables = r"G:\TalesHacking\TOD2\GitProject\Tales-of-Destiny-2"

dfKanji = pd.read_csv(os.path.join(pathTables,"dictionary","tod2_utf8.txt"), sep=",", header=None, names=['hex', 'value'])
dfSymbols = pd.read_csv(os.path.join(pathTables,"dictionary","tod2_symbols.txt"),  header=None, names=['hex', 'value'], sep=", ", engine='python', encoding='utf-8')
dfSymbols.fillna("",inplace=True)
dfSymbols = dfSymbols.astype(str)


#Make a big table with all the elements
dfAllPoss = pd.concat( [dfKanji, dfSymbols])
dfAllPoss['value'] = dfAllPoss['value'].str.replace(' ', '')



#Stuff to search
japText = '戦闘メンバーに戦闘可能なキャラがいません'
#List all the different possible ways of HEX for this text
df = [ dfAllPoss.loc[dfAllPoss['value'] == character, 'hex'].tolist() for character in japText]
listValues = []
for element in itertools.product(*df):
    listValues.append(('').join(element).lower())

slpsFile = os.path.join(pathTables, "ps2","scripts","abcde", "SLPS_251.72")
lookForHex(listValues, slpsFile)

#For one specific file
#file1 = r"F:\PythonCode\TOD_GoogleDoc\abcde\SLPS_258.42"

#listFiles = os.listdir(pathTables+"/../patch/DAT_FILES/")
#listFiles = [join(pathTables+"/../patch/DAT_FILES/"+file) for file in listFiles]
#listFiles.append(file1)

folderList = ['DAT_FILES', 'ENEM', 'PAK0','PAK1', 'PAK3']
allDir = [ os.path.join(pathTables, "../patch", ele) for ele in folderList]

for myDir in allDir:
    for file in os.listdir(myDir):
        lookForHex(listValues,myDir+"/"+file)
        
        
hexJp = "25 64"

hexToJpn(pathTables, hexJp)