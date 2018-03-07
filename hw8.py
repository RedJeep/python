''' 
cs1114 
Submission: hw08
Programmer:Jeffrey Garip
Username: Jwg327
purpose is to create files that show percent change of data over time

'''

PER_1970='1970-1990'
PER_1990='1990-2007'




def readData():
    ''' reads data from file'''
    fh=open("UNDATA.txt",'r')
    data=fh.read()
    print data


def parseFile():
    ''' parses file'''
    allcountries=[]
    fh=open("UNDATA.txt",'r')
    lines=fh.readlines()
    lines.pop(0)
    lines.pop(len(lines)-1)
    for line in lines:
        allcountries.append(parseLine(line))
    countries1970=[]
    countries1990=[]
    for country in allcountries:
        if country[1]==PER_1970:
            countries1970.append(country)
        else:
            countries1990.append(country)
    fh.close()
    return countries1970,countries1990

def parseLine(line):
    ''' parses line'''
    countryList=line.split(',')
    name=countryList[0].strip(',')
    PeriodPercent=countryList[1].split()
    period=PeriodPercent[0]
    percent=PeriodPercent[1].strip('%')
    parsedList=[name,period,percent]
    return parsedList

def findAverage(countryList):
    ''' finds average'''
    total=0.0
    for country in countryList:
        total+=float(country[2])
    average= total/len(countryList)
        


def highNlow(countryList):
    ''' displays highest averages'''
    largest=countryList[0]
    twolargest=[]
    thirdlargest =[]
    smallest =countryList[0]
    twosmallest = []
    thirdsmallest=[]
    for country in countryList:
        if abs(float(country[2]))>abs(float(largest[2])):
            thirdlargest = twolargest
            twolargest = largest
            largest = country
        if abs(float(country[2]))<abs(float(smallest[2])):
            thirdsmallest =twosmallest
            twosmallest =smallest
            smallest = country
    return [largest, twolargest, thirdlargest, smallest, twosmallest, thirdsmallest]





def writeFile(filename, average, highsNlows):
    ''' takes info from 1970-1990 and creates file based on that data.\n
#based on that data it will display countries numberic value in desending order'''
    fh=open(filename,"w")
    fh.write(filename.strip('.txt')+"_report\n")
    fh.write('Average percent change over all: '+str(average)+'\n')
    fh.write('The three countries or regions with the largest change:\n')
    count = 00
    while count !=3:
        fh.write(highsNlows[count][0]+ ', ('+ str(highsNlows[count][2])+'%) ')
        count+=1
    fh.write('\nThe three countries or regions with the smallest change:\n')
    while count !=6:
        fh.write(highsNlows[count][0]+ ', ('+ str(highsNlows[count][2])+'%) ')
        count+=1
    fh.write('\n')
    fh.close()
    



    
    
    


def main():
    countryList1970,countryList1990  = parseFile()
    average1970=findAverage(countryList1970)
    average1990=findAverage(countryList1990)
    highNlow1970=highNlow(countryList1970)
    highNlow1990=highNlow(countryList1990)
    writeFile('1970_1990_summary.txt',average1970,highNlow1970)
    writeFile('1990_2007_summary.txt',average1990,highNlow1990)

main()
