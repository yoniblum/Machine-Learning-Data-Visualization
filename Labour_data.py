import matplotlib.pyplot as plt
import numpy as np
import csv as csv

"""
This program preprocesses correlates and plots data 


"""


with open('labour_data.csv','r') as f:
    reader = csv.reader(f)
    count=0
    database_of_tuples=[]
    finalVector=[]
    for row in reader:
        #each row represents a tuple in our database
        #our schema is as follows: [year,province,employment_status,industry,sex,age_group,value]
        
        informationVector=row[0:7] #creating a vector for each chart using relevant info (indices 0-6)
        
        #print(informationVector[0])
        
        
        year=informationVector[0] #2014-2019
        province=informationVector[1] #10 provinces stored as strings
        employment_status=informationVector[2]
        industry=informationVector[3]
        sex=informationVector[4]
        age=informationVector[5]
        value=informationVector[6].strip()
        
        #every attribute is stored as string
        #we will change this for year,and value in this if statement
        
        

        if count!=0: #first column is title
            
            year=int(year)
            
            if len(value)==0:
                value=0 #assuming no data means zero (I know null!=0)
                value=float(value) #the rest can remain strings
            else:
                value=float(value)
                
            
        ###########
        finalVector=[year,province,employment_status,industry,sex,age,value]
        
        database_of_tuples.append(finalVector)
        
        count=count+1
    ######### DONE PREPROCESSING THE DATA AND INSERTING IT INTO A NUMPY ARRAY 
    
    statcan=np.array(database_of_tuples)
    
    #this is a 7x16201 numpy array where the first element is the database schema 
    #and all the following elements are tuples representing the data
    
    #turn numpy array into relational database with sql?
    #https://stackoverflow.com/questions/18621513/python-insert-numpy-array-into-sqlite3-database
    
    ###KEY
    

    
#    List of 23 industry categories
    
