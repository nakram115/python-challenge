'Create pathway and read data'
import os
import csv

def getTtlRev(years_dict):
    ttlRev = 0
    for year in years_dict:
        i = 1
        for item in years_dict[year]:
            if i % 2 == 0:
                ttlRev = ttlRev + int(item)
            i += 1
    return(ttlRev)

def get_rev_change(years_dict):
    rev_list = []
    month_list = []
    for year in years_dict:
        i=0
        for element in years_dict[year]:
            if i % 2 != 0:
                rev_list.append(int(element))
            else: # save month info
                month_list.append(year+'-'+element)
            i+=1
    z=[b-a for a,b in zip(rev_list,rev_list[1:])]
    minIdx = z.index(min(z))
    min_ = min(z)
    min_mnth = month_list[minIdx+1]
    maxIdx = z.index(max(z))
    max_mnth = month_list[maxIdx+1]
    max_ = max(z)
    avg = sum(z)/len(z)
    o = "Avg change in revenue "+str(avg)+'\n'
    o = o + "Greatest increase in revenue: "+max_mnth+' '+\
         str(max_)+'\n'
    o = o + "Greatest decrease in revenue: "+min_mnth+' '+\
        str(min_)+'\n'
    return(o)


data_files = ['budget_data_1.csv','budget_data_2.csv']

for fname in data_files:
    csvpath = os.path.join('raw_data', fname)

    with open(csvpath, newline='') as csvfile:

        # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')

        #print(csvreader)

        # Set the variables
        Date=[]
        Revenue=[]

        #Append the data
        Date=[0]
        Revenue=[1]


        #  Each row is read as a row
        years = {} #This will hold all file data in term of dictionary
        count = 0
        ttl_months = 0
        for row in csvreader:
            if len(row[0])==6:
                s=4
            else:
                s=6
            if count == 0: 
                count += 1
                continue #1st row is header, don't need it
            ttl_months += 1
            if not row[0][s:] in years:
                years[row[0][s:]]=[row[0][0:3],int(row[1])]
            else:
                years[row[0][s:]].extend([row[0][0:3],int(row[1])])
        rev_change_output = get_rev_change(years)
        print(rev_change_output)
        ttlRev = getTtlRev(years)
        print("Total rev is: "+str(ttlRev))
        print(str(ttl_months)+" Months")
    
        filename= fname[0:-4] + ".txt"
        with open (filename,'w') as f:
            f.write("Financial Analysis\n")
            f.write("Total amount of months:" + " " + str(ttl_months)+'\n')
            f.write("Total Revenue: " + str(ttlRev) + '\n')
            f.write(rev_change_output)    

        





