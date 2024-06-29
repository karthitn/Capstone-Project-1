import sqlalchemy
import mysql.connector
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
db_url = 'mysql://root:guvi@localhost:3306/me32'
engine = create_engine(db_url)
from sqlalchemy import text

with engine.connect() as connection:
    result1 = connection.execute(text("select District,sum(Population) as Total_Population from census group by District order by District"))
    output1 = result1.fetchall()
st.title('Querying MySQL database and showing output in streamlit')
df1 = pd.DataFrame(output1)
st.markdown(" 1.What is the total population of each district?  \n **Query:**  \nselect District,sum(Population) as Total_Population from census group by District order by District  \n**Output:** ")
st.dataframe(df1)

with engine.connect() as connection:
    result2 = connection.execute(text("select District,sum(Population) as Total_Population from census group by District order by District"))
    output2 = result2.fetchall()
df2 = pd.DataFrame(output2)
st.markdown(" 2.How many literate males and females are there in each district?  \n **Query:**  \nselect District,sum(Literate_Male) as Literate_Male,sum(Literate_Female) as Literate_Female from census group by District order by District  \n**Output:** ")
st.dataframe(df2)

with engine.connect() as connection:
    result3 = connection.execute(text("select District,round((sum(Male_Workers)/sum(Male))*100) as Male_Worker_Percent,round((sum(Female_Workers)/sum(Female))*100) as Female_Worker_Percent from census group by District order by District"))
    output3 = result3.fetchall()
df3 = pd.DataFrame(output3)
st.markdown(" 3.What is the percentage of workers (both male and female) in each district?  \n **Query:**  \nselect District,round((sum(Male_Workers)/sum(Male))*100) as Male_Worker_Percent,round((sum(Female_Workers)/sum(Female))*100) as Female_Worker_Percent from census group by District order by District  \n**Output:** ")
st.dataframe(df3)

with engine.connect() as connection:
    result4 = connection.execute(text("select District,sum(LPG_or_PNG_Households) as LPG_or_PNG_Households from census group by District order by District"))
    output4 = result4.fetchall()
df4 = pd.DataFrame(output4)
st.markdown(" 4.How many households have access to LPG or PNG as a cooking fuel in each district?  \n **Query:**  \nselect District,sum(LPG_or_PNG_Households) as LPG_or_PNG_Households from census group by District order by District  \n**Output:** ")
st.dataframe(df4)

with engine.connect() as connection:
    result5 = connection.execute(text("select District,round((sum(Hindus)/sum(Population))*100) as Hindus,round((sum(Muslims)/sum(Population))*100) as Muslims,round((sum(Christians)/sum(Population))*100) as Christians,round((sum(Sikhs)/sum(Population))*100) as Sikhs,round((sum(Buddhists)/sum(Population))*100) as Buddhists,round((sum(Jains)/sum(Population))*100) as Jains,round((sum(Others_Religions)/sum(Population))*100) as Others_Religions,round((sum(Religion_Not_Stated)/sum(Population))*100) as Religion_Not_Stated from census group by District order by District"))
    output5 = result5.fetchall()
df5 = pd.DataFrame(output5)
st.markdown(" 5.What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?  \n **Query:**  \n select District,round((sum(Hindus)/sum(Population))*100) as Hindus,round((sum(Muslims)/sum(Population))*100) as Muslims,round((sum(Christians)/sum(Population))*100) as Christians,round((sum(Sikhs)/sum(Population))*100) as Sikhs,round((sum(Buddhists)/sum(Population))*100) as Buddhists,round((sum(Jains)/sum(Population))*100) as Jains,round((sum(Others_Religions)/sum(Population))*100) as Others_Religions,round((sum(Religion_Not_Stated)/sum(Population))*100) as Religion_Not_Stated from census group by District order by District  \n**Output:** ")
st.dataframe(df5)

with engine.connect() as connection:
    result6 = connection.execute(text("select District,sum(Households_with_Internet) as Households_with_Internet from census group by District order by District"))
    output6 = result6.fetchall()
df6 = pd.DataFrame(output6)
st.markdown(" 6.How many households have internet access in each district?  \n **Query:**  \n select District,sum(Households_with_Internet) as Households_with_Internet from census group by District order by District  \n**Output:** ")
st.dataframe(df6)

