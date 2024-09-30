-- 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기
-- CASE문: CASE ~ WHEN ~ THEN ~ ELSE ~ END, 프로그래밍 언어의 switch문과 유사함
SELECT CAR_ID,
       CASE
           WHEN MAX(CASE WHEN "2022-10-16" BETWEEN START_DATE AND END_DATE THEN 1 ELSE 0 END) = 1 
           THEN "대여중"
           ELSE "대여 가능"
        END AS "AVAILABILITY"
FROM car_rental_company_rental_history
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;