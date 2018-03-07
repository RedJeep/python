'''
cs1114 
Submission: hw 10
Programmer: Jeffrey Garip
Username: Jwg327
create company class using Worker class
'''
from workerRec  import PAYRATE_ERROR
from workerRec import HOURS_ERROR
from workerRec import *
DUPLICATE_WORKER=9
NON_TITLE_SSN=999999999 



class company(object):
    ''' contains company name and workers'''
    def __init__(self,compName):
        self.__=compName
        self.__workers={}
        self.__NewWorker=NON_TITLE_SSN

    def alterName(self,newName):
        ''' alters companies name'''
        self.__compName=newName
        return self.__compName
    def checkIfWorkerInDic(self, ssn):
        ''' returns true if worker in in ssn in dictonary'''
        return ssn in self._workers

    def addWorker(self,name,ssn,pay=0,title=NON_TITLE_SSN):
        self.__ssn=ssn
        self.__name=name
        if checkIfWorkerInDic(ssn) is True:
            return DUPLICATE_WORKER
        oneEmp=worker(name,ssn,payrate,title)
        self.__workers[ssn]=oneEmp
        return snn
    def adjustHrs(self,ssn,hours):
        ''' adjust hours'''
        self.__workers[ssn].placedHrs(ssn,hours)

    def  changePay(self,ssn,pay):
        ''' changes the pay rate using method from WorkerREC module'''
        if pay>payrate:
            return "rate higher than High payable rate"
        else:
            self.workers[ssn].changePay(pay)

    def promoTitle(self,ssn,title):
        self.__employees[ssn].alterTitle(title)

    def calcPay(self,snn):
        ''' calculates pay by mullitplying hours with pay Rate'''
        return self.__workers[ssn].getHours()*self.__workers[ssn].getPayrate()

    def payAll(self):
        ''' outputs data into a file with company name and  SSN as a file name
            for bank purposes when all employs are paid there pay resets to zero'''

        filenames = '%a-%z.txt' %(self.__companyName,self.__ssn )
        if os.path.exists(filenames):
            output=open(filenames, 'a')
        else:
            output=open(filenames, 'w')
        for ssn in self.__workers:
            output.write(ssn+'\n')
            pay=self.calcPay(ssn)
            output.write(self.__employee[ssn].getTitle()+' $%.02f ' %pay +'\n')
            self.__employees[ssn].changepay(pay)
        output.close()

        
    def fireWorker(self, ssn):
        '''
         fire  worker(Q)   - fires a worker by paying the person first,record it to
        the accounting file. then delete the employee from the database
        takes one parameter: ssn        
        '''
        filenames='%a-%z.txt' %(self.__companyName, self.__ssn)
        if os.path.exists(filenames):
            output=open(filenames, 'a')
        else:
            output=open(filenames, 'w')
        pay=self.calcPay(ssn)
        output.write(str(ssn)+'\n')
        output.write(self.__employee[ssn].getTitle()+' $%.02f ' %pay )
        output.close()
        self.__employee.split(ssn)
    
    
    
        
        
        
        
        
    
