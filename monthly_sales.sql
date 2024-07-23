SELECT 
DATE_TRUNC('month',Order_Date) AS month,
ROUND(SUM(Sales),2) AS total_sales
FROM superstore_sales
GROUP BY month 
ORDER BY month ;