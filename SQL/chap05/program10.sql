-- 상품을 구매한 회원 비율 구하기
-- DISTINCT: 고유한
SELECT YEAR(SALES_DATE) AS YEAR, MONTH(SALES_DATE) AS MONTH,
       COUNT(DISTINCT u.USER_ID) AS PURCHASED_USERS,
       ROUND(COUNT(DISTINCT u.USER_ID)/(SELECT COUNT(*) FROM user_info WHERE JOINED LIKE "2021%"), 1) AS PUCHASED_RATIO
FROM user_info u
RIGHT JOIN online_sale o ON u.USER_ID = o.USER_ID
WHERE JOINED LIKE "2021%"
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;