-- 조건에 맞는 회원수 구하기
SELECT COUNT(*) AS "USERS"
FROM user_info
WHERE (joined BETWEEN "2021-01-01" AND "2021-12-31") AND (age BETWEEN 20 AND 29);