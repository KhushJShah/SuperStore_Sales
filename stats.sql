SELECT 
    COUNT(*) AS total_records,
    ROUND(MIN(Sales), 2) AS min_sales,
    ROUND(MAX(Sales), 2) AS max_sales,
    ROUND(AVG(Sales), 2) AS avg_sales,
    ROUND(SUM(Sales), 2) AS total_sales
FROM superstore_sales;
