-- 평균 일일 대여 요금 구하기
SELECT ROUND(AVG(daily_fee)) AS AVERAGE_FEE
FROM car_rental_company_car
WHERE car_type = "SUV";