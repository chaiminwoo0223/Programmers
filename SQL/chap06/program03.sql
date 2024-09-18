-- 자동차 대여 기록에서 장기/단기 대여 구분하기
-- 예1) 대여 시작일 = 2022-09-01, 대여 종료일 = 2022-09-01, 대여 기간 = 1, 단기 대여
-- 예2) 대여 시작일 = 2022-09-01, 대여 종료일 = 2022-09-30, 대여 기간 = 30, 장기 대여
SELECT history_id AS "HISTORY_ID", 
       car_id AS "CAR_ID", 
       DATE_FORMAT(start_date, "%Y-%m-%d") AS "START_DATE",
       DATE_FORMAT(end_date, "%Y-%m-%d") AS "END_DATE",
       IF((DATEDIFF(end_date, start_date) + 1) >= 30, "장기 대여", "단기 대여") AS "RENT_TYPE"
FROM car_rental_company_rental_history
WHERE DATE_FORMAT(start_date, "%Y-%m") = "2022-09"
ORDER BY history_id DESC;