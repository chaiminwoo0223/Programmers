-- 조회수가 가장 많은 중고거래 게시판의 첨부파일 조회하기
SELECT CONCAT("/home/grep/src/", ub.BOARD_ID, "/", FILE_ID, FILE_NAME, FILE_EXT) AS "FILE_PATH"
FROM (SELECT * FROM used_goods_board ORDER BY VIEWS DESC LIMIT 1) ub
INNER JOIN used_goods_file uf ON ub.BOARD_ID = uf.BOARD_ID
ORDER BY FILE_ID DESC;