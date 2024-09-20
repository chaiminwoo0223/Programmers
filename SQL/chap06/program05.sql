-- 조건에 부합하는 중고거래 상태 조회하기
SELECT BOARD_ID, WRITER_ID, TITLE, PRICE,
       IF(STATUS = "SALE", "판매중", IF(STATUS = "RESERVED", "예약중", "거래완료")) AS "STATUS"
FROM used_goods_board
WHERE DATE_FORMAT(CREATED_DATE, "%Y-%m-%d") = "2022-10-05"
ORDER BY BOARD_ID DESC;