#!/usr/bin/env python
# coding: utf-8

# # Python Turotial: Work with CSV

# In[ ]:





# # Reading 

# ### Read CSV using Python's inbuilt standard library csv

# In[19]:


import csv


# In[20]:


file = open('Salary_Data.csv')
type(file)


# In[21]:


csvreader = csv.reader(file)


# In[22]:


header = []
header = next(csvreader)
header


# In[23]:


rows = []
for row in csvreader:
    rows.append(row)
rows


# In[8]:


file.close()


# #### complete code

# In[26]:


import csv
file = open("Salary_Data.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
print(rows)
file.close()


# ### using with()

# In[27]:


import csv
rows = []

with open("Salary_Data.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
        
print(header)
print(rows)


# ## using .readlines()

# In[31]:


with open('Salary_Data.csv') as file:
    content = file.readlines()
header = content[:1]
rows = content[1:]
print(header)
print(rows)


# ## using pandas

# In[34]:


import pandas as pd
data = pd.read_csv('Salary_Data.csv')
data


# In[35]:


data.columns


# In[15]:


data.Salary


# # Writing

# In[ ]:





# ### Writing to a CSV file using csv.writer

# In[83]:


import csv


# In[36]:


header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]


# In[37]:


filename = 'Students_Data.csv'
with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file) # 2. create a csvwriter object
    csvwriter.writerow(header) # 4. write the header
    csvwriter.writerows(data) # 5. write the rest of the data


# ### Writing to a CSV file using .write()

# In[38]:


header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]

filename = 'Student_scores.csv'
with open(filename, 'w') as file:
    
    for header in header:
        file.write(str(header)+', ')
    file.write('\n')
    for row in data:
        for x in row:
            file.write(str(x)+', ')
        file.write('\n')


# ### Write to a CSV using Pandas

# In[39]:


import pandas as pd
header = ['Name', 'M1 Score', 'M2 Score']
data = [['Alex', 62, 80], ['Brad', 45, 56], ['Joey', 85, 98]]
data = pd.DataFrame(data, columns=header)
data.to_csv('Stu_data.csv', index=False)


# In[64]:


import csv
import pandas as pd

# open file
with open('AMZN.csv') as csvDataFile:
# read file as csv
    csvReader = csv.reader(csvDataFile)

# print row by row
    rowcount=0
    for row in csvReader:
        rowcount+=1
        print(row[0])
    print("There are " + str(rowcount) + " rows in the file.")
    


# In[65]:


import pandas as pd
data = pd.read_csv('AMZN.csv')
data


# In[67]:


import pandas as pd
data = pd.read_csv('AMZN.csv')
#Select 'open' from amzn where date =='2021-06-30'
print(data['Open'].loc[data['Date'] == '2021-06-30'])

#Select * from amzn where date =='2021-06-30'
print(data.loc[data['Date'] == '2021-06-30'])


# In[ ]:




