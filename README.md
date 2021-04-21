# Data-Visualization

Task: 
 
Visualize labour / employment data ((https://www150.statcan.gc.ca/n1/daily-quotidien/190308/dq190308a-eng.htm) for Canada by province and industry for the last 5 years which should be pivotable by demographic (age, sex, ethnicity and industry / sector).
 
Use open skills data and job titles using this link  and visualize a mashup correlating skills and jobs to industry and employment and provide a sample for evaluation.
Suggest in detail, how you would train these two data sets over time and what machine learning algorithm you would use to make the data "smarter" over time.
 
 
Method
 
The first step in tackling this type of challenge is to divide the problem into subproblems.  
This challenge consists of a few subproblems.  


Finding a way to visualize the labour and employment data from statcan in a way that represents the data in an informative and clear way.  The data should be complete and accurate.  
 
Constraints: I am only going to use the data given by Statcan, which may limit the data that is being represented.  (More on this later) ** Age as classification rather than as continuous variable
 
My goal is to write a program which allows the users to pivot the data in a way that shows all the data 
 
Use the “job titles”, and “skills” datasets to build a relational database to generate an understanding of the dataset
Visualize mashup correlating the statcan dataset with the data.world dataset 
Explain an effective Machine Learning algorithm which correlates this data
This will include talking about the “learning process”
 
 
 
 
 
 
 
Part 1 

In order to visualize the data we must first understand the data itself.  
 
Examining the dataset we may see that all the data inputs are formed as classifications.  For example, age is classified in 3 ways: ages 15-24, ages 25-54, and age 55 and over.  
Once the data has been completely compiled into one dataset, it is clear that it can be parameterised in a more efficient manner using SQL queries
 
The Database schema for Dataset 1 is as follows: 
 
LabourData(Date,Province,EmploymentStatus, Industry, Sex, Age_Group, Value)
 
Each row forms a key, which is why they are all underlined.  
 
There are a few other mentioned attributes, however these are not very relevant. They may be eliminated from the chart if we can use the others for groupings.  
SQL may be used to investigate the data to see if we may eliminate unnecessary columns from our dataset.  
We uploaded the relevant 2-3 datasets into our data.world set.  
 
 
 
 
 
 
 
SQL query to show no data loss from eliminating certain columns from our dataset: 
Self join and count distinct tuples (allows us to see if using modified schema will result in data loss)
 
SELECT distinct labourdata1.year,labourdata2.year,labourdata1.province,labourdata2.province,labourdata1.employmentstatus,labourdata2.employmentstatus,
labourdata1.industry,labourdata2.industry, labourdata1.age_group,labourdata2.age_group, labourdata1.value,labourdata2.value,labourdata1.sex,labourdata2.sex
FROM labour_data labourdata1,labour_data labourdata2
where labourdata1.province=labourdata2.province and labourdata1.age_group=labourdata2.age_group
and labourdata1.industry=labourdata2.industry and labourdata1.year=labourdata2.year
and labourdata1.sex=labourdata2.sex and labourdata1.employmentstatus=labourdata2.employmentstatus and labourdata1.province="Ontario" #province can be swapped, all provinces have same number of data tuples
LIMIT 10000
 


No data loss from selecting only those attributes
Delete other attributes and store this much more simple schema since they have redundant information
 
1620 results for each province, same as in other query
 
The next step is getting the data into a form where it can easily be processed  
 
I would have much preferred to have my python code integrated with SQL type queries, however, I was not able to implement this with CSV files, so instead I created my own text processing script.  	
 
 
 
 
 
 
 
 
 
 
 
 
 
Python code:
 
import matplotlib.pyplot as plt
import numpy as np
import csv as csv
with open('labour_data.csv','r') as f:
    reader = csv.reader(f)
    count=0
    database_of_tuples=[]
    finalVector=[]
    for row in reader:
        #each row represents a tuple in our database
        #our schema is as follows: [year,province,employment_status,industry,sex,age_group,value]
        
        informationVector=row[0:7] #creating a vector for each chart using relevant info (indices 0-6)



 
 
Since the data is formed as a classification, histograms are appropriate
We can also use line graphs.
 
My plan is to design a system where the user can choose which data it is they would like to represent.  
 
The first set of graphs will look at the average unemployment/employment by province in each industry as an aggregate value using data from the years 2014-2019.  
We are using the aggregated data since the larger sample size gives us more accurate data. 
The option to select by year exists, along with the possibility of choosing an additional pivot such as age, industry or sex.  These options have to be typed out in the same way that they exist in the database, which could be tricky.  Normally a GUI would be preferred here.  
 
Our dataset did not display data on ethnicities.  
 
While testing initially, I would get values that matched up to my SQL queries.  
However, later on there seemed to be a problem with the employment and unemployment by industry data.  
 

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Part 2: Linking the two datasets
 
In order to link our two datasets, we must find a way to link the two datasets in a logical way.  
The statcan dataset has the following schema: 
 
LabourData(Date,Province,EmploymentStatus, Industry, Sex, Age_Group, Value)

The Data.world dataset has the following schema: 
 
JobSkills(Company,Title, Category, Location, Responsibilities, MinimumQualifications, PreferredQualifications)
 
One way to connect the two datasets would be to use Industry to connect the two datasets.  
 
Each company belongs to a certain industry, which can be easily found by introducing a new Dataset.  
 
The dataset (image below), from Wikipedia’s List of Canadian companies, is an example of a dataset we could introduce to get this information.  
 
The schema is as follows:  
 
NotableCompanies(Name,Industry,Sector, Headquarters,Founded, Notes)
 
We could reduce this schema to:  NotableCompanies(Name,Industry), since those are the only attributes we need.  
 
SQL QUERY: 
SELECT Name,Industry FROM NotableCompanies
 
Since the elements of the industry attributes in NotableCompanies do not necessarily match the industry attributes in LabourData, some processing would have to be done on the NotableCompanies database to get the two attributes to contain the same elements.  
For example, “Financials”, in NotableCompanies would be switched to “Finance and insurance [52]”, as in LabourData.  
 
List of 23 industry categories in StatCan database:
    
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
 

 
https://en.wikipedia.org/wiki/List_of_companies_of_Canada
 
 
 
 
 
At this point, we have 3 Datasets: 
 
LabourData(Date,Province,EmploymentStatus, Industry, Sex, Age_Group, Value)


JobSkills(Company,Title, Category, Location, Responsibilities, MinimumQualifications, PreferredQualifications)
 
NotableCompanies(Name,Industry)
For our dataset, we will make NotableCompanies simply consist of two tuples, since there are only two companies in the JobSkills relation:
 
Name 
Industry
Google
Professional, scientific and technical services [54]
Youtube
Other services (except public administration) [81]

 
 
Assuming JobSkills.Company is a subset of NotableCompanies.Name, we can join the datasets.  
 
select *
from notablecompanies, job_skills ,labour_data
where notablecompanies.name=job_skills.company and notablecompanies.industry=labour_data.industry
limit 5000
 
We have successfully linked the two datasets. 
 
The schema for the above Query includes all of the attributes of LabourData and JobSkills
 
For our last bit of processing, we will extract keywords from the Responsibilities, MinimumQualifications, and PreferredQualifications attributes, and create tuples with those keywords attached as added attributes.  

We can now do processing on the two datasets.  
 
Ultimately, we would like to find a correlation between job skills, and the various attributes in labour data.  
Finding this correlation can help us answer some very interesting questions.


 
For example: 
 
What skills or qualifications might make someone more employable? 
What skills or qualifications  are useful in different industries? 
Which skills or qualifications are more common among different age groups? 
What skills or qualifications are likely to be found amongst men and women? 
 
Although not all of this data is actually stored in the dataset, much of it can be inferred via a good machine learning algorithm.  
 
 
 
Part 3 Setup for Machine Learning algorithm
 
 
Certain skills are correlated with certain industries in a way that is possibly linearly related.  
For example, the technology sector will have a much higher demand for technical skills like programming.  In order to calculate the strength of the correlation between skills (as keywords) and industries, we can look at the frequency at which jobs in some industries demand said skills.  From this we can find a value for the correlation.  
 
Example  (Made up numbers)
Correlation between Programming skill and Employment
Given:
 Programming is mentioned in 11% of job applications in technology sector
Comparatively, it is mentioned in less than 1% of job applications in other sectors
Hypothesis: 
The employability of someone with a programming skill set will strongly correlate to the technology industry.  
If the technology industry is increasing in employment numbers, we know that someone with a programming skill set has good chances of finding employment.  
 
 
To find how different skills correlate to industries, we could form a correlation matrix out of our dataset.  
 
There are many methods for finding the correlation between linearly related variables, including linear regressions and Pearson's correlation.  (Bag of words can be used for pre-processing text data into numerical form)
 
Another method of finding a correlation may be by using neural networks. 
 
A neural network that predicts industry based on all the attributes (except industry)  in the tuples listed in our final dataset.  The expected output would be the industry from the same tuple. 
 
We can create a feed forward Neural Network with randomly initialized weights. (See Neural_Network.py)
The error function for the output would be zero when the expected output matches the predicted output and one when it doesn't.  Through multiple iterations of forward and backwards propagation, the weights would be adjusted for optimal predictions.  This is the learning process.  
 

 
 
 
 
 
 
 
 
 


