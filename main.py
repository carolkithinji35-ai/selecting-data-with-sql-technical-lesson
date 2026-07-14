import sqlite3
import pandas as pd

conn = sqlite3.connect("data.sqlite")
cur = conn.cursor()

# retrieving all the employee data that exists on the table
employee_data = pd.read_sql(
    """
SELECT * 
FROM employees;
""", conn)

# print(employee_data)


employee_names = pd.read_sql("""
SELECT firstname, lastname AS surname
FROM employees;
""", conn)
# print(employee_names)


employee_jobs = pd.read_sql(
    """
        SELECT firstname AS employee, jobTitle,
        CASE
        WHEN jobTitle = "Sales Rep" THEN "Sales Rep"
        ELSE "Other"
        END AS role
        FROM employees
        """, conn
)
# print(employee_jobs)


#  retrieving the number of distinct jobtitles from the table
distinct = pd.read_sql(
    """
        SELECT COUNT(DISTINCT jobTitle) 
        FROM employees
""", conn
)
# print(distinct)

employee_positions = pd.read_sql(
    """
SELECT firstName, lastName, jobTitle,
CASE 
WHEN jobTitle = "Sales Rep" THEN "Sales Rep"
ELSE "NOT Sales Rep"
END AS Role
FROM employees
""", conn
).head(10)
# print(employee_positions)

# Get office locations using "IF ELSE" statements AS "WHEN THEN " statements
office = pd.read_sql(
    """
    SELECT firstName, jobTitle, officeCode,
    CASE
    WHEN officeCode = "1" THEN "HQ"
    WHEN officeCode = "2" THEN "Home Office"
    WHEN officeCode = "3" THEN "NY City"
    WHEN officeCode = "4" THEN "Boston Office"
    WHEN officeCode = "5" THEN "London"
    WHEN officeCode = "6" THEN "Denver"
    WHEN officeCode = "7" THEN "EMEA"
    END AS office
    FROM employees
    
""", conn
)
# print(office)

# get the length of firstNames
firstname_len = pd.read_sql(
    """
    SELECT LENGTH(firstName) AS name_length
    
    FROM employees;
    
""", conn
)
# print(firstname_len)

# get names in  all caps
caps = pd.read_sql(
    """
    SELECT UPPER(firstName) AS name_in_all_caps
    
    FROM employees;
    
""", conn
).head()
# print(caps)


# finding a substring(subset of a string)
employees_initials = pd.read_sql(
    """
    SELECT substr(firstName ,1 , 1)|| "." ||substr(lastName, 1, 1) AS initials
    FROM employees;
""", conn
).head(6)
# print(employees_initials)

# built in Math methods in SQL
order_details = pd.read_sql(
    """
    SELECT * FROM orderDetails
""", conn
).head(20)
# print(order_details)


# ROUNDED prices to the nearest dollar
rounded_price = pd.read_sql(
    """
    SELECT round(priceEach) AS rounded_prices
    FROM orderDetails;
""",conn
).head(10)
# print(rounded_price)


# return prices as intergers
rounded_price_int = pd.read_sql(
    """
    SELECT CAST(round(priceEach) AS INTEGER) AS rounded_prices_int
    FROM orderDetails;
""",conn
).head(10)
# print(rounded_price_int)


# Math operations
total_price = pd.read_sql(
    """
    SELECT priceEach * quantityOrdered AS total_price
    FROM orderDetails
""", conn
).head(10)
print(total_price)

all_orders = pd.read_sql(
    """
    SELECT * FROM orders
""", conn
).head(10)
print(all_orders)

# know how many days there are between the requiredDate and the orderDate for each order

days_remaining = pd.read_sql(
    """
    SELECT julianday(requiredDate) - julianday(orderDate) AS days_from_order_to_required
    FROM orders
""",conn
).head(10)
print(days_remaining)
conn.close()
