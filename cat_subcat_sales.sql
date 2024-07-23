SELECT Category,sub_category, COUNT(*) AS ORDER_COUNT
FROM superstore_sales
GROUP BY Category, sub_category
ORDER BY order_count DESC;