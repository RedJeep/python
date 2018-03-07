#!C:\Python27\python.exe
''' 
cs1114 

Submission: hw02

Programmer: jeffrey Garip
Username: jwg327

purpose of program is to construct bridge brochure
based on the importation of modules given to us

'''
from bridgeBuilders import *
def pauseTheScreen():
    ''' pauses screen awaiting for user input.....'''
    screenPause=raw_input(" to stop the pause Press any key")
def main():
    showBridgeSalesBrochure( )
    pauseTheScreen()
    
if __name__ == '__main__':
    main()
