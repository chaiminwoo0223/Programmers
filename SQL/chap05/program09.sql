-- 그룹별 조건에 맞는 식당 목록 출력하기
-- 문제 오류: 리뷰를 가장 많이 작성한 회원 1명을 조회
SELECT MEMBER_NAME, REVIEW_TEXT, DATE_FORMAT(REVIEW_DATE, "%Y-%m-%d") AS REVIEW_DATE
FROM rest_review a
INNER JOIN (SELECT MEMBER_ID FROM rest_review rr GROUP BY MEMBER_ID ORDER BY COUNT(*) DESC LIMIT 1) b ON a.MEMBER_ID = b.MEMBER_ID
INNER JOIN member_profile c ON a.MEMBER_ID = c.MEMBER_ID
ORDER BY REVIEW_DATE, REVIEW_TEXT;