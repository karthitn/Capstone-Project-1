#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


path = r'C:\Users\Karth\Downloads\census_2011.xlsx'


# In[5]:


df = pd.read_excel(path)


# In[6]:


df


# In[ ]:


#Task 1: Rename the Column names


# In[7]:


df.columns


# In[8]:


df.rename(columns={"State name":"State/UT","District name":"District","Male_Literate":"Literate_Male",
                  "Female_Literate":"Literate_Female","Rural_Households":"Households_Rural",
                  "Urban_ Households":"Households_Urban","Age_Group_0_29":"Young_and_Adult",
                  "Age_Group_30_49":"Middle_Aged","Age_Group_50":"Senior_Citizen",
                  "Age not stated":"Age_Not_Stated"},inplace = True )


# In[9]:


df


# In[23]:


#Task 2: Rename State/UT Names


# In[10]:


def title_case_except_and(text):
    return text.title().replace(" And ", " and ")
df['State/UT'] = df['State/UT'].apply(title_case_except_and)


# In[11]:


df


# In[26]:


#Task 3: New State/UT formation


# In[12]:


districts_in_telangana = ['Adilabad','Nizamabad','Karimnagar','Medak','Hyderabad', 'Ranga Reddy', 'Nalgonda','Mahbubnagar','Warangal','Khammam']


# In[13]:


df.loc[df['District'].isin(districts_in_telangana), 'State/UT'] = 'Telangana'


# In[14]:


df


# In[15]:


filtered_df = df[['State/UT','District']][df['State/UT'] == 'Telangana']


# In[16]:


filtered_df


# In[17]:


filtered_df1 = df[['State/UT','District']][df['State/UT'] == 'Jammu and Kashmir']
filtered_df1


# In[18]:


df.loc[df['District'].isin(['Leh(Ladakh)','Kargil']), 'State/UT'] = 'Ladakh'


# In[19]:


filtered_df1 = df[['State/UT','District']][df['State/UT'] == 'Ladakh']
filtered_df1


# In[20]:


df


# In[36]:


#Task 4: Find and process Missing Data


# In[21]:


df.isnull().sum()


# In[22]:


df.isnull().sum().sum()


# In[23]:


df_null = df.isnull().mean()*100
df_null


# In[24]:


#percentage of data missing for the columns before applying chnages
pd.set_option('display.max_colwidth', 200)
df_null.to_frame().T


# In[25]:


Fill_Male_NA = df['Population']-df['Female']
df['Male'] = df['Male'].fillna(Fill_Male_NA)
Fill_Female_NA = df['Population']-df['Male']
df['Female'] = df['Female'].fillna(Fill_Female_NA)
Fill_Population = df['Male']+df['Female']
df['Population'] = df['Population'].fillna(Fill_Population)

Fill_Male_Lit_NA = df['Literate']-df['Literate_Female']
df['Literate_Male'] = df['Literate_Male'].fillna(Fill_Male_Lit_NA)
Fill_Female_Lit_NA = df['Literate']-df['Literate_Male']
df['Literate_Female'] = df['Literate_Female'].fillna(Fill_Female_Lit_NA)
Fill_Lit_NA = df['Literate_Male']+df['Literate_Female']
df['Literate'] = df['Literate'].fillna(Fill_Lit_NA)

Fill_Pop_by_Age = df['Young_and_Adult']+df['Middle_Aged']+df['Senior_Citizen']+df['Age_Not_Stated']
df['Population'] = df['Population'].fillna(Fill_Pop_by_Age)

Fill_House_Rur_NA = df['Households']-df['Urban_Households']
df['Households_Rural'] = df['Households_Rural'].fillna(Fill_House_Rur_NA)
Fill_House_Urb_NA = df['Households']-df['Households_Rural']
df['Urban_Households'] = df['Urban_Households'].fillna(Fill_House_Urb_NA)
Fill_Household_NA = df['Urban_Households']+df['Households_Rural']
df['Households'] = df['Households'].fillna(Fill_Household_NA)


# In[26]:


pd.set_option('display.max_colwidth', 200)
df.isnull().sum().to_frame().T


# In[27]:


#percentage of data missing for the columns after applying chnages
df_null = df.isnull().mean()*100
pd.set_option('display.max_colwidth', 200)
df_null.to_frame().T


# In[44]:


#Task  5: Save Data to MongoDB


# In[28]:


import pymongo
import json


# In[29]:


client = pymongo.MongoClient('localhost',27017)


# In[30]:


db = client['me32']


# In[31]:


df.shape


# In[32]:


data = df.to_dict(orient = "records")


# In[33]:


data


# In[34]:


db = client['me32']


# In[48]:


#Below three lines to delete the all documents in the "census" collection
mycol = db['census']


# In[49]:


x = mycol.delete_many({})


# In[50]:


print(x.deleted_count, " documents deleted.")


# In[51]:


db.census.insert_many(data)


# In[52]:


collection = db['census']


# In[ ]:


#Fetching the Data from the mongoDB


# In[53]:


# Fetch data as a cursor
cursor = collection.find({})
cursor


# In[54]:


# Convert cursor to list of dictionaries
data_list = list(cursor)


# In[55]:


data_list


# In[56]:


#Converting the data into tabular formart
mongodbdata = pd.DataFrame(data_list)


# In[57]:


mongodbdata


# In[ ]:


#Upload the data fetched from mongodb into mysql db


# In[117]:


pip install sqlalchemy


# In[58]:


import sqlalchemy


# In[59]:


from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData


# In[60]:


#MySQL database URL
db_url = 'mysql://root:guvi@localhost:3306/me32'


# In[61]:


# Create SQLAlchemy engine to connect to the MySQL database
engine = create_engine(db_url)


# In[44]:


#Converting the data into tabular formart
mongodbdata = pd.DataFrame(data_list)


# In[103]:


#Renamed the following column names because it has reached the limit on the length of identifier names
mongodbdata.rename(columns = {"Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car":"Households_with_TV_Comp_Laptop_Tel_mobile_phone_and_Scooter_Car",
                              "Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households":"Type_of_latrine_Night_soil_open_drain_Households",
                              "Type_of_latrine_Flush_pour_flush_connected_to_other_system_Households":"Type_of_Latrine_flush_other_system_Households",
                              "Not_having_latrine_facility_within_the_premises_Alternative_source_Open_Households":"No_latrine_Alt_Source_Open_Households",
                              "Main_source_of_drinking_water_Handpump_Tubewell_Borewell_Households":"Main_water_source_Handpump_Tubewell_Borewell",
                              "Main_source_of_drinking_water_Other_sources_Spring_River_Canal_Tank_Pond_Lake_Other_sources__Households":"Main_water_source_Other_Spring_River_Canal_Tank_Pond_Lake"},inplace=True)


# In[104]:


#insert the data into the MySQL database
mongodbdata.to_sql('census', con=engine, if_exists='append', index=False)


# In[45]:


from sqlalchemy import text


# In[62]:


# Example: Execute a SELECT query using SQLAlchemy Core
with engine.connect() as connection:
    result = connection.execute(text("select sum(Population) as Total_Population,District from census group by District order by District"))
    output = result.fetchall()


# In[63]:


output


# In[127]:


import streamlit as st


# In[128]:


st.write("output")


# In[135]:


streamlit run Census.py


# In[ ]:





# In[ ]:





# In[ ]:




