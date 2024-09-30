-- 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기
SELECT MONTH(START_DATE) AS "MONTH", CAR_ID, count(*) AS RECORDS
FROM car_rental_company_rental_history
WHERE CAR_ID IN (SELECT CAR_ID
                 FROM car_rental_company_rental_history
                 WHERE START_DATE BETWEEN "2022-08-01" AND "2022-10-31"
                 GROUP BY CAR_ID
                 HAVING count(*) >= 5) AND START_DATE BETWEEN "2022-08-01" AND "2022-10-31"
GROUP BY MONTH, CAR_ID
ORDER BY MONTH, CAR_ID DESC;