with engine.connect() as connection:
    result7 = connection.execute(text("select District,round((sum(Below_Primary_Education)/sum(Literate_Education))*100) as Below_Primary_Education,round((sum(Primary_Education)/sum(Literate_Education))*100) as Primary_Education,round((sum(Middle_Education)/sum(Literate_Education))*100) as Middle_Education,round((sum(Secondary_Education)/sum(Literate_Education))*100) as Secondary_Education,round((sum(Higher_Education)/sum(Literate_Education))*100) as Higher_Education,round((sum(Graduate_Education)/sum(Literate_Education))*100) as Graduate_Education,round((sum(Other_Education)/sum(Literate_Education))*100) as Other_Education from census group by District order by District"))
    output7 = result7.fetchall()
df7 = pd.DataFrame(output7)
st.markdown(" 7.What is the educational attainment distribution (below primary, primary, middle, secondary, etc.) in each district?   \n **Query:**  \n select District,round((sum(Below_Primary_Education)/sum(Literate_Education))*100) as Below_Primary_Education,round((sum(Primary_Education)/sum(Literate_Education))*100) as Primary_Education,round((sum(Middle_Education)/sum(Literate_Education))*100) as Middle_Education,round((sum(Secondary_Education)/sum(Literate_Education))*100) as Secondary_Education,round((sum(Higher_Education)/sum(Literate_Education))*100) as Higher_Education,round((sum(Graduate_Education)/sum(Literate_Education))*100) as Graduate_Education,round((sum(Other_Education)/sum(Literate_Education))*100) as Other_Education from census group by District order by District  \n**Output:** ")
st.dataframe(df7)

with engine.connect() as connection:
    result8 = connection.execute(text("select District,sum(Households_with_Bicycle) as Households_with_Bicycle,sum(Households_with_Car_Jeep_Van) as Households_with_Car_Jeep_Van,sum(Households_with_Radio_Transistor) as Households_with_Radio_Transistor,sum(Households_with_Scooter_Motorcycle_Moped) as Households_with_Scooter_Motorcycle_Moped from census group by District order by District"))
    output8 = result8.fetchall()
df8 = pd.DataFrame(output8)
st.markdown(" 8.How many households have access to various modes of transportation (bicycle, car, radio, television, etc.) in each district?   \n **Query:**  \n select District,sum(Households_with_Bicycle) as Households_with_Bicycle,sum(Households_with_Car_Jeep_Van) as Households_with_Car_Jeep_Van,sum(Households_with_Radio_Transistor) as Households_with_Radio_Transistor,sum(Households_with_Scooter_Motorcycle_Moped) as Households_with_Scooter_Motorcycle_Moped from census group by District order by District  \n**Output:** ")
st.dataframe(df8)

with engine.connect() as connection:
    result9 = connection.execute(text("select District,sum(Condition_of_occupied_census_houses_Dilapidated_Households) as Dilapidated_Households,sum(Households_with_separate_kitchen_Cooking_inside_house) as Houses_with_separate_kitchen,sum(Having_bathing_facility_Total_Households) as Houses_with_bathing_facility,sum(Having_latrine_facility_within_the_premises_Total_Households) as Houses_with_latrine_facility from census group by District order by District"))
    output9 = result9.fetchall()
df9 = pd.DataFrame(output9)
st.markdown(" 9.What is the condition of occupied census houses (dilapidated, with separate kitchen, with bathing facility, with latrine facility, etc.) in each district?   \n **Query:**  \n select District,sum(Condition_of_occupied_census_houses_Dilapidated_Households) as Dilapidated_Households,sum(Households_with_separate_kitchen_Cooking_inside_house) as Houses_with_separate_kitchen,sum(Having_bathing_facility_Total_Households) as Houses_with_bathing_facility,sum(Having_latrine_facility_within_the_premises_Total_Households) as Houses_with_latrine_facility from census group by District order by District  \n**Output:** ")
st.dataframe(df9)

with engine.connect() as connection:
    result10 = connection.execute(text("with temp as (select c._id,District,Household_size_1_to_2_persons,Household_size_3_persons_Households,Household_size_4_persons_Households,Household_size_5_persons_Households,Household_size_6_8_persons_Households,Household_size_9_persons_and_above_Households,coalesce(Household_size_1_to_2_persons,0)+coalesce(Household_size_3_persons_Households,0)+coalesce(Household_size_4_persons_Households,0)+coalesce(Household_size_5_persons_Households,0)+coalesce(Household_size_6_8_persons_Households,0)+coalesce(Household_size_9_persons_and_above_Households,0) as House_size from census c) select h.District,round((sum(h.Household_size_1_to_2_persons)/sum(h.House_size))*100) as House_size_1_to_2_ppl,round((sum(h.Household_size_3_persons_Households)/sum(h.House_size))*100) as House_size_3_ppl,round((sum(h.Household_size_4_persons_Households)/sum(h.House_size))*100) as House_size_4_ppl,round((sum(h.Household_size_5_persons_Households)/sum(h.House_size))*100) as House_size_5_ppl,round((sum(h.Household_size_6_8_persons_Households)/sum(h.House_size))*100) as House_size_6_8_ppl,round((sum(h.Household_size_9_persons_and_above_Households)/sum(h.House_size))*100) as House_size_9_ppl_above from temp h group by h.District order by h.District"))
    output10 = result10.fetchall()
