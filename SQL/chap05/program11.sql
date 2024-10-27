-- FrontEnd 개발자 찾기
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME 
FROM developers
WHERE SKILL_CODE & (SELECT SUM(CODE) FROM skillcodes WHERE CATEGORY = "Front End")
ORDER BY ID;