tmp=''
versionLength=3
typeIDLength=3
with open("input.txt") as data:
    hexString=data.readline()
    for char in hexString:
        tmp+={"0:04b"}.format(str(bin(int(char,16))))
        binaryString=tmp.replace('0b','')
print(binaryString)
binaryList=[]
for char in binaryString:
    binaryList.append(int(char))
print(binaryList)
decoded=[[]]

def decodeNextPacket(index):
    version=''
    typeID=''
    litteralStr=''

def snipInput(index):
    version=int(binaryString[index:index+3],2)
    print("Version: "+str(version))
    index=index+versionLength
    print(index)
    typeID=int(binaryString[index:index+3],2)
    print("TypeID: "+str(typeID))

    
    
snipInput(0)