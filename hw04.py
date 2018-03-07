#!C:\Python27\python.exe
''' 
cs1114 

Submission: hw 04

Programmer: Jeffrey Garip
Username: Jwg327@nyu.edu

create function that returns common elements
'''

def getComElements( lst,lst2):
     ''' compares two list and returns alist with no duplicates '''
     nwlst=[]
     for item in lst:
         if item in lst2:
             nwlst.append(item)

     return nwlst
