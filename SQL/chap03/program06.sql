-- 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기
SELECT car_type AS "CAR_TYPE", COUNT(*) AS "CARS"
FROM car_rental_company_car
WHERE options LIKE "%시트%"
GROUP BY car_type
ORDER BY car_type;