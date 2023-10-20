Table: Customer

# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | referee_id  | int     |
# +-------------+---------+
# In SQL, id is the primary key column for this table.
# Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.
 

# Find the names of the customer that are not referred by the customer with id = 2.

# Return the result table in any order.

# The result format is in the following example.

 

# Example 1:

# Input: 
# Customer table:
# +----+------+------------+
# | id | name | referee_id |
# +----+------+------------+
# | 1  | Will | null       |
# | 2  | Jane | null       |
# | 3  | Alex | 2          |
# | 4  | Bill | null       |
# | 5  | Zack | 1          |
# | 6  | Mark | 2          |
# +----+------+------------+
# Output: 
# +------+
# | name |
# +------+
# | Will |
# | Jane |
# | Bill |
# | Zack |
# +------+

# My Solution in Pandas

import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    # Fill all the NULL values on the referee_id column with 0
    customer['referee_id'] = customer["referee_id"].fillna(0)
    
    # filter for customers who are not referred by customerID 2
    result_df = customer[customer['referee_id'] != 2]
    return result_df[['name']]