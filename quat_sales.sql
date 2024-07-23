SELECT 
    EXTRACT(YEAR FROM Order_Date) AS year,
    EXTRACT(QUARTER FROM Order_Date) AS quarter,
    ROUND(SUM(Sales), 2) AS total_sales
FROM superstore_sales
GROUP BY year, quarter
ORDER BY year, quarter;
