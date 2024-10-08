-- 조건에 맞는 사용자 정보 조회하기
SELECT USER_ID, NICKNAME, 
       CONCAT(CITY, ' ', STREET_ADDRESS1, ' ', STREET_ADDRESS2) AS "전체주소",
       CONCAT(SUBSTRING(TLNO, 1, 3), '-', SUBSTRING(TLNO, 4, 4), '-', SUBSTRING(TLNO, 8, 4)) AS "전화번호"
FROM used_goods_board ugb
INNER JOIN used_goods_user ugu ON ugb.WRITER_ID = ugu.USER_ID
GROUP BY WRITER_ID
HAVING COUNT(WRITER_ID) >= 3
ORDER BY USER_ID DESC;