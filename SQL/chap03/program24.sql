-- 언어별 개발자 분류하기
-- WITH 절
WITH front AS(
    SELECT SUM(CODE)
    FROM skillcodes
    WHERE CATEGORY = "Front End")
    
SELECT CASE
       WHEN SKILL_CODE & (SELECT * FROM front) AND SKILL_CODE & (SELECT SUM(CODE) FROM skillcodes WHERE NAME = "Python") THEN "A"
       WHEN SKILL_CODE & (SELECT SUM(CODE) FROM skillcodes WHERE NAME = "C#") THEN "B"
       WHEN SKILL_CODE & (SELECT * FROM front) THEN "C"
       END AS GRADE, 
       ID,
       EMAIL
FROM developers
HAVING GRADE IS NOT NULL -- MySQL에서 예외적으로 허용
ORDER BY GRADE, ID;