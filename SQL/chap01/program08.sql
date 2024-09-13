-- 조건에 맞는 도서 리스트 출력하기
SELECT book_id AS "BOOK_ID", DATE_FORMAT(published_date, "%Y-%m-%d") AS "PUBLISHED_DATE"
FROM book
WHERE YEAR(published_date) = 2021 AND category = "인문"
ORDER BY published_date;