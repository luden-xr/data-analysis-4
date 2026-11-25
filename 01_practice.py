import csv

LOT = dp("17_열처리.csv")  # 오늘의 주 데이터
PROC = dp("17_열처리_공정.csv")  # 빈 칸이 섞인 파일
WIDE = dp("20_cmapss_fd001_sample.csv")  # 열 수만 셉니다

with open(LOT, encoding="utf-8-sig") as f:
    r = csv.reader(f)
    header = next(r)  # 첫 줄은 열 이름이라 따로 꺼냅니다
    rows = list(r)  # 나머지가 데이터
