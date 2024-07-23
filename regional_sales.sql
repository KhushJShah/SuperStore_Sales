SELECT 
    Region, 
    ROUND(SUM(Sales), 2) AS total_sales
FROM superstore_sales
GROUP BY Region
ORDER BY total_sales DESC;