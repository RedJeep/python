#!C:\Python27\python.exe
''' 
cs1114
Submission: hw 06
Programmer: Jeffrey Garip
Username: Jwg327@nyu.edu
create function records NASA data entry an inhabited planet 
'''
def numTrans():
    ''' asks user for number of transmitions they will process'''
    num=int(raw_input("how many transmistions:?"))
    while num<0:
        num=int(raw_input( "Sorry must be 1 or more. Try again:"))

    return num 

def dataEntry(num,lstTemp):
    ''' ask usr for data entry based on numbers'''
    print("New Data Entry")
    lstTemp=[]
    while True:
        inp=raw_input('enter temp')
        if(inp=='stop'):
            break
        else:
            temp=float(inp)
            if(temp<=-33.4 or temp>=33.4):
                print("Rejected!",temp)
            lstTemp.append(temp)
        
    return lstTemp    

def calcStats(lstTemp,stats):
    ''' calculates stats based on given numbers'''
    stats=[]
    maxium=-33.24
    minium=33.24
    accumlator=0
    counter=0
    average=0
    removed=0
    for num in lstTemp:
        if num<= -33.34 or num>=33.34:
            lstTemp.remove(num)
            removed+=1.0
        else:
            accumlator+=num 
            counter+=1
    average= accumlator/counter
    rejected=removed/len(lstTemp)
    maxy=max(lstTemp)
    mini=min(lstTemp)
    print ("average:",average)
    print ("percent rejected",rejected)
    print ("the Max value was",max(lstTemp))
    print ("the min value was", min(lstTemp))
    stats.append(average)
    stats.append(rejected)
    stats.append(maxy)
    stats.append(mini)
    
    return stats
    


def main():
    
    lstNFo=[]
    stats=[]
    num=numTrans()
    for val in range(num):
        lstTemp=dataEntry(num,lstNFo)
        stats=calcStats(lstTemp, stats)
        lstNFo.append(stats)
        print lstNFo
    total=0
    for x in lstNFo:
        for y in x:
            total+=y
    average=total/len(x)
    overmax=sum(max(lstNFo))/4
    overmin=sum(min(lstNFo))/4
    print("overall average:",average)
    print( "the overmax value was",overmax)
    print (" the overmin was", overmin)
    
        
        
   
main()
    
