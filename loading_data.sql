SET datestyle = 'DMY';

COPY superstore_sales(Row_ID, Order_ID, Order_Date, Ship_Date, Ship_Mode, Customer_ID, Customer_Name, Segment, Country, City, State, Postal_Code, Region, Product_ID, Category, Sub_Category, Product_Name, Sales)
FROM 'C:/Users/nupur/computer/Desktop/SuperStore_Sales/archive/train.csv'
DELIMITER ','
CSV HEADER;