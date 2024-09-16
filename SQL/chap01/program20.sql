-- 3월에 태어난 여성 회원 목록 출력하기
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, "%Y-%m-%d") AS DATE_OF_BIRTH
FROM member_profile
WHERE GENDER = 'W' AND TLNO IS NOT NULL AND MONTH(DATE_OF_BIRTH) = 03
ORDER BY MEMBER_ID;