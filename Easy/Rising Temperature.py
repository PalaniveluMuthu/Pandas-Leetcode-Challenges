# Table: Weather

# +---------------+---------+
# | Column Name   | Type    |
# +---------------+---------+
# | id            | int     |
# | recordDate    | date    |
# | temperature   | int     |
# +---------------+---------+
# id is the column with unique values for this table.
# This table contains information about the temperature on a certain day.
 

# Write a solution to find all dates' Id with higher temperatures compared to its previous dates (yesterday).

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Weather table:
# +----+------------+-------------+
# | id | recordDate | temperature |
# +----+------------+-------------+
# | 1  | 2015-01-01 | 10          |
# | 2  | 2015-01-02 | 25          |
# | 3  | 2015-01-03 | 20          |
# | 4  | 2015-01-04 | 30          |
# +----+------------+-------------+
# Output: 
# +----+
# | id |
# +----+
# | 2  |
# | 4  |
# +----+
# Explanation: 
# In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
# In 2015-01-04, the temperature was higher than the previous day (20 -> 30).

#Pandas Schema 

# data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
# weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})

# My Solution in Pandas

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    # Sort the data frame by record Date and replace it in the existing DF using inplace
    
    weather.sort_values(by='recordDate', inplace=True)
    
    # find difference of previous record by using DF.diff() command.
    #This will check if the current temperature is greater than the current record and date difference is 1

    return weather[(weather.temperature.diff() > 0 &
    (weather.recordDate.diff().dt.days == 1))][['id']]
    