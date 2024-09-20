-- 조건에 맞는 개발자 찾기
-- &: 비트 논리곱 연산자
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM developers
WHERE SKILL_CODE & (SELECT SUM(CODE) FROM skillcodes WHERE NAME IN ("Python", "C#"))
ORDER BY ID;