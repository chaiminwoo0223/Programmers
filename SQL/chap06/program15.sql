-- 대여 기록이 존재하는 자동차 리스트 구하기
SELECT cr.car_id AS "CAR_ID"
FROM car_rental_company_car cr
INNER JOIN car_rental_company_rental_history ch ON cr.car_id = ch.car_id
WHERE cr.car_type = "세단" and MONTH(ch.start_date) = "10"
GROUP BY cr.car_id
ORDER BY cr.car_id DESC;