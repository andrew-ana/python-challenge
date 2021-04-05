#!/usr/bin/env python
# coding: utf-8

# In[1]:


## OMIMP
## Andrew Anastasiades

#  O   M   I   M   P  
#  H   A       I   A  
#      N       S   N
#              S   D
#                  A
#                  S


# In[2]:


##Dependencies
import os
import csv


# In[25]:


##File Path Parameters
budget_data_path = os.path.join("Resources", "budget_data.csv") #Budget Data File Path
results_file_path = os.path.join("Analysis","Financial Analysis.txt")


# In[4]:


##READ FILE
data_list = list() #List to hold rows #OMIMP
with open(budget_data_path) as budget_file:
    csvreader = csv.reader(budget_file, delimiter=',') #Reader Object
    header = next(csvreader) # Get Column Heads #OMIMP
    for row in csvreader:
        data_list.append(row)
    #Now we can close File


# In[55]:


## ANALYZE DATA
# List Comprehensions to make life easier
month_list = [row[0] for row in data_list] #MONTHS
income_values = [int(row[1]) for row in data_list] #INCOME
changes = [income_values[i]-income_values[i-1] for i in range(1, len(income_values))] #CHANGES

total_months = len(month_list)
total_income = sum(income_values)


average_change = sum(changes) / len(changes)
greatest = max(changes)
least = min(changes)

greatest_increase = [month_list[changes.index(greatest)+1], greatest] # you have to add one to month index bcause first month has no change
greatest_decrease = [month_list[changes.index(least)+1], least] # [month , change]


# In[56]:


##WRITE RESULTS 
with open(results_file_path, "w") as results:
    
    results.write(f"Financial Analysis")
    print(f"Financial Analysis")
    
    results.write(f"--------------------------")
    print(f"--------------------------")
    
    results.write(f"Total Months: {total_months}")
    print(f"Total Months: {total_months}")
    
    results.write(f"Total: {total_income}")
    print(f"Total: ${total_income}")
    
    results.write(f"Average Change: ${average_change}")
    print(f"Average Change: ${average_change}")
    
    results.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
    
    results.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
    

