'''
cs1114 
Submission: hw 10
Programmer: Jeffrey Garip
Username: Jwg327
create company tester
'''
from comp import *
from comp import DUPLICATE_WORKER
from comp import NON_TITLE_SSN

def main():
    compy=company('Randy&CO')
    compy.alterName('j&j')
    compy.addWorker('joe',3434)
    compy.adjustHrs(1232,3)
    compy.changePay(3434 ,12.50)
    compy.calcPay(3434)

main()