#Agriculture [111-112, 1100, 1151-1152]
#Forestry and logging and support activities for forestry [113, 1153]
#Fishing, hunting and trapping [114]
#Mining, quarrying, and oil and gas extraction [21, 2100]
#Utilities [22]
#Construction [23]
#Manufacturing [31-33]
#Durables [321, 327, 331-339]
#Non-durables [311-316, 322-326]
#Wholesale trade [41]
#Retail trade [44-45]
#Transportation and warehousing [48-49]
#Finance and insurance [52]
#Real estate and rental and leasing [53]
#Professional, scientific and technical services [54]
#Business, building and other support services [55, 56]
#Educational services [61]
#Health care and social assistance [62]
#Information, culture and recreation [51, 71]
#Accommodation and food services [72]
#Other services (except public administration) [81]
#Public administration [91]
#Unclassified industries
    
    
    
    
    
    
    
    
    #for plotting purposes:
    
    #Prompt the user to query for specific information
    #ideally this would be done with a GUI, however done like this due to time constraints
    #changing the code in the loop can be done for faster query results
    
    #CREATE THE RELEVANT HASHMAPS FOR EASY HISTOGRAM PLOTTING
    unemployment_by_industry={}  
    employment_by_industry={} # for total data on industries
    
    #for plotting purposes:
    
    employment_by_industry_1={}
    employment_by_industry_2={}
    employment_by_industry_3={}
    employment_by_industry_4={}
    
    unemployment_by_industry_1={}
    unemployment_by_industry_2={}
    unemployment_by_industry_3={}
    unemployment_by_industry_4={}
    
    
    employment_by_gender={"Males":0,"Females":0}
    unemployment_by_gender={"Males":0,"Females":0}
    
    
    employment_by_age_group={"15 to 24 years":0,"25 to 54 years":0,"55 years and over":0}
    unemployment_by_age_group={"15 to 24 years":0,"25 to 54 years":0,"55 years and over":0}
    
    unemployment_by_year ={2014: 0, 2015: 0, 2016: 0, 2017: 0, 2018: 0,2019: 0} 
    employment_by_year ={2014: 0, 2015: 0, 2016: 0, 2017: 0, 2018: 0,2019: 0}

    
    #Prompting user
    
    print("Would you like to see Employment data or Unemployment data?")
    print("Enter Employment or Unemployment: ")
    emp=input()
    
    print("Would you like to pivot based on industry, age, year, or sex?")
    print("Enter i,a,y, or s for each respective option: ")

    grouping=input()

    
    print("Which province would you like to see the data for?")
    print("Enter name of province (capitalized), or All if you would like to see data for all provinces")
    prov=input()
    
    if prov!="Ontario" and prov!="Quebec" and prov!="Prince Edward Island" and prov!="Newfoundland and Labrador" and prov!="Nova Scotia" and prov!="New Brunswick" and prov!="Alberta" and prov!="Manitoba" and prov!="Saskatchewan" and prov!="British Columbia":
        prov="Canada"
    
    
    if grouping=="y":
        print("Would you like to choose another pivot?")
        print("Y/N")
        userAnswer=input()
        if userAnswer=="Y":
            print("Would you like to pivot based on industry, age or sex?")
            print("Enter i,a, or s for each respective option: ")
            pivot=input()
            
            if pivot=="i":
                print("Which industry? Choose from list lines 82-105")
                piv=input()
                
            elif pivot=="a":
                print("Which age Group? (15 to 24 years), (25 to 54 years),(55 years and over)")
                piv=input()
            
            else: #pivot==s
                print("Which gender? Males or Females?")
                piv=input()
            
        else: 
            pivot="none"
            print("Ok...")
            
        
        
        
        
        
    #pivot by age, gender, demographic, ethnicity
        
    
    count=0
    
    #Main loop for data extraction
    
    for data in database_of_tuples:#instead of statcan
        
        
        if count!=0: #first tuple is the schema
            
            year=data[0] #2014-2019
            province=data[1] #10 provinces stored as strings
            employment_status=data[2] #Employment/Unemployment
            industry=data[3] #there is a list of industries //possibly print out for each
            sex=data[4]
            age=data[5]
            value=data[6]
            
            
            #data_by_industry is created here 
            # same as select distinct industry from data_list 
            
            
            if employment_status=="Employment":
                
                if prov=="Canada":
                    
                    
                    ###Industry Pivot
                
                    if industry not in employment_by_industry.keys():
                        employment_by_industry.update({industry:value})
                        
                        if len(employment_by_industry)<6:
                            employment_by_industry_1.update({industry:value})
                        elif len(employment_by_industry)<12:
                            employment_by_industry_2.update({industry:value})
                        elif len(employment_by_industry)<18:
                            employment_by_industry_3.update({industry:value})
                        else:
                            employment_by_industry_4.update({industry:value})
                    

                    else:
                    
                        employment_by_industry[industry]=employment_by_industry[industry]+value
                        if industry in employment_by_industry_1.keys():
                            employment_by_industry_1[industry]=employment_by_industry_1[industry]+value
                        elif industry in employment_by_industry_2.keys():
                            employment_by_industry_2[industry]=employment_by_industry_2[industry]+value
                        elif industry in employment_by_industry_3.keys():
                            employment_by_industry_3[industry]=employment_by_industry_3[industry]+value
                        else:
                            employment_by_industry_4[industry]=employment_by_industry_4[industry]+value
                            
                    employment_by_gender[sex]=employment_by_gender[sex]+value
                    employment_by_age_group[age]=employment_by_age_group[age]+value
                    
                    #employment by year data
                    if pivot=="none":
                        employment_by_year[year]=employment_by_year[year]+value
                    
                    elif pivot=="s":
                        if sex==piv:
                            employment_by_year[year]=employment_by_year[year]+value
                    elif pivot=="i":
                        if piv==industry:
                            employment_by_year[year]=employment_by_year[year]+value
                    else: 
                        if piv==age:
                            employment_by_year[year]=employment_by_year[year]+value
                            
                        
                    
                else: #for province based data

                    if industry not in employment_by_industry.keys() and province==prov:
                        employment_by_industry.update({industry:value})
                        
                        if len(employment_by_industry)<6:
                            employment_by_industry_1.update({industry:value})
                        elif len(employment_by_industry)<12:
                            employment_by_industry_2.update({industry:value})
                        elif len(employment_by_industry)<18:
                            employment_by_industry_3.update({industry:value})
                        else:
                            employment_by_industry_4.update({industry:value})
    
                    elif province==prov:
                        
                        employment_by_industry[industry]=employment_by_industry[industry]+value
                        if industry in employment_by_industry_1.keys():
                            employment_by_industry_1[industry]=employment_by_industry_1[industry]+value
                        elif industry in employment_by_industry_2.keys():
                            employment_by_industry_2[industry]=employment_by_industry_2[industry]+value
                        elif industry in employment_by_industry_3.keys():
                            employment_by_industry_3[industry]=employment_by_industry_3[industry]+value
                        else:
                            employment_by_industry_4[industry]=employment_by_industry_4[industry]+value
                            
                    if province==prov:
                        employment_by_gender[sex]=employment_by_gender[sex]+value
                        employment_by_age_group[age]=employment_by_age_group[age]+value
                        
                        
                        if pivot=="none":
                            employment_by_year[year]=employment_by_year[year]+value
                        
                        elif pivot=="s":
                            if sex==piv:
                                employment_by_year[year]=employment_by_year[year]+value
                        elif pivot=="i":
                            if piv==industry:
                                employment_by_year[year]=employment_by_year[year]+value
                        else: 
                            if piv==age:
                                employment_by_year[year]=employment_by_year[year]+value
                    
                    
                 
                    
                        
            elif employment_status=="Unemployment":#unemployment
                
                if prov=="Canada":
                    
                    if industry not in unemployment_by_industry.keys():
                        unemployment_by_industry.update({industry:value})
                        if len(unemployment_by_industry)<6:
                            unemployment_by_industry_1.update({industry:value})
                        elif len(unemployment_by_industry)<12:
                            unemployment_by_industry_2.update({industry:value})
                        elif len(unemployment_by_industry)<18:
                            unemployment_by_industry_3.update({industry:value})
                        else:
                            unemployment_by_industry_4.update({industry:value})
                            
                        
                    else:
                        unemployment_by_industry[industry]=unemployment_by_industry[industry]+value
                        if industry in unemployment_by_industry_1.keys():
                            unemployment_by_industry_1[industry]=unemployment_by_industry_1[industry]+value
                        elif industry in unemployment_by_industry_2.keys():
                            unemployment_by_industry_2[industry]=unemployment_by_industry_2[industry]+value
                        elif industry in unemployment_by_industry_3.keys():
                            unemployment_by_industry_3[industry]=unemployment_by_industry_3[industry]+value
                        else:
                            unemployment_by_industry_4[industry]=unemployment_by_industry_4[industry]+value
                            
                    unemployment_by_gender[sex]=unemployment_by_gender[sex]+value
                    unemployment_by_age_group[age]=unemployment_by_age_group[age]+value
                    
                    
                    if pivot=="none":
                            unemployment_by_year[year]=employment_by_year[year]+value
                        
                    elif pivot=="s":
                        if sex==piv:
                            unemployment_by_year[year]=employment_by_year[year]+value
                    elif pivot=="i":
                        if piv==industry:
                            unemployment_by_year[year]=employment_by_year[year]+value
                    else: 
                        if piv==age:
                            unemployment_by_year[year]=employment_by_year[year]+value
                    
                    
                    
                    
                else: #for province based data
                    if industry not in unemployment_by_industry.keys() and province==prov:
                        unemployment_by_industry.update({industry:value})
                        
                        if len(unemployment_by_industry)<6:
                            unemployment_by_industry_1.update({industry:value})
                        elif len(unemployment_by_industry)<12:
                            unemployment_by_industry_2.update({industry:value})
                        elif len(unemployment_by_industry)<18:
                            unemployment_by_industry_3.update({industry:value})
                        else:
                            unemployment_by_industry_4.update({industry:value})
                            
                        
                    elif province==prov:
                        unemployment_by_industry[industry]=unemployment_by_industry[industry]+value
                        if industry in unemployment_by_industry_1.keys():
                            unemployment_by_industry_1[industry]=unemployment_by_industry_1[industry]+value
                        elif industry in unemployment_by_industry_2.keys():
                            unemployment_by_industry_2[industry]=unemployment_by_industry_2[industry]+value
                        elif industry in unemployment_by_industry_3.keys():
                            unemployment_by_industry_3[industry]=unemployment_by_industry_3[industry]+value
                        else:
                            unemployment_by_industry_4[industry]=unemployment_by_industry_4[industry]+value
                    if province==prov:
                        unemployment_by_gender[sex]=employment_by_gender[sex]+value
                        unemployment_by_age_group[age]=employment_by_age_group[age]+value
                        
                        if pivot=="none":
                            unemployment_by_year[year]=employment_by_year[year]+value
                        
                        elif pivot=="s":
                            if sex==piv:
                                unemployment_by_year[year]=employment_by_year[year]+value
                        elif pivot=="i":
                            if piv==industry:
                                unemployment_by_year[year]=employment_by_year[year]+value
                        else: 
                            if piv==age:
                                unemployment_by_year[year]=employment_by_year[year]+value
                    
        count=count+1
        
        
    
        
        
        
        
    
        
    #### end of for loop
    
    
   
    
    
    #same number of tuples for each year, 6 years
    #all results are averages, besides for the yearly groupings
    
    for a in unemployment_by_industry:
        unemployment_by_industry[a]=unemployment_by_industry[a]/6  
    
    for b in employment_by_industry:
        employment_by_industry[b]=employment_by_industry[b]/6
        
    for c in unemployment_by_gender:
        unemployment_by_gender[c]=unemployment_by_gender[c]/6
    
    for d in employment_by_gender:
        employment_by_gender[d]=employment_by_gender[d]/6
        
    for e in unemployment_by_age_group:
        unemployment_by_age_group[e]=unemployment_by_age_group[e]/6
    
    for f in employment_by_age_group:
        employment_by_age_group[f]=employment_by_age_group[f]/6
        
    
    #subplot is preferable
    
     ###Graphing data 
     
    print(unemployment_by_industry)
    print(employment_by_industry)
    
    
    if emp=="Employment":
        
        if grouping=="i":
            plt.bar(employment_by_industry.keys(), employment_by_industry.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Employment in '+prov+' from 2014-2019')
            plt.xlabel('Industry')
            plt.ylabel('Employment (x1000)')
            plt.xticks(rotation='vertical')
            plt.show()
            
            
            plt.bar(employment_by_industry_1.keys(), employment_by_industry_1.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Employment in '+prov+' from 2014-2019')
            plt.xlabel('Industry')
            plt.ylabel('Employment (x1000)')
            plt.xticks(rotation='vertical')
            plt.show()
            
            plt.bar(employment_by_industry_2.keys(), employment_by_industry_2.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Employment in '+prov+' from 2014-2019')
            plt.xlabel('Industry')
            plt.ylabel('Employment (x1000)')
            plt.xticks(rotation='vertical')
            plt.show()
            
            plt.bar(employment_by_industry_3.keys(), employment_by_industry_3.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Employment in '+prov+' from 2014-2019')
            plt.xlabel('Industry')
            plt.ylabel('Employment (x1000)')
            plt.xticks(rotation='vertical')
            plt.show()
            
            plt.bar(employment_by_industry_4.keys(), employment_by_industry_4.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Employment in '+prov+' from 2014-2019')
            plt.xlabel('Industry')
            plt.ylabel('Employment (x1000)')
            plt.xticks(rotation='vertical')
            plt.show()
        elif grouping=="s":
            plt.bar(employment_by_gender.keys(), employment_by_gender.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Employment in '+prov+' from 2014-2019')
            plt.xlabel('Gender')
            plt.ylabel('Employment (x1000)')
            
            plt.show()
        elif grouping=="y":
            plt.bar(employment_by_year.keys(), employment_by_year.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Employment in '+prov+' by year for '+piv)
            plt.xlabel('Year')
            plt.ylabel('Employment (x1000)')
            
        else: 
            plt.bar(employment_by_age_group.keys(), employment_by_age_group.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Employment in '+prov+' from 2014-2019')
            plt.xlabel('Age Groups')
            plt.ylabel('Employment (x1000)')
            
            plt.show()
            
            
    else: #for unemployment
        
        
        if grouping=="i":
            plt.bar(unemployment_by_industry.keys(), unemployment_by_industry.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Unmployment in '+prov+' from 2014-2019')
            plt.xlabel('Industry')
            plt.ylabel('Unemployment (x1000)')
            plt.xticks(rotation='vertical')
            plt.show()
            
            
            plt.bar(unemployment_by_industry_1.keys(), unemployment_by_industry_1.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Unmployment in '+prov+' from 2014-2019')
            plt.xlabel('Industry')
            plt.ylabel('Unemployment (x1000)')
            plt.xticks(rotation='vertical')
            plt.show()
            
            plt.bar(unemployment_by_industry_2.keys(), unemployment_by_industry_2.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Unmployment in '+prov+' from 2014-2019')
            plt.xlabel('Industry')
            plt.ylabel('Unemployment (x1000)')
            plt.xticks(rotation='vertical')
            plt.show()
            
            plt.bar(unemployment_by_industry_3.keys(), unemployment_by_industry_3.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Unemployment by Industry for '+prov+" from 2014-2019")
            plt.xlabel('Industry')
            plt.ylabel('Unemployment (x1000)')
            plt.xticks(rotation='vertical')
            plt.show()
            
            plt.bar(unemployment_by_industry_4.keys(), unemployment_by_industry_4.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Unmployment in '+prov+' from 2014-2019')
            plt.xlabel('Industry')
            plt.ylabel('Unemployment (x1000)')
            plt.xticks(rotation='vertical')
            plt.show()
        elif grouping=="s":
            plt.bar(unemployment_by_gender.keys(), unemployment_by_gender.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Unmployment in '+prov+' from 2014-2019')
            plt.xlabel('Gender')
            plt.ylabel('Unemployment (x1000)')
            
            plt.show()
        elif grouping=="y":
            plt.bar(unemployment_by_year.keys(), unemployment_by_year.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Employment in '+prov+' by year for '+piv)
            plt.xlabel('Year')
            plt.ylabel('Employment (x1000)')
        else: #grouping==age
            plt.bar(unemployment_by_age_group.keys(), unemployment_by_age_group.values(), align='center')
            plt.autoscale(enable=True, axis='both', tight=None)
            plt.title('Average Unmployment in '+prov+' from 2014-2019')
            plt.xlabel('Age Group')
            plt.ylabel('Unemployment (x1000)')
            
            plt.show()
            
            
            
        
        
        
        
       
    
    
    
    
    
    
        
            
    
    

            
            
    




        
        
    
        
        
        
        
        
    