-- 카테고리 별 도서 판매량 집계하기
SELECT category AS "CATEGORY", SUM(sales) AS "TOTAL_SALES"
FROM book b
INNER JOIN book_sales bs ON b.book_id = bs.book_id
WHERE sales_date >= '2022-01-01' and sales_date <= '2022-01-31'
GROUP BY category
ORDER BY category;