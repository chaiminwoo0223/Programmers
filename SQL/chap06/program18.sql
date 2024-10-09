-- 자동차 대여 기록 별 대여 금액 구하기
SELECT HISTORY_ID, 
       ROUND(CASE 
             WHEN DATEDIFF(END_DATE, START_DATE)+1 < 7 THEN 1
             WHEN DATEDIFF(END_DATE, START_DATE)+1 < 30 THEN 0.95
             WHEN DATEDIFF(END_DATE, START_DATE)+1 < 90 THEN 0.92
             ELSE 0.85
             END * DAILY_FEE * (DATEDIFF(END_DATE, START_DATE)+1)) AS FEE
FROM car_rental_company_car cc
INNER JOIN car_rental_company_rental_history ch ON cc.CAR_ID = ch.CAR_ID
INNER JOIN car_rental_company_discount_plan cd ON cc.CAR_TYPE = cd.CAR_TYPE
WHERE cc.CAR_TYPE = "트럭"
GROUP BY HISTORY_ID
ORDER BY FEE DESC, HISTORY_ID DESC;