df10 = pd.DataFrame(output10)
st.markdown(" 10.How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.) in each district?   \n **Query:**  \n with temp as (select c._id,District,Household_size_1_to_2_persons,Household_size_3_persons_Households,Household_size_4_persons_Households,Household_size_5_persons_Households,Household_size_6_8_persons_Households,Household_size_9_persons_and_above_Households,coalesce(Household_size_1_to_2_persons,0)+coalesce(Household_size_3_persons_Households,0)+coalesce(Household_size_4_persons_Households,0)+coalesce(Household_size_5_persons_Households,0)+coalesce(Household_size_6_8_persons_Households,0)+coalesce(Household_size_9_persons_and_above_Households,0) as House_size from census c) select h.District,round((sum(h.Household_size_1_to_2_persons)/sum(h.House_size))*100) as House_size_1_to_2_ppl,round((sum(h.Household_size_3_persons_Households)/sum(h.House_size))*100) as House_size_3_ppl,round((sum(h.Household_size_4_persons_Households)/sum(h.House_size))*100) as House_size_4_ppl,round((sum(h.Household_size_5_persons_Households)/sum(h.House_size))*100) as House_size_5_ppl,round((sum(h.Household_size_6_8_persons_Households)/sum(h.House_size))*100) as House_size_6_8_ppl,round((sum(h.Household_size_9_persons_and_above_Households)/sum(h.House_size))*100) as House_size_9_ppl_above from temp h group by h.District order by h.District  \n**Output:** ")
st.dataframe(df10)

with engine.connect() as connection:
    result11 = connection.execute(text("select `State/UT`,sum(coalesce(Households_Rural,0))+sum(coalesce(Urban_Households,0)) as Households from census group by `State/UT` order by `State/UT`"))
    output11 = result11.fetchall()
df11 = pd.DataFrame(output11)
st.markdown(" 11.What is the total number of households in each state?   \n **Query:**  \n select `State/UT`,sum(coalesce(Households_Rural,0))+sum(coalesce(Urban_Households,0)) as Households from census group by `State/UT` order by `State/UT`  \n**Output:** ")
st.dataframe(df11)

with engine.connect() as connection:
    result12 = connection.execute(text("select `State/UT`,sum(Having_latrine_facility_within_the_premises_Total_Households) as Households_with_latrine_facility_within_the_premises from census group by `State/UT` order by `State/UT`"))
    output12 = result12.fetchall()
df12 = pd.DataFrame(output12)
st.markdown(" 12.How many households have a latrine facility within the premises in each state?   \n **Query:**  \n select `State/UT`,sum(Having_latrine_facility_within_the_premises_Total_Households) as Households_with_latrine_facility_within_the_premises from census group by `State/UT` order by `State/UT`  \n**Output:** ")
st.dataframe(df12)

with engine.connect() as connection:
    result13 = connection.execute(text("select `State/UT`,round(AVG(coalesce(Household_size_1_to_2_persons,0))) as Household_size_1_to_2_persons,round(AVG(coalesce(Household_size_3_persons_Households,0))) as Household_size_3_persons_Households,round(AVG(coalesce(Household_size_4_persons_Households,0))) as Household_size_4_persons_Households,round(AVG(coalesce(Household_size_5_persons_Households,0))) as Household_size_5_persons_Households,round(AVG(coalesce(Household_size_6_8_persons_Households,0))) as Household_size_6_8_persons_Households,round(AVG(coalesce(Household_size_9_persons_and_above_Households,0))) as Household_size_9_persons_and_above_Households from census group by `State/UT` order by `State/UT`"))
    output13 = result13.fetchall()
df13 = pd.DataFrame(output13)
st.markdown(" 13.What is the average household size in each state?   \n **Query:**  \n select `State/UT`,round(AVG(coalesce(Household_size_1_to_2_persons,0))) as Household_size_1_to_2_persons,round(AVG(coalesce(Household_size_3_persons_Households,0))) as Household_size_3_persons_Households,round(AVG(coalesce(Household_size_4_persons_Households,0))) as Household_size_4_persons_Households,round(AVG(coalesce(Household_size_5_persons_Households,0))) as Household_size_5_persons_Households,round(AVG(coalesce(Household_size_6_8_persons_Households,0))) as Household_size_6_8_persons_Households,round(AVG(coalesce(Household_size_9_persons_and_above_Households,0))) as Household_size_9_persons_and_above_Households from census group by `State/UT` order by `State/UT`  \n**Output:** ")
st.dataframe(df13)

