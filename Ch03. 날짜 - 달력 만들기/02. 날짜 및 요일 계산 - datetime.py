import datetime

# 날짜 표현 - datetime.date
day1 = datetime.date(2024, 2, 10)
print(day1)

# 날짜/시간 표현 - datetime.datetime
day2 = datetime.datetime(2024, 2, 10, 16, 10, 20)
print(day2)
print(day2.year)  # 연도
print(day2.month)  # 월
print(day2.day)  # 날짜
print(day2.hour)  # 시간
print(day2.minute)  # 분
print(day2.second)  # 초

