# Capstone-Project-1

<h1>Census Data Standardization and Analysis Pipeline<br/></h1>

**Problem Statement:** <br/> The task is to clean, process, and analyze census data from a given source, including data renaming, missing data handling, state/UT name standardization, new state/UT formation handling, data storage, database connection, and querying. The goal is to ensure uniformity, accuracy, and accessibility of the census data for further analysis and visualization.<br/>

**Technologies Used:** <br/> Python, SQL, MongoDB, Streamlit.<br/>

**Project Workflow:** <br/>Using Python, retrieve census data from a given source and clean it up, which includes data renaming, missing data handling, and name standardization. Load the cleaned data into MongoDB, then pull it back and load it into MySQL DB. Querying the MySQL DB within Python and visualizing the results in Streamlit. 

**Task performed to complete the project:** <br/> **1. Fetching Census Data** - Install necessary Python libraries and Use pandas to read data from the given source.<br/>
**2. Data Cleaning** - Rename columns to have consistent naming conventions. Handle missing data by filling in by using information from other columns. <br/>
**3. Load Cleaned Data into MongoDB** - Used pymongo to connect and load data. <br/>
**4. Fetch Data from MongoDB and Load into MySQL** - Retrieved data from MongoDB and Used SQLAlchemy to connect and load data. <br/>
**5. Querying the DB in Python and Displaying with Streamlit** - Query the data from MySQL and Use Streamlit to display the results. <br/>
