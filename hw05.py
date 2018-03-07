#!C:\Python27\python.exe
''' 
cs1114 

Submission: hw 05

Programmer: Jeffrey Garip
Username: Jwg327@nyu.edu

create function that returns common elements
'''
def getPostion( lst,lsty):
     ''' compares two list and returns one list list based on smilar position'''
     fst=[]
     sec=[]
     lstNlst=[]
     for item in range(len(lst)):
        if lst[item] in lsty:
            fst.append(item)
            print fst

     for index in range(len(lsty)):
         if lsty[index] in lst:
             sec.append(index)


     lstNlst.append(fst)
     lstNlst.append(sec)

     return  lstNlst
     
    
     