with engine.connect() as connection:
    result14 = connection.execute(text("select `State/UT`,sum(coalesce(Ownership_Owned_Households,0)) as Owned_Households,sum(coalesce(Ownership_Rented_Households,0)) as Rented_Households from census group by `State/UT` order by `State/UT`"))
    output14 = result14.fetchall()
df14 = pd.DataFrame(output14)
st.markdown(" 14.How many households are owned versus rented in each state?   \n **Query:**  \n select `State/UT`,sum(coalesce(Ownership_Owned_Households,0)) as Owned_Households,sum(coalesce(Ownership_Rented_Households,0)) as Rented_Households from census group by `State/UT` order by `State/UT`  \n**Output:** ")
st.dataframe(df14) 

with engine.connect() as connection:
    result15 = connection.execute(text("select `State/UT`,sum(Type_of_latrine_facility_Pit_latrine_Households) as Type_of_latrine_facility_Pit_latrine_Households,sum(Type_of_latrine_facility_Other_latrine_Households) as Type_of_latrine_facility_Other_latrine_Households,sum(Type_of_latrine_Night_soil_open_drain_Households) as Type_of_latrine_Night_soil_open_drain_Households,sum(Type_of_Latrine_flush_other_system_Households) as Type_of_Latrine_flush_other_system_Households from census group by `State/UT` order by `State/UT`"))
    output15 = result15.fetchall()
df15 = pd.DataFrame(output15)
st.markdown(" 15.What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) in each state?   \n **Query:**  \n select `State/UT`,sum(Type_of_latrine_facility_Pit_latrine_Households) as Type_of_latrine_facility_Pit_latrine_Households,sum(Type_of_latrine_facility_Other_latrine_Households) as Type_of_latrine_facility_Other_latrine_Households,sum(Type_of_latrine_Night_soil_open_drain_Households) as Type_of_latrine_Night_soil_open_drain_Households,sum(Type_of_Latrine_flush_other_system_Households) as Type_of_Latrine_flush_other_system_Households from census group by `State/UT` order by `State/UT`  \n**Output:** ")
st.dataframe(df15) 

with engine.connect() as connection:
    result16 = connection.execute(text("select `State/UT`,sum(Location_of_drinking_water_source_Near_the_premises_Households) as Location_of_drinking_water_source_Near_the_premises_Households from census group by `State/UT` order by `State/UT`"))
    output16 = result16.fetchall()
df16 = pd.DataFrame(output16)
st.markdown(" 16.How many households have access to drinking water sources near the premises in each state?   \n **Query:**  \n select `State/UT`,sum(Location_of_drinking_water_source_Near_the_premises_Households) as Location_of_drinking_water_source_Near_the_premises_Households from census group by `State/UT` order by `State/UT`  \n**Output:** ")
st.dataframe(df16) 

with engine.connect() as connection:
    result17 = connection.execute(text("select `State/UT`,round(AVG(coalesce(Power_Parity_Less_than_Rs_45000,0))) as Power_Parity_Less_than_Rs_45000,round(AVG(coalesce(Power_Parity_Rs_45000_150000,0))) as Power_Parity_Rs_45000_150000,round(AVG(coalesce(Power_Parity_Rs_150000_330000,0))) as Power_Parity_Rs_150000_330000,round(AVG(coalesce(Power_Parity_Rs_330000_545000,0))) as Power_Parity_Rs_330000_545000,round(AVG(coalesce(Power_Parity_Above_Rs_545000,0))) as Power_Parity_Above_Rs_545000 from census group by `State/UT` order by `State/UT`"))
    output17 = result17.fetchall()
df17 = pd.DataFrame(output17)
st.markdown(" 17.What is the average household income distribution in each state based on the power parity categories?   \n **Query:**  \n select `State/UT`,round(AVG(coalesce(Power_Parity_Less_than_Rs_45000,0))) as Power_Parity_Less_than_Rs_45000,round(AVG(coalesce(Power_Parity_Rs_45000_150000,0))) as Power_Parity_Rs_45000_150000,round(AVG(coalesce(Power_Parity_Rs_150000_330000,0))) as Power_Parity_Rs_150000_330000,round(AVG(coalesce(Power_Parity_Rs_330000_545000,0))) as Power_Parity_Rs_330000_545000,round(AVG(coalesce(Power_Parity_Above_Rs_545000,0))) as Power_Parity_Above_Rs_545000 from census group by `State/UT` order by `State/UT`  \n**Output:** ")
st.dataframe(df17)

