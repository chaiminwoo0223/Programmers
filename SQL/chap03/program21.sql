-- 년, 월, 성별 별 상품 구매 회원 수 구하기
-- 예시에 답이 있다.
-- DISTINCT: 중복 제거
SELECT YEAR(sales_date) AS YEAR, MONTH(sales_date) AS MONTH, GENDER, COUNT(DISTINCT u.USER_ID) AS USERS
FROM user_info u
RIGHT JOIN online_sale o ON u.USER_ID = o.USER_ID
WHERE GENDER IS NOT NULL
GROUP BY YEAR, MONTH, GENDER
ORDER BY YEAR, MONTH, GENDER;