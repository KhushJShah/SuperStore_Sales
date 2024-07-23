SELECT 
    Ship_Mode, 
    ROUND(SUM(Sales), 2) AS total_sales
FROM superstore_sales
GROUP BY Ship_Mode
ORDER BY total_sales DESC;