with engine.connect() as connection:
    result18 = connection.execute(text("with temp as (select `State/UT`,Married_couples_1_Households,Married_couples_2_Households,Married_couples_3_Households,Married_couples_4_Households,Married_couples_5__Households,coalesce(Married_couples_1_Households,0)+coalesce(Married_couples_2_Households,0)+coalesce(Married_couples_3_Households,0)+coalesce(Married_couples_4_Households,0)+coalesce(Married_couples_5__Households,0) as married_couples_total from census) select c.`State/UT`,round((sum(c.Married_couples_1_Households)/sum(married_couples_total))*100) as Married_couples_1_Households,round((sum(c.Married_couples_2_Households)/sum(married_couples_total))*100) as Married_couples_2_Households,round((sum(c.Married_couples_3_Households)/sum(married_couples_total))*100) as Married_couples_3_Households,round((sum(c.Married_couples_4_Households)/sum(married_couples_total))*100) as Married_couples_4_Households,round((sum(c.Married_couples_5__Households)/sum(married_couples_total))*100) as Married_couples_5_Households from temp c group by c.`State/UT` order by c.`State/UT`"))
    output18 = result18.fetchall()
df18 = pd.DataFrame(output18)
st.markdown(" 18.What is the percentage of married couples with different household sizes in each state?   \n **Query:**  \n with temp as (select `State/UT`,Married_couples_1_Households,Married_couples_2_Households,Married_couples_3_Households,Married_couples_4_Households,Married_couples_5__Households,coalesce(Married_couples_1_Households,0)+coalesce(Married_couples_2_Households,0)+coalesce(Married_couples_3_Households,0)+coalesce(Married_couples_4_Households,0)+coalesce(Married_couples_5__Households,0) as married_couples_total from census) select c.`State/UT`,round((sum(c.Married_couples_1_Households)/sum(married_couples_total))*100) as Married_couples_1_Households,round((sum(c.Married_couples_2_Households)/sum(married_couples_total))*100) as Married_couples_2_Households,round((sum(c.Married_couples_3_Households)/sum(married_couples_total))*100) as Married_couples_3_Households,round((sum(c.Married_couples_4_Households)/sum(married_couples_total))*100) as Married_couples_4_Households,round((sum(c.Married_couples_5__Households)/sum(married_couples_total))*100) as Married_couples_5_Households from temp c group by c.`State/UT` order by c.`State/UT`  \n**Output:** ")
st.dataframe(df18) 

with engine.connect() as connection:
    result19 = connection.execute(text("select `State/UT`,sum(coalesce(Power_Parity_Less_than_Rs_45000,0)) as Power_Parity_Less_than_Rs_45000,sum(coalesce(Power_Parity_Rs_45000_150000,0)) as Power_Parity_Rs_45000_150000,sum(coalesce(Power_Parity_Rs_150000_240000,0)) as Power_Parity_Rs_150000_240000 from census group by `State/UT` order by `State/UT`"))
    output19 = result19.fetchall()
df19 = pd.DataFrame(output19)
st.markdown(" 19.How many households fall below the poverty line in each state based on the power parity categories?   \n **Query:**  \n select `State/UT`,sum(coalesce(Power_Parity_Less_than_Rs_45000,0)) as Power_Parity_Less_than_Rs_45000,sum(coalesce(Power_Parity_Rs_45000_150000,0)) as Power_Parity_Rs_45000_150000,sum(coalesce(Power_Parity_Rs_150000_240000,0)) as Power_Parity_Rs_150000_240000 from census group by `State/UT` order by `State/UT`  \n**Output:** ")
st.dataframe(df19) 

with engine.connect() as connection:
    result20 = connection.execute(text("select `State/UT` , round((sum(Literate)/sum(Population))*100) as  Literacy_Rate from census group by `State/UT` order by `State/UT`"))
    output20 = result20.fetchall()
df20 = pd.DataFrame(output20)
st.markdown(" 20.What is the overall literacy rate (percentage of literate population) in each state?   \n **Query:**  \n select `State/UT` , round((sum(Literate)/sum(Population))*100) as  Literacy_Rate from census group by `State/UT` order by `State/UT`  \n**Output:** ")
st.dataframe(df20) 