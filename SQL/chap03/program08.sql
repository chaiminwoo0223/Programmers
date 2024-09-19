-- 진료과별 총 예약 횟수 출력하기
SELECT MCDP_CD AS "진료과 코드", COUNT(*) AS "5월예약건수"
FROM appointment
WHERE DATE_FORMAT(APNT_YMD, "%Y-%m") = "2022-05"
GROUP BY MCDP_CD
ORDER BY 5월예약건수, MCDP_CD;