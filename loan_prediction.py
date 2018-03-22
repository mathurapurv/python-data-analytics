import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




def percConvert(ser):
  return ser/float(ser[-1])*100

def readFile() : 
  return pd.read_csv("dataset\\train_loanprediction.csv")


show_graphs=False
df = readFile()

print("type(df) : ", type(df))   #  <class 'pandas.core.frame.DataFrame'>
print("type(df['Gender']) : ",type(df['Gender']))  # <class 'pandas.core.series.Series'>

print("df.shape() : ", df.shape) # df.shape() :  (614, 13)

print("\n-- Print top 2 rows of the data frame --\n")
print(df.head(2))

print("\n-- Print df[2:5]  --\n")
print(df[2:5]) 

print("\n-- Describe the data set -- \n")
print(df.describe())

print("\n-- Distribution of values - group by - for 'Property_Area' -- \n")
print(df['Property_Area'].value_counts()) 

print("\n-- Distribution of values - group by - for 'Gender' -- \n")
print(df['Gender'].value_counts()) 

print("\n--Draw histogram of the DataFrame’s series using matplotlib / pylab. -- \n")

df['ApplicantIncome'].hist(bins=500)
# plt.show()

print("\n-- Filtered data set with conditions and reduced columns -- \n")
df_filtered = df.loc[(df["Gender"]=="Female") & (df["Education"]=="Not Graduate")
             & (df["Loan_Status"]=="Y"), 
             ["Gender","Education","Loan_Status",
             "ApplicantIncome","CoapplicantIncome",
             "LoanAmount"]]  
print(df_filtered)
df_filtered['ApplicantIncome'].hist(bins=50)

print ('\n-- Probility of getting loan for each Credit History class --\n' )
df_pivot = df.pivot_table(values='Loan_Status',
            index=['Credit_History'],
            aggfunc=lambda x: x.map({'Y':1,'N':0}).mean())  


print (df_pivot)

#Determine pivot table
print('\n-- Pivot Table : group by "Gender","Married","Self_Employed" , mean of LoanAmount  -- \n')
impute_grps = df.pivot_table(values=["LoanAmount"], 
                index=["Gender","Married","Self_Employed"],
                aggfunc=np.mean)
print(impute_grps)

# avergae income grouped  by  gender 
print("\n-- avergae income grouped  by  gender  --\n ")  
gender_based_income  = df.pivot_table(values=["ApplicantIncome"] , 
                                        index=["Gender"] , 
                                        aggfunc=np.mean )  

print(gender_based_income)  
gender_based_income['ApplicantIncome'].hist(bins=500)

if show_graphs : 
  plt.show()

# gender vs loan status correlation , using cross tab 
print('-- gender vs loan status correlation , using cross tab  --')
gender_loanstatus_crosstab = pd.crosstab(df['Gender'] , df['Loan_Status'] ,margins=True)
print(gender_loanstatus_crosstab)
print(gender_loanstatus_crosstab.apply(percConvert , axis=1))

#group by

print('\n-- groupby:  [Education , Property_Area] --\n')
data_aggregatedby_Education_Property_Area = df.groupby(['Education' , 'Property_Area'])

print("data_aggregatedby_Education_Property_Area.groups.keys() : ", 
        data_aggregatedby_Education_Property_Area.groups.keys())  

print("\n-- data_aggregatedby_Education_Property_Area.groups[('Not Graduate', 'Semiurban')]  --\n")
print(data_aggregatedby_Education_Property_Area.groups[('Not Graduate', 'Semiurban')])

print("\n--  type(data_aggregatedby_Education_Property_Area.groups[('Not Graduate', 'Semiurban')]) --\n")
print(type(data_aggregatedby_Education_Property_Area.groups[('Not Graduate', 'Semiurban')]))  
        
print("\n--  data_aggregatedby_Education_Property_Area.size() --\n")
print(data_aggregatedby_Education_Property_Area.size())

data_aggregatedby_Education_Property_Area_loanPassed = df[df['Loan_Status']=='Y'].groupby(['Education' , 'Property_Area'])
print("\n--  data_aggregatedby_Education_Property_Area_loanPassed --\n")
print(data_aggregatedby_Education_Property_Area_loanPassed.size())

print("\n-- avergae ApplicantIncome by education and propertytype   --\n")
print(data_aggregatedby_Education_Property_Area['ApplicantIncome'].mean())  


#print(data_aggregatedby_Education_Property_Area['Dependents'].apply(lambda x:   ', '.join(x) )   ) 


print("\n--   --\n")