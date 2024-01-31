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

# 날짜/시간 합치기 - combine
day = datetime.datetime(2024, 2, 12)
time = datetime.time(20, 32, 11)
dt = datetime.datetime.combine(day, time)
print(dt)

# 현재 날짜/시간 - today, now
today = datetime.date.today()
now = datetime.datetime.now()

print("오늘: %s" % today)
print("지금: %s" % now)

# print("함수 수행시간 : %f 초" % (end - start))

# 날짜 뺄셈
day1 = datetime.date(2023, 12, 10)
day2 = datetime.date(2024, 1, 20)

diff = day2 - day1
print(diff)

# 날짜 뺄셈
day1 = datetime.datetime(2023, 12, 10, 15, 2, 3)
day2 = datetime.datetime(2024, 1, 20, 20, 30, 20)

diff = day2 - day1
print(diff)

# 날짜 덧셈
plus = datetime.timedelta(weeks=10, days=10, hours=1, minutes=10, seconds=10)
print(plus)

add = day1 + plus
print(add)


