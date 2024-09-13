-- 조건에 맞는 도서와 저자 리스트 출력하기
SELECT book_id AS "BOOK_ID", author_name AS "AUTHOR_NAME", DATE_FORMAT(published_date, "%Y-%m-%d") AS "PUBLISHED_DATE"
FROM book b
INNER JOIN author a ON b.author_id = a.author_id
WHERE category = "경제"
ORDER BY published_